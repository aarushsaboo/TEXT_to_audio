import streamlit as st
from gtts import gTTS
from io import BytesIO

def text_to_speech(text):
    audio_bytes = BytesIO()
    tts = gTTS(text=text, lang='en', slow=False)
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes

st.title("Text to Speech Converter")

text_source = st.radio("Select text source:", ('Text Input', 'Text File'))

text_input = ""
if text_source == 'Text Input':
    text_input = st.text_area("Enter text to convert to speech:", height=150)

elif text_source == 'Text File':
    uploaded_file = st.file_uploader("Or upload a text file", type="txt")

    if uploaded_file is not None:
        text_input = uploaded_file.read().decode("utf-8")
        st.text_area("File contents:", value=text_input, height=150)

if st.button("Convert to Speech"):
    if text_input:
        audio_bytes = text_to_speech(text_input)
        st.audio(audio_bytes, format="audio/mp3")
        st.download_button(
            label="Download Audio",
            data=audio_bytes,
            file_name="output.mp3",
            mime="audio/mp3"
        )
    else:
        st.warning("Please enter some text or upload a file.")

st.markdown("---")
st.markdown("Made with ❤️ using Streamlit and gTTS")