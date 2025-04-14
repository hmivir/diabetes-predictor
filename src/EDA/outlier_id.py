import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import scipy.stats as stats


def plot_box(dataframe):
    """
    Plots the boxplot with outliers of a feature in the dataset."""

    rows = 4
    cols = 4
    total_features = len(dataframe.columns)
    plt.figure(figsize=(20, 20))

    for i, column in enumerate(dataframe.columns, 1):
        plt.subplot(rows, cols, i)
        # IQR
        Q1 = dataframe[column].quantile(0.25)
        Q3 = dataframe[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        sns.boxplot(dataframe[column], color="skyblue")
        plt.axhline(y=lower_bound, color="r", linestyle="--")
        plt.axhline(y=upper_bound, color="r", linestyle="--")
        plt.title(f"Boxplot of {column}", fontsize=15)
        plt.xlabel(column, fontsize=12)
        plt.ylabel("Frequency", fontsize=12)
    plt.tight_layout()
    plt.show()
