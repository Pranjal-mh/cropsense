# 🌿 CropSense — AI Crop Disease Detector

CropSense is a Django + Django REST Framework backend that lets a user upload
a photo of a crop leaf, sends it to a **free pre-trained Hugging Face model**
for classification, and returns the detected disease along with a
practical remedy and prevention tips. It demonstrates a clean
Python/Django + ML integration and a small REST API, plus a minimal HTML
demo page.

## Features

- 📸 **Upload a leaf photo** via a simple web page or directly via the API
- 🤖 **ML inference** through the Hugging Face Inference API (no GPU or local
  model download required) — or optionally run the model locally
- 🌾 Covers **38 crop/disease classes** across 14 crops (Apple, Tomato,
  Potato, Corn, Grape, Pepper, and more), based on the PlantVillage dataset
- 💊 Returns a **description, remedy, and prevention tip** for each diagnosis
- 🗂️ **REST API** built with Django REST Framework, with a browsable API and
  detection history endpoint
- 🧪 Includes a Django test suite

## Tech Stack

- Python 3.11+, Django 5, Django REST Framework
- Hugging Face Inference API (`linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification`
  by default — any plant-disease image-classification model can be swapped in)
- SQLite (default; swap `DATABASES` for Postgres in production)
- Vanilla JS demo frontend (no build step)

## Project Structure

```
cropsense/
├── config/                # Django project settings, URLs, WSGI/ASGI
├── detector/               # The app: models, views, serializers, ML service
│   ├── ml_service.py       # Hugging Face API (or local) wrapper
│   ├── disease_data.py     # Disease name → description/remedy knowledge base
│   ├── models.py           # DetectionRecord (upload history)
│   ├── serializers.py
│   ├── views.py            # API endpoints
│   ├── urls.py
│   └── tests.py
├── templates/detector/index.html   # Minimal upload demo page
├── requirements.txt
├── .env.example
└── manage.py
```

## Getting Started

### 1. Clone & install

```bash
git clone https://github.com/<your-username>/cropsense.git
cd cropsense
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure environment

```bash
cp .env.example .env
```

Get a **free** Hugging Face access token at
https://huggingface.co/settings/tokens and add it to `.env`:

```
HF_API_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxx
```

(The Inference API works without a token too, but you'll hit rate limits
sooner, and some models require it for cold-start loading.)

### 3. Run migrations & start the server

```bash
python manage.py migrate
python manage.py runserver
```

Open **http://127.0.0.1:8000/** for the demo upload page, or use the API
directly.

## REST API

| Method | Endpoint          | Description                                   |
|--------|-------------------|------------------------------------------------|
| POST   | `/api/detect/`    | Upload an image, get back a diagnosis + remedy |
| GET    | `/api/diseases/`  | List all 38 diseases the model can detect      |
| GET    | `/api/history/`   | Last 50 detections (saved automatically)       |
| GET    | `/api/health/`    | Health check / current model config            |

### Example: detect a disease

```bash
curl -X POST http://127.0.0.1:8000/api/detect/ \
  -F "image=@/path/to/leaf.jpg"
```

```json
{
  "prediction": {
    "label": "Tomato___Late_blight",
    "crop": "Tomato",
    "disease": "Late Blight",
    "is_healthy": false,
    "confidence": 0.9231,
    "description": "An aggressive water-mold disease (Phytophthora infestans)...",
    "remedy": "Remove and destroy infected plants immediately, and apply a systemic fungicide...",
    "prevention": "Avoid overhead irrigation, provide good spacing..."
  },
  "alternatives": [
    { "label": "Tomato___Early_blight", "confidence": 0.041, "...": "..." }
  ],
  "model": "linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification"
}
```

## Swapping the ML Model

Any Hugging Face **image-classification** model works — set `HF_MODEL_ID` in
`.env`. If the model's label set differs from PlantVillage's 38 classes,
update `detector/disease_data.py` with matching descriptions/remedies (an
unknown label still returns a sensible generic fallback, so the API never
breaks).

Two inference modes (`HF_INFERENCE_MODE` in `.env`):

- **`api`** (default) — calls the hosted Hugging Face Inference API over
  HTTP. Lightweight, no local ML dependencies.
- **`local`** — loads and runs the model in-process with `transformers` +
  `torch` (`pip install transformers torch`). Useful for offline demos or to
  avoid API rate limits.

## Running Tests

```bash
python manage.py test detector
```

## Notes & Disclaimers

This project is for educational/demo purposes. Predictions from a
general-purpose plant disease classifier should not replace advice from a
professional agronomist or local agricultural extension office, especially
for high-value crops.

## License

MIT — see [LICENSE](LICENSE).
