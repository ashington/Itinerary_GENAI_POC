import streamlit as st
import os
import google.generativeai as ggi
from dotenv import load_dotenv

class GeminiChatApp:
    """
    A class to encapsulate the Gemini Pro chat application functionality.
    """

    def __init__(self, api_key_file=".env", model_name="models/learnlm-1.5-pro-experimental"):
        """
        Initializes the GeminiChatApp with API key and model name.

        Args:
            api_key_file (str): Path to the .env file containing the API key.
            model_name (str): Name of the Gemini Pro model.
        """
        self.api_key_file = api_key_file
        self.model_name = model_name
        self.api_key = self._load_api_key()
        self.model = self._configure_model()
        self.chat = self.model.start_chat()

    def _load_api_key(self):
        """
        Loads the API key from the .env file.

        Returns:
            str: The API key.
        """
        load_dotenv(self.api_key_file)
        return os.getenv("API_KEY")

    def _configure_model(self):
        """
        Configures the Gemini Pro model.

        Returns:
            google.generativeai.GenerativeModel: The configured model.
        """
        ggi.configure(api_key=self.api_key)
        return ggi.GenerativeModel(self.model_name)

    def get_llm_response(self, question):
        """
        Sends a question to the Gemini Pro model and returns the response.

        Args:
            question (str): The user's question.

        Returns:
            google.generativeai.types.generation_types.GenerateContentResponseIterator: The model's response.
        """
        return self.chat.send_message(question, stream=True)

    def run(self):
        """
        Runs the Streamlit chat application.
        """
        st.title("Chat Application using Gemini Pro")

        user_quest = st.text_input("Ask a question:")
        btn = st.button("Ask")

        if btn and user_quest:
            result = self.get_llm_response(user_quest)
            st.subheader("Response:")
            for word in result:
                st.text(word.text)

if __name__ == "__main__":
    app = GeminiChatApp()
    app.run()