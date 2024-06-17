from domain.generation.api.gemini import GeminiGenerator
from settings import load_settings

SETTINGS = load_settings()

generator = GeminiGenerator(SETTINGS)
response = generator.generate("How does a transformer work?")
