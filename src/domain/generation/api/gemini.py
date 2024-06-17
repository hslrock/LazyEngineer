import json

import google.generativeai as genai

from settings import load_settings


class GeminiGenerator:
    def __init__(self, settings):
        self.settings = settings
        genai.configure(api_key=self.settings.GEMINI.API_KEY)

    def generate(self, prompt):
        model = genai.GenerativeModel(model_name=self.settings.GEMINI.MODEL_NAME)
        raw_response = model.generate_content(prompt)
        return raw_response
