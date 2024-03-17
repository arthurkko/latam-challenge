from typing import List
import pandas as pd

def groupby_and_count(df: pd.DataFrame, by: List[str]) -> pd.DataFrame:

    """
    Groups a pandas DataFrame by the specified columns.

    Parameters:
        df (pd.DataFrame): The pandas DataFrame to group.
        by (List[str]): A list of column names by which to group the DataFrame.

    Returns:
        pd.DataFrame: A new DataFrame with the data grouped by the specified columns.
    """

    if len(by)==1:
        grouped = df.groupby(by[0], as_index=False).count()
    else:
        grouped = df.groupby(by, as_index=False).size()

    return grouped