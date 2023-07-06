from injector import inject
from models.text_processing import TextProcessingModel


class ClassifierHandler:
    @inject
    def __init__(self, text_processing: TextProcessingModel) -> None:
        self.text_processing = text_processing

    def predictions(self, arg: dict) -> dict:
        text = arg.get("text")
        tokens = self.text_processing.run(text)
        print(tokens)
        return {}
