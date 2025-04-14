import kagglehub
import os
import pandas as pd


def load_data(dataset_path, file_name):
    """
    Loads the dataset into a Pandas DataFrame.
    Args:
        dataset_path (str): Path to the directory where the dataset is stored.
        file_name (str): The name of the dataset file (default is "diabetes.csv").
    Returns:
        pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        # Define the full path to the dataset file
        file_path = os.path.join(dataset_path, file_name)

        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found at path: {file_path}")
            # Load the dataset into a Pandas DataFrame
        df = pd.read_csv(file_path)
        print(f"Dataset loaded successfully. Shape: {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None
