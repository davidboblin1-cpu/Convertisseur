import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="Compresseur d'Images Gratuit", layout="centered")

st.title("🖼️ Compresseur & Convertisseur d'Images")
st.write("Réduisez la taille de vos images JPG/PNG en quelques secondes.")

# Import de l'image par l'utilisateur
uploaded_file = st.file_uploader("Choisissez une image...", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not None:
    # Charge l'image
    image = Image.open(uploaded_file)
    st.image(image, caption="Image originale", use_container_width=True)
    
    # Réglage de la qualité de compression
    quality = st.slider("Qualité de compression (%)", min_value=10, max_value=90, value=60)
    
    # Convertit en RGB si l'image originale a un canal alpha (ex: PNG transparent)
    if image.mode in ("RGBA", "P"):
        image = image.convert("RGB")
    
    # Sauvegarde temporaire en mémoire
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG", quality=quality, optimize=True)
    buffer.seek(0)
    
    # Calcul des tailles
    original_size = len(uploaded_file.getvalue()) / 1024
    compressed_size = len(buffer.getvalue()) / 1024
    gain = 100 - (compressed_size / original_size * 100)
    
    st.success(f"Taille réduite de **{original_size:.1f} KB** à **{compressed_size:.1f} KB** (-{gain:.1f}%) !")
    
    # Bouton de téléchargement
    st.download_button(
        label="Télécharger l'image compressée",
        data=buffer,
        file_name="image_compressee.jpg",
        mime="image/jpeg"
    )
