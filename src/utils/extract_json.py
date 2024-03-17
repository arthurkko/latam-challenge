import pandas as pd

def extract_json(file_path: str, col: list = None) -> pd.DataFrame:
    
    """
    Extract JSON data from a file into a DataFrame.
    
    Parameters:
        file_path (str): The path to the JSON file.
        col (list): A list of column names to extract from the JSON file. If None, all columns will be extracted.
    
    Returns:
        pd.DataFrame: A DataFrame containing the extracted JSON data.
    """

    if col is None:
        df = pd.read_json(file_path, lines=True)
    else:
        df = pd.read_json(file_path, lines=True)[col]

    return df