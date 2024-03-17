from typing import List, Dict
import pandas as pd

def dict_to_df(dict: Dict, col: List[str]) -> pd.DataFrame:

    """
    Converts a dictionary into a pandas DataFrame.

    Parameters:
        dict (Dict): The dictionary containing the data.
        col (List[str]): A list of column name to include in the DataFrame.

    Returns:
        pd.DataFrame: A pandas DataFrame created from the dictionary data,
                      with the specified column.
    """

    df = pd.DataFrame.from_dict(dict, orient="index", columns=col)

    return df