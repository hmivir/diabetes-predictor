import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt


def correlation_matrix(data):
    """
    Plots the correlation matrix of a dataset."""
    # Calculate the correlation matrix
    correlation_matrix = data.corr()

    # Create a heatmap to visualize the correlation matrix
    plt.figure(figsize=(8, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Matrix")
    plt.show()
