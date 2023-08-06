from typing import Tuple
import importlib.resources as pkg_resources
from . import files
import pickle
import numpy
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor

CLASSIC, ARAM = 'CLASSIC', 'ARAM'


def get_model(mode: str = CLASSIC) -> Tuple[MLPRegressor, StandardScaler]:
    if mode not in [CLASSIC, ARAM]:
        raise ValueError('Undefined mode for model')
    with pkg_resources.open_binary(files, f'{mode.lower()}_model.pkl') as file:
        model = pickle.load(file)
    with pkg_resources.open_binary(files, f'{mode.lower()}_scaler.pkl') as file:
        scaler = pickle.load(file)
    # with pkg_resources.path(files, f'{mode.lower()}_model.pkl') as path:
    #     async with aiofiles.open(path, 'rb') as file:
    #         model = pickle.load(await file.read())
    # with pkg_resources.open_binary(files, f'{mode.lower()}_scaler.pkl') as file:
    #     scaler = pickle.load(file)
    return model, scaler


def predict(model: MLPRegressor, scaler: StandardScaler, duration_seconds: int, victory: bool) -> int:
    data = numpy.array([[duration_seconds, int(victory)]])
    scaled_data = scaler.transform(data)
    result = model.predict(scaled_data)
    return round(result[0])
