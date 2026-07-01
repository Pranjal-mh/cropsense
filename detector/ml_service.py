"""
Thin wrapper around a Hugging Face image-classification model.

Two modes, controlled by settings.HF_INFERENCE_MODE (env var
HF_INFERENCE_MODE):

  "api"   (default) - call the free Hugging Face Inference API over HTTP.
                       Only needs `requests`; no ML libraries or GPU needed.
                       Requires an HF_API_TOKEN for reliable access (a
                       generous free tier is available at
                       https://huggingface.co/settings/tokens).

  "local" - load the model once with `transformers` + `torch` and run
            inference in-process. Useful for offline demos or avoiding
            API rate limits. Requires `pip install transformers torch`.
"""

from __future__ import annotations

import io
import logging
import time

import requests
from django.conf import settings
from PIL import Image, UnidentifiedImageError

logger = logging.getLogger(__name__)


class PredictionError(Exception):
    """Raised when the model could not produce a prediction."""


def _validate_image(image_bytes: bytes) -> None:
    """Raise PredictionError if the bytes aren't a readable image."""
    try:
        img = Image.open(io.BytesIO(image_bytes))
        img.verify()
    except (UnidentifiedImageError, OSError) as exc:
        raise PredictionError("The uploaded file is not a valid image.") from exc


def classify_image(image_bytes: bytes) -> list[dict]:
    """
    Run the configured model on raw image bytes.

    Returns a list of {"label": str, "score": float} sorted by descending
    confidence (as returned by the Hugging Face image-classification
    pipeline format).
    """
    _validate_image(image_bytes)

    if settings.HF_INFERENCE_MODE == "local":
        return _classify_local(image_bytes)
    return _classify_via_api(image_bytes)


def _classify_via_api(image_bytes: bytes, retries: int = 3) -> list[dict]:
    headers = {}
    if settings.HF_API_TOKEN:
        headers["Authorization"] = f"Bearer {settings.HF_API_TOKEN}"

    last_error = None
    for attempt in range(retries):
        try:
            response = requests.post(
                settings.HF_API_URL,
                headers=headers,
                data=image_bytes,
                timeout=30,
            )
        except requests.RequestException as exc:
            last_error = str(exc)
            time.sleep(1.5 * (attempt + 1))
            continue

        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and result and "label" in result[0]:
                return result
            raise PredictionError(f"Unexpected response from Hugging Face API: {result}")

        if response.status_code == 503:
            # Model is loading (cold start on the free inference API).
            wait = response.json().get("estimated_time", 5)
            logger.info("HF model still loading, waiting %.1fs", wait)
            time.sleep(min(wait, 15))
            continue

        last_error = f"HTTP {response.status_code}: {response.text[:300]}"
        break

    raise PredictionError(
        f"Could not get a prediction from the Hugging Face Inference API. {last_error or ''}".strip()
    )


_local_pipeline = None


def _classify_local(image_bytes: bytes) -> list[dict]:
    global _local_pipeline

    if _local_pipeline is None:
        try:
            from transformers import pipeline
        except ImportError as exc:
            raise PredictionError(
                "HF_INFERENCE_MODE=local requires `transformers` and `torch`. "
                "Install them with: pip install transformers torch"
            ) from exc

        logger.info("Loading local model %s (first call only)...", settings.HF_MODEL_ID)
        _local_pipeline = pipeline("image-classification", model=settings.HF_MODEL_ID)

    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    return _local_pipeline(image)
