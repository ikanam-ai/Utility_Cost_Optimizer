import pickle


def load_model():
    path = "models/base.bin"

    return pickle.loads(path)
