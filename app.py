import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech
import base64

def main():
    st.title("Multilingual AI Assistant 🤖")

    # Button to start recording
    if st.button("Ask me anything!"):
        with st.spinner("Listening..."):
            text = voice_input()
            
            if not text:
                st.error("Sorry, could not capture your voice. Please try again.")
                return
            
            response = llm_model_object(text)
            
            if not response:
                st.error("Sorry, no response generated. Please try again.")
                return
            
            text_to_speech(response)

            # Display the response text
            st.text_area(label="Response:", value=response, height=350)
            
            # Read the audio file
            audio_file_path = "speech.mp3"
            with open(audio_file_path, 'rb') as audio_file:
                audio_bytes = audio_file.read()
            
            # Base64 encode the audio bytes
            audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
            audio_html = f"""
                <audio controls autoplay loop>
                    <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
                </audio>
            """
            st.markdown(audio_html, unsafe_allow_html=True)

            # Provide a download button for the audio file
            st.download_button(label="Download Speech",
                               data=audio_bytes,
                               file_name="speech.mp3",
                               mime="audio/mp3")

if __name__ == "__main__":
    main()
