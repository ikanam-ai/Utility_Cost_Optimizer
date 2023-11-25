import pickle
import pandas as pd


def load_model() -> pd.DataFrame:
    path = "models/base.bin"
    with open(path, "rb") as f:
        return pickle.load(f)
