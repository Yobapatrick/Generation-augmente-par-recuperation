from transformers import pipeline
from models.config import MODEL_CONFIG


class GenerationModel:

    def __init__(self):
        self.generator = pipeline(
            "text-generation",
            model=MODEL_CONFIG["generation_model"]
        )

    def generate(self, query: str, context: str):
        prompt = f"Contexte:\n{context}\n\nQuestion:\n{query}\n\nRéponse:"
        result = self.generator(
            prompt,
            max_length=MODEL_CONFIG["max_length"],
            temperature=MODEL_CONFIG["temperature"]
        )
        return result[0]["generated_text"]