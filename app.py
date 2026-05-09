import streamlit as st
from modules.camera import camera_translate
from modules.image import image_translate
from modules.voice import voice_translate
from modules.text import text_translate
from modules.history import save_history

st.set_page_config(page_title="Translator Studio", layout="wide")
st.title("🌐 Multi-Modal Translator Studio")

menu = st.sidebar.selectbox("Select Mode", [
    "Live Camera",
    "Image Translator",
    "Voice Translator",
    "Text Translator",
    "History"
])

if menu == "Live Camera":
    st.write("Starting live camera translator...")
    camera_translate()

elif menu == "Image Translator":
    img = st.file_uploader("Upload Image")
    lang = st.selectbox("Language", ["en", "hi", "fr"])
    if img:
        text, translated = image_translate(img, lang)
        st.text_area("Extracted Text", text)
        st.text_area("Translated", translated)
        st.download_button("Download", translated)

elif menu == "Voice Translator":
    lang = st.selectbox("Target Language", ["en", "hi", "fr"])
    if st.button("Start Recording"):
        voice_translate(lang)
        st.success("Translation Played")

elif menu == "Text Translator":
    text = st.text_area("Enter text")
    lang = st.selectbox("Target Language", ["en", "hi", "fr"])
    if st.button("Translate"):
        translated = text_translate(text, lang)
        st.text_area("Translated", translated)
        save_history({"input": text, "output": translated})
