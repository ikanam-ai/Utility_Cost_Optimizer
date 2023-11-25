import numpy as np
import pandas as pd
from catboost import CatBoostRegressor
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def smape(y_true: pd.DataFrame, y_pred: pd.DataFrame) -> int:
    return 100 * (2 * np.abs(y_pred - y_true) / (np.abs(y_pred) + np.abs(y_true))).mean()


def get_model_stats(model, preprocessor):
    feature_importance = pd.DataFrame({'feature_importance': model.feature_importances_,
                                       'feature_names': preprocessor.get_feature_names_out()}).sort_values(
        by=['feature_importance'],
        ascending=False)

    return feature_importance


def train(X: pd.DataFrame, y: pd.DataFrame) -> tuple[CatBoostRegressor, tuple[float, int]]:
    model_metrics = CatBoostRegressor(iterations=1000,
                                      learning_rate=0.008,
                                      depth=7,
                                      loss_function='MAE',
                                      eval_metric='SMAPE',
                                      verbose=100)

    model = CatBoostRegressor(iterations=1000,
                              learning_rate=0.008,
                              depth=7,
                              loss_function='MAE',
                              eval_metric='SMAPE',
                              verbose=100)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42, shuffle=False)
    model_metrics.fit(X_train, y_train, eval_set=(X_test, y_test), early_stopping_rounds=100)
    y_pred = model_metrics.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    smape_ = smape(y_test, y_pred)
    model.fit(X, y, early_stopping_rounds=100)

    return model, (mae, smape_)


def prepare_data(dataset: pd.DataFrame, numeric_features: list[str]) -> tuple[
    pd.DataFrame, pd.DataFrame, ColumnTransformer]:
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

    return X_train, y, preprocessor


def make_logic(dataset, numeric_features) -> tuple[
    pd.DataFrame, pd.DataFrame, pd.DataFrame, CatBoostRegressor, tuple[float, int]]:
    X, y, processor = prepare_data(dataset, numeric_features)
    model, model_metrics = train(X, y)
    feature_df = get_model_stats(model, processor)
    # model_metrics - 2 числа: [mae, smape]
    # feature_df - датасет полезности фичей

    return feature_df, y, X, model, model_metrics


