import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


def outlier_remove(dataframe):
    """
    This function removes the outliers from the dataframe.
    Filters the rows based on defined thresholds for each feature.
    """

    # Aplicar filtro de outliers solo en las features
    dataframe_filtered = dataframe[
        (dataframe["Pregnancies"] >= 0)
        & (dataframe["Pregnancies"] <= 13.5)
        & (dataframe["Glucose"] >= 37.12)
        & (dataframe["Glucose"] <= 202.12)
        & (dataframe["BloodPressure"] >= 35.0)
        & (dataframe["BloodPressure"] <= 107.0)
        & (dataframe["SkinThickness"] >= 0.05)
        & (dataframe["SkinThickness"] <= 80.0)
        & (dataframe["Insulin"] >= 0.5)
        & (dataframe["Insulin"] <= 318.12)
        & (dataframe["BMI"] >= 13.35)
        & (dataframe["BMI"] <= 50.55)
        & (dataframe["DiabetesPedigreeFunction"] >= 0)
        & (dataframe["DiabetesPedigreeFunction"] <= 1.2)
        & (dataframe["Age"] > 0)
        & (dataframe["Age"] <= 66.5)
    ]

    return dataframe_filtered


from sklearn.preprocessing import StandardScaler
import pandas as pd


def standardize_features(dataframe):
    """
    This function standardizes the features in the dataframe excluding the 'Outcome' column.
    The features are scaled to have zero mean and unit variance.

    Parameters:
    - dataframe (pd.DataFrame): The input dataframe containing both features and target.

    Returns:
    - pd.DataFrame: A dataframe with standardized features, preserving the 'Outcome' column.
    """
    # Exclude the 'Outcome' column to avoid standardizing the target
    features = dataframe.drop(columns=["Outcome"])

    # Initialize the StandardScaler
    scaler = StandardScaler()

    # Fit the scaler to the features and transform them
    features_scaled = scaler.fit_transform(features)

    # Convert the scaled features back into a DataFrame
    dataframe_standardized = pd.DataFrame(features_scaled, columns=features.columns)

    # Add the 'Outcome' column back to the dataframe
    dataframe_standardized["Outcome"] = dataframe["Outcome"].values

    return dataframe_standardized


def normalize_feature(dataframe):
    """
    This function normalizes the features in the dataframe excluding the 'Outcome' column.
    The features are scaled to have values between 0 and 1.

    Parameters:
    - dataframe (pd.DataFrame): The input dataframe containing both features and target.

    Returns:
    - pd.DataFrame: A dataframe with normalized features, preserving the 'Outcome' column.
    """
    # Exclude the 'Outcome' column to avoid normalizing the target
    features = dataframe.drop(columns=["Outcome"])

    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()

    # Fit the scaler to the features and transform them
    features_scaled = scaler.fit_transform(features)

    # Convert the scaled features back into a DataFrame
    dataframe_normalized = pd.DataFrame(features_scaled, columns=features.columns)

    # Add the 'Outcome' column back to the dataframe
    dataframe_normalized["Outcome"] = dataframe["Outcome"].values

    return dataframe_normalized
