import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import io

# 1. Configuration de la page
st.set_page_config(
    page_title="Compresseur d'Images Gratuit",
    layout="centered"
)

# 2. Injection du script AdSense (exécuté dès le début pour charger le head)
st.markdown(
    """
    <head>
        <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9695837901552067"
        crossorigin="anonymous"></script>
    </head>
    """,
    unsafe_allow_html=True
)

# --- CORPS DE L'APPLICATION ---
st.title("🖼️ Compresseur & Convertisseur d'Images")
st.write("Réduisez la taille de vos images JPG/PNG en quelques secondes.")

uploaded_file = st.file_uploader("Choisissez une image...", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Image originale", use_container_width=True)
    
    quality = st.slider("Qualité de compression (%)", min_value=10, max_value=90, value=60)
    
    if image.mode in ("RGBA", "P"):
        image = image.convert("RGB")
    
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG", quality=quality, optimize=True)
    buffer.seek(0)
    
    original_size = len(uploaded_file.getvalue()) / 1024
    compressed_size = len(buffer.getvalue()) / 1024
    gain = 100 - (compressed_size / original_size * 100)
    
    st.success(f"Taille réduite de **{original_size:.1f} KB** à **{compressed_size:.1f} KB** (-{gain:.1f}%) !")
    
    st.download_button(
        label="Télécharger l'image compressée",
        data=buffer,
        file_name="image_compressee.jpg",
        mime="image/jpeg"
    )
