import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import scipy.stats as stats


def plot_distribution(dataframe):
    """
    Plots the distribution of a feature in the dataset."""

    rows = 4
    cols = 4
    total_features = len(dataframe.columns)

    plt.figure(figsize=(20, 20))

    for i, column in enumerate(dataframe.columns, 1):
        plt.subplot(rows, cols, i)
        sns.histplot(dataframe[column], kde=True, bins=20, color="skyblue")
        plt.title(f"Distribution of {column}", fontsize=15)
        plt.xlabel(column, fontsize=12)
        plt.ylabel("Frequency", fontsize=12)
    plt.tight_layout()
    plt.show()


def compute_skewness(dataframe):
    """
    Computes the skewness of each feature in the dataset."""

    skewness = dataframe.apply(stats.skew, nan_policy="omit")
    return skewness


def plot_pairplot(dataframe, hue="Outcome"):
    """
    Parameters:
    dataframe (pd.DataFrame): The dataset to visualize.
    hue (str): Column to color the points by category (e.g., Outcome).

    """
    sns.pairplot(dataframe, hue=hue, diag_kind="kde", corner=True, palette="husl")
    plt.show()


def plot_scatter(dataframe, target, title_suffix=""):
    """
    Plots scatter plots of each feature against the target variable.

    Parameters:
    dataframe (pd.DataFrame): The dataset containing features and target variable.
    target (str): The name of the target variable.
    title_suffix (str): Additional text to add to the title to specify the subset (e.g., "Diabetes" or "No Diabetes").
    """

    rows = 4
    cols = 4
    plt.figure(figsize=(25, 25))

    for i, column in enumerate(dataframe.drop(columns=[target]).columns, 1):
        plt.subplot(rows, cols, i)
        plt.scatter(dataframe[column], dataframe[target], alpha=0.5, color="skyblue")
        plt.title(f"{column} vs {target} ({title_suffix})", fontsize=15)
        plt.xlabel(column, fontsize=12)
        plt.ylabel(target, fontsize=12)

    plt.tight_layout()
    plt.show()
