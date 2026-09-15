import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import io

# Configuration de la page
st.set_page_config(page_title="Compresseur d'Image", page_icon="🖼️", layout="centered")

st.title("🖼️ Compresseur d'Image en Ligne")
st.write("Téléchargez une image, ajustez la qualité pour réduire sa taille et téléchargez le résultat.")

# ---------------------------------------------------------
# SCRIPT PUBLICITAIRE ADSTERRA
# ---------------------------------------------------------
adsterra_code = """
<script async="async" data-cfasync="false" src="https://pl31361635.profitableratecpmnetwork.com/cd069042531af35912924a12f1e7e736/invoke.js"></script>
<div id="container-cd069042531af35912924a12f1e7e736"></div>
"""

# Affichage de la publicité en haut de page
components.html(adsterra_code, height=100)
# ---------------------------------------------------------

# Téléversement de l'image
uploaded_file = st.file_uploader("Choisissez une image (JPG, PNG, WEBP)", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    st.subheader("Aperçu de l'image originale")
    st.image(image, use_column_width=True)
    
    # Obtenir la taille originale
    original_bytes = uploaded_file.getvalue()
    st.info(f"Taille originale : {len(original_bytes) / 1024:.2f} KB")

    # Reglage de la qualité
    quality = st.slider("Qualité de compression (%)", min_value=10, max_value=90, value=70)

    # Traitement de compression
    output_buffer = io.BytesIO()
    
    # Conversion en RGB si PNG avec transparence pour sauvegarde en JPEG
    if image.mode in ("RGBA", "P"):
        image_to_save = image.convert("RGB")
    else:
        image_to_save = image

    image_to_save.save(output_buffer, format="JPEG", quality=quality, optimize=True)
    compressed_bytes = output_buffer.getvalue()

    st.subheader("Résultat")
    st.success(f"Nouvelle taille : {len(compressed_bytes) / 1024:.2f} KB")

    # Bouton de téléchargement
    st.download_button(
        label="Télécharger l'image compressée",
        data=compressed_bytes,
        file_name="image_compressee.jpg",
        mime="image/jpeg"
    )

    # Rappel de la publicité sous le bouton de téléchargement
    st.markdown("---")
    components.html(adsterra_code, height=100)
