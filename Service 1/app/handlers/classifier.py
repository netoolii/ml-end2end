from injector import inject
from models.text_processing import TextProcessingModel
from models.predictor import PredictorModel


class ClassifierHandler:
    @inject
    def __init__(
        self, text_processing: TextProcessingModel, predictor: PredictorModel
    ) -> None:
        self.text_processing = text_processing
        self.predictor = predictor

    def predictions(self, arg: dict) -> dict:
        text = arg.get("text")
        tokens = self.text_processing.run(text)
        print(tokens)
        result = self.predictor.run(tokens)
        print(result)
        return {}
