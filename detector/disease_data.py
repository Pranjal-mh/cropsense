"""
Static knowledge base used to turn a raw model label (e.g.
"Tomato___Late_blight") into a friendly crop name, disease name,
description, and actionable remedy.

The label format matches the PlantVillage dataset (38 classes), which is
what the default Hugging Face model
(linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification) was
fine-tuned on. If you swap in a different model, update this file to match
its label set.
"""

DISEASE_INFO = {
    "Apple___Apple_scab": {
        "crop": "Apple",
        "disease": "Apple Scab",
        "is_healthy": False,
        "description": "A fungal disease (Venturia inaequalis) causing dark, scabby lesions on leaves and fruit.",
        "remedy": "Remove and destroy fallen leaves, prune for airflow, and apply a fungicide "
        "(e.g. captan or myclobutanil) starting at green tip stage and repeating on a 7-10 day schedule.",
        "prevention": "Plant scab-resistant apple varieties and avoid overhead irrigation.",
    },
    "Apple___Black_rot": {
        "crop": "Apple",
        "disease": "Black Rot",
        "is_healthy": False,
        "description": "A fungal disease (Botryosphaeria obtusa) causing purple leaf spots, fruit rot, and cankers.",
        "remedy": "Prune out dead/cankered wood, remove mummified fruit, and apply a fungicide "
        "labeled for black rot during the growing season.",
        "prevention": "Sanitize pruning tools and remove nearby wild/abandoned apple trees that host the fungus.",
    },
    "Apple___Cedar_apple_rust": {
        "crop": "Apple",
        "disease": "Cedar Apple Rust",
        "is_healthy": False,
        "description": "A fungal disease requiring both apple and cedar/juniper hosts, causing bright orange leaf spots.",
        "remedy": "Apply a protectant fungicide (myclobutanil or mancozeb) from pink bud through several weeks after petal fall.",
        "prevention": "Remove nearby cedar/juniper trees where possible, or plant rust-resistant apple cultivars.",
    },
    "Apple___healthy": {
        "crop": "Apple",
        "disease": "Healthy",
        "is_healthy": True,
        "description": "No signs of disease detected on this apple leaf.",
        "remedy": "No treatment needed. Continue routine monitoring and good orchard hygiene.",
        "prevention": "Maintain balanced fertilization, proper spacing, and regular pest scouting.",
    },
    "Blueberry___healthy": {
        "crop": "Blueberry",
        "disease": "Healthy",
        "is_healthy": True,
        "description": "No signs of disease detected on this blueberry leaf.",
        "remedy": "No treatment needed. Continue routine monitoring.",
        "prevention": "Maintain acidic, well-drained soil and adequate air circulation between bushes.",
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "crop": "Cherry",
        "disease": "Powdery Mildew",
        "is_healthy": False,
        "description": "A fungal disease (Podosphaera clandestina) forming white, powdery patches on leaves and shoots.",
        "remedy": "Apply sulfur or a labeled fungicide at first sign of infection and improve canopy airflow with pruning.",
        "prevention": "Avoid excess nitrogen fertilization and water at the base rather than overhead.",
    },
    "Cherry_(including_sour)___healthy": {
        "crop": "Cherry",
        "disease": "Healthy",
        "is_healthy": True,
        "description": "No signs of disease detected on this cherry leaf.",
        "remedy": "No treatment needed. Continue routine monitoring.",
        "prevention": "Prune for airflow and monitor during warm, humid weather when mildew risk is highest.",
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "crop": "Corn (Maize)",
        "disease": "Gray Leaf Spot",
        "is_healthy": False,
        "description": "A fungal disease (Cercospora zeae-maydis) producing rectangular gray-tan lesions on leaves.",
        "remedy": "Apply a foliar fungicide (strobilurin or triazole) when disease appears before tasseling in susceptible fields.",
        "prevention": "Rotate crops away from corn, use resistant hybrids, and till under infected residue.",
    },
    "Corn_(maize)___Common_rust_": {
        "crop": "Corn (Maize)",
        "disease": "Common Rust",
        "is_healthy": False,
        "description": "A fungal disease (Puccinia sorghi) producing small, reddish-brown raised pustules on both leaf surfaces.",
        "remedy": "Apply a fungicide if rust is severe before tasseling; most field corn tolerates light infections without yield loss.",
        "prevention": "Plant rust-resistant hybrids, especially in areas with a history of severe rust.",
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "crop": "Corn (Maize)",
        "disease": "Northern Leaf Blight",
        "is_healthy": False,
        "description": "A fungal disease (Exserohilum turcicum) causing long, cigar-shaped gray-green lesions on leaves.",
        "remedy": "Apply a foliar fungicide at early disease onset, particularly on susceptible hybrids in humid weather.",
        "prevention": "Rotate crops, till under residue, and choose resistant hybrids.",
    },
    "Corn_(maize)___healthy": {
        "crop": "Corn (Maize)",
        "disease": "Healthy",
        "is_healthy": True,
        "description": "No signs of disease detected on this corn leaf.",
        "remedy": "No treatment needed. Continue routine monitoring.",
        "prevention": "Rotate crops and scout fields regularly during the growing season.",
    },
    "Grape___Black_rot": {
        "crop": "Grape",
        "disease": "Black Rot",
        "is_healthy": False,
        "description": "A fungal disease (Guignardia bidwellii) causing circular brown leaf spots and shriveled, mummified fruit.",
        "remedy": "Remove mummified berries and infected canes, and apply a fungicide program from bud break through veraison.",
        "prevention": "Prune for canopy airflow and clean up fallen leaves/fruit each season.",
    },
    "Grape___Esca_(Black_Measles)": {
        "crop": "Grape",
        "disease": "Esca (Black Measles)",
        "is_healthy": False,
        "description": "A fungal trunk disease complex causing tiger-stripe leaf discoloration and dark berry spotting.",
        "remedy": "There is no cure; remove and destroy severely infected vines/wood and apply trunk-wound protectant after pruning.",
        "prevention": "Prune during dry weather, avoid large pruning wounds, and disinfect tools between vines.",
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "crop": "Grape",
        "disease": "Leaf Blight (Isariopsis Leaf Spot)",
        "is_healthy": False,
        "description": "A fungal disease causing angular brown spots that can merge and cause premature leaf drop.",
        "remedy": "Apply a copper-based or labeled fungicide and remove heavily infected leaves.",
        "prevention": "Improve air circulation through canopy management and avoid overhead irrigation.",
    },
    "Grape___healthy": {
        "crop": "Grape",
        "disease": "Healthy",
        "is_healthy": True,
        "description": "No signs of disease detected on this grape leaf.",
        "remedy": "No treatment needed. Continue routine monitoring.",
        "prevention": "Maintain good canopy airflow and monitor closely during wet weather.",
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "crop": "Orange",
        "disease": "Huanglongbing (Citrus Greening)",
        "is_healthy": False,
        "description": "A serious bacterial disease spread by the Asian citrus psyllid, causing blotchy mottled leaves and misshapen, bitter fruit.",
        "remedy": "There is no cure; remove and destroy infected trees to slow spread and control the psyllid vector with approved insecticides.",
        "prevention": "Source certified disease-free nursery stock and monitor/control psyllid populations.",
    },
    "Peach___Bacterial_spot": {
        "crop": "Peach",
        "disease": "Bacterial Spot",
        "is_healthy": False,
        "description": "A bacterial disease (Xanthomonas) causing small, dark, water-soaked spots on leaves and fruit.",
        "remedy": "Apply copper-based bactericides during dormancy and early season; avoid overhead watering.",
        "prevention": "Plant resistant peach varieties and avoid working in wet orchards to limit bacterial spread.",
    },
    "Peach___healthy": {
        "crop": "Peach",
        "disease": "Healthy",
        "is_healthy": True,
        "description": "No signs of disease detected on this peach leaf.",
        "remedy": "No treatment needed. Continue routine monitoring.",
        "prevention": "Maintain good sanitation and monitor during warm, wet spring weather.",
    },
    "Pepper,_bell___Bacterial_spot": {
        "crop": "Bell Pepper",
        "disease": "Bacterial Spot",
        "is_healthy": False,
        "description": "A bacterial disease (Xanthomonas) causing small, water-soaked spots that turn brown with yellow halos.",
        "remedy": "Apply copper-based bactericides at first sign of disease and remove severely infected plants.",
        "prevention": "Use certified disease-free seed/transplants and avoid overhead irrigation.",
    },
    "Pepper,_bell___healthy": {
        "crop": "Bell Pepper",
        "disease": "Healthy",
        "is_healthy": True,
        "description": "No signs of disease detected on this bell pepper leaf.",
        "remedy": "No treatment needed. Continue routine monitoring.",
        "prevention": "Rotate crops and avoid working in wet fields to reduce bacterial spread.",
    },
    "Potato___Early_blight": {
        "crop": "Potato",
        "disease": "Early Blight",
        "is_healthy": False,
        "description": "A fungal disease (Alternaria solani) causing dark concentric-ringed spots ('target' pattern) on lower leaves.",
        "remedy": "Apply a fungicide (chlorothalonil or azoxystrobin) on a regular schedule once symptoms appear.",
        "prevention": "Rotate crops, avoid overhead irrigation, and ensure balanced soil fertility.",
    },
    "Potato___Late_blight": {
        "crop": "Potato",
        "disease": "Late Blight",
        "is_healthy": False,
        "description": "An aggressive water-mold disease (Phytophthora infestans) causing dark, water-soaked lesions that spread rapidly in cool, wet weather.",
        "remedy": "Apply a systemic fungicide immediately (e.g. mancozeb or chlorothalonil) and remove/destroy infected plants to stop spread.",
        "prevention": "Plant certified disease-free seed potatoes, avoid overhead irrigation, and destroy volunteer plants and cull piles.",
    },
    "Potato___healthy": {
        "crop": "Potato",
        "disease": "Healthy",
        "is_healthy": True,
        "description": "No signs of disease detected on this potato leaf.",
        "remedy": "No treatment needed. Continue routine monitoring.",
        "prevention": "Rotate crops and monitor closely during cool, wet weather when blight risk is highest.",
    },
    "Raspberry___healthy": {
        "crop": "Raspberry",
        "disease": "Healthy",
        "is_healthy": True,
        "description": "No signs of disease detected on this raspberry leaf.",
        "remedy": "No treatment needed. Continue routine monitoring.",
        "prevention": "Prune out old canes after fruiting and maintain good airflow.",
    },
    "Soybean___healthy": {
        "crop": "Soybean",
        "disease": "Healthy",
        "is_healthy": True,
        "description": "No signs of disease detected on this soybean leaf.",
        "remedy": "No treatment needed. Continue routine monitoring.",
        "prevention": "Rotate crops and scout fields regularly, particularly after heavy rain.",
    },
    "Squash___Powdery_mildew": {
        "crop": "Squash",
        "disease": "Powdery Mildew",
        "is_healthy": False,
        "description": "A fungal disease forming white, powdery patches on leaves and stems, reducing yield if untreated.",
        "remedy": "Apply sulfur, potassium bicarbonate, or a labeled fungicide at first sign of disease.",
        "prevention": "Space plants for airflow, avoid overhead watering, and choose resistant varieties.",
    },
    "Strawberry___Leaf_scorch": {
        "crop": "Strawberry",
        "disease": "Leaf Scorch",
        "is_healthy": False,
        "description": "A fungal disease (Diplocarpon earlianum) causing small purple spots that merge into scorched-looking blotches.",
        "remedy": "Remove infected leaves after harvest and apply a labeled fungicide during periods of wet weather.",
        "prevention": "Avoid overhead irrigation and space plants for good air circulation.",
    },
    "Strawberry___healthy": {
        "crop": "Strawberry",
        "disease": "Healthy",
        "is_healthy": True,
        "description": "No signs of disease detected on this strawberry leaf.",
        "remedy": "No treatment needed. Continue routine monitoring.",
        "prevention": "Maintain good bed sanitation and remove old/dead foliage each season.",
    },
    "Tomato___Bacterial_spot": {
        "crop": "Tomato",
        "disease": "Bacterial Spot",
        "is_healthy": False,
        "description": "A bacterial disease (Xanthomonas) causing small, dark, greasy-looking spots on leaves and fruit.",
        "remedy": "Apply copper-based bactericides early and remove heavily infected leaves; avoid working with wet plants.",
        "prevention": "Use certified disease-free seed/transplants and rotate crops for 2-3 years.",
    },
    "Tomato___Early_blight": {
        "crop": "Tomato",
        "disease": "Early Blight",
        "is_healthy": False,
        "description": "A fungal disease (Alternaria solani) causing concentric-ringed 'target' spots on older/lower leaves.",
        "remedy": "Remove infected lower leaves, mulch to reduce soil splash, and apply a fungicide (chlorothalonil or copper).",
        "prevention": "Rotate crops, stake/prune for airflow, and avoid overhead watering.",
    },
    "Tomato___Late_blight": {
        "crop": "Tomato",
        "disease": "Late Blight",
        "is_healthy": False,
        "description": "An aggressive water-mold disease (Phytophthora infestans) causing large, water-soaked, rapidly-spreading lesions.",
        "remedy": "Remove and destroy infected plants immediately, and apply a systemic fungicide preventatively on remaining plants during cool, wet weather.",
        "prevention": "Avoid overhead irrigation, provide good spacing, and remove volunteer tomato/potato plants.",
    },
    "Tomato___Leaf_Mold": {
        "crop": "Tomato",
        "disease": "Leaf Mold",
        "is_healthy": False,
        "description": "A fungal disease (Passalora fulva) common in humid greenhouses, causing yellow spots on top and olive-green mold underneath leaves.",
        "remedy": "Improve ventilation, reduce humidity, and apply a labeled fungicide if the infection persists.",
        "prevention": "Space and prune plants for airflow, and avoid wetting foliage when watering.",
    },
    "Tomato___Septoria_leaf_spot": {
        "crop": "Tomato",
        "disease": "Septoria Leaf Spot",
        "is_healthy": False,
        "description": "A fungal disease causing small, circular spots with dark borders and light gray centers on lower leaves.",
        "remedy": "Remove infected lower leaves promptly and apply a fungicide (chlorothalonil or copper) on a regular schedule.",
        "prevention": "Mulch around plants, avoid overhead watering, and rotate crops each season.",
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "crop": "Tomato",
        "disease": "Two-Spotted Spider Mite Damage",
        "is_healthy": False,
        "description": "A pest infestation causing fine yellow stippling, webbing, and bronzing on leaves.",
        "remedy": "Spray with insecticidal soap or horticultural oil, targeting the undersides of leaves, and introduce predatory mites if available.",
        "prevention": "Keep plants well-watered (mites thrive in dry, dusty conditions) and monitor regularly during hot weather.",
    },
    "Tomato___Target_Spot": {
        "crop": "Tomato",
        "disease": "Target Spot",
        "is_healthy": False,
        "description": "A fungal disease (Corynespora cassiicola) causing brown lesions with concentric rings on leaves and fruit.",
        "remedy": "Apply a labeled fungicide and remove infected foliage to reduce spore spread.",
        "prevention": "Improve airflow through staking/pruning and avoid prolonged leaf wetness.",
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "crop": "Tomato",
        "disease": "Tomato Yellow Leaf Curl Virus",
        "is_healthy": False,
        "description": "A viral disease spread by whiteflies, causing upward-curling, yellowing leaves and stunted growth.",
        "remedy": "There is no cure; remove and destroy infected plants and control whitefly populations with insecticidal soap or approved insecticides.",
        "prevention": "Use virus-resistant tomato varieties and reflective mulches/row covers to deter whiteflies.",
    },
    "Tomato___Tomato_mosaic_virus": {
        "crop": "Tomato",
        "disease": "Tomato Mosaic Virus",
        "is_healthy": False,
        "description": "A viral disease causing mottled light/dark green mosaic patterns and leaf distortion.",
        "remedy": "There is no cure; remove and destroy infected plants. Wash hands and disinfect tools after handling infected plants.",
        "prevention": "Use resistant varieties and certified virus-free seed; avoid tobacco use around plants (a related virus source).",
    },
    "Tomato___healthy": {
        "crop": "Tomato",
        "disease": "Healthy",
        "is_healthy": True,
        "description": "No signs of disease detected on this tomato leaf.",
        "remedy": "No treatment needed. Continue routine monitoring.",
        "prevention": "Rotate crops, stake for airflow, and scout weekly during the growing season.",
    },
}


def get_disease_info(raw_label: str) -> dict:
    """
    Look up friendly info for a raw model label. Falls back to a generic
    response if the label isn't in the knowledge base (e.g. a different
    model was configured), so the API never breaks on an unknown class.
    """
    info = DISEASE_INFO.get(raw_label)
    if info:
        return {"label": raw_label, **info}

    # Fallback: try to make the raw label presentable.
    crop, _, disease = raw_label.partition("___")
    disease = disease.replace("_", " ").strip() or "Unknown"
    is_healthy = "healthy" in raw_label.lower()
    return {
        "label": raw_label,
        "crop": crop.replace("_", " ") or "Unknown",
        "disease": "Healthy" if is_healthy else disease,
        "is_healthy": is_healthy,
        "description": "No detailed information available for this class in the local knowledge base.",
        "remedy": "No treatment needed." if is_healthy else "Consult a local agricultural extension office for a treatment plan.",
        "prevention": "Practice crop rotation, good sanitation, and regular field monitoring.",
    }
