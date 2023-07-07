from injector import inject, singleton
from services.text_processing import TextProcessingService
from services.tokenizer import TokenizerService


class TextProcessingModel:
    @inject
    @singleton
    def __init__(
        self, text_processing: TextProcessingService, tokenizer: TokenizerService
    ) -> None:
        self.text_processing = text_processing
        self.tokenizer = tokenizer

    def run(self, text: str) -> dict:
        text = self.text_processing.run(text)
        tokens = self.tokenizer.predict(text)
        return tokens
