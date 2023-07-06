from injector import inject, singleton
from services.text_processing import TextProcessingService


class TextProcessingModel:
    @inject
    def __init__(self, text_processing: TextProcessingService) -> None:
        self.text_processing = text_processing

    def run(self, text: str) -> dict:
        text = self.text_processing.run(text)
        return {"tokens": [1, 2, 3, 4, 5], "text": text}
