from injector import inject, singleton
from services.predictor import PredictorService
import numpy as np


class PredictorModel:
    @inject
    @singleton
    def __init__(self, prediction_service: PredictorService) -> None:
        self.prediction_service = prediction_service

    def run(self, tokens: dict) -> np.ndarray:
        return self.prediction_service.predict(tokens)
