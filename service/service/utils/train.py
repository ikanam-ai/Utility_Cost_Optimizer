import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler
from catboost import CatBoostRegressor


def smape(y_true, y_pred):
    return 100 * (2 * np.abs(y_pred - y_true) / (np.abs(y_pred) + np.abs(y_true))).mean()


def train(x_train, y_train) -> CatBoostRegressor:
    # TODO сделать вывод метрик
    model = CatBoostRegressor(iterations=1000,
                              learning_rate=0.008,
                              depth=7,
                              loss_function='MAE',
                              eval_metric='SMAPE',
                              verbose=100)

    model.fit(x_train, y_train, eval_set=([], []), early_stopping_rounds=100)

    return model


def prepare_data(dataset: pd.DataFrame, numeric_features: list[str]) -> tuple[pd.DataFrame, pd.DataFrame]:
    numeric_transformer = Pipeline(
        steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
    )

    categorical_features = ["state", "year", "Код статьи"]
    categorical_transformer = Pipeline(
        steps=[
            ("encoder", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )

    X = dataset.drop('Отнесено', axis=1)
    y = dataset['Отнесено'].astype('int')

    X_train = preprocessor.fit_transform(X, y)

    return X_train, y
