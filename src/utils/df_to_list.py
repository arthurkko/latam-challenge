from typing import List, Tuple
import pandas as pd

def df_to_list(df: pd.DataFrame, cols: List[str]) -> List[Tuple[str, int]]:

    """
    Converts selected columns from a pandas DataFrame into a list of tuples.

    Parameters:
        df (pd.DataFrame): The pandas DataFrame containing the data.
        cols (List): A list of column names from the DataFrame to include in the conversion.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple contains values from the selected columns.
                               The first element of the tuple is a string representing the column name,
                               and the second element is an integer representing the corresponding value.
    """

    col1 = cols[0]
    col2 = cols[1]

    resp = [(df[col1].iloc[i] ,df[col2].iloc[i]) for i in range(10)]

    return resp