import numpy as np


class PredictorService:
    def __init__(self) -> None:
        pass

    def predict(self, tokens: dict) -> np.ndarray:
        return np.asarray([0.1, 0.9])
