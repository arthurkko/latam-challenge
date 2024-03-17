import pandas as pd

def find_top10(df: pd.DataFrame, by: str, reset_index: bool = False, drop: bool = False) -> pd.DataFrame:
    
    """
    Find the top 10 values of a Dataframe.
    
    Parameters:
        df (pd.Dataframe): It's the input DataFrame containing the data you want to sort.
        by (str): It's a string that specifies the column by which you want to sort the values.
        reset_index (bool): Whether to reset the index of the resulting DataFrame. Default is False.
        drop (bool): If reset_index is True, drop the previous index. Default is False.
    
    Returns:
        pd.DataFrame: A DataFrame with the top 10 values sorted in descending order based on the specified column.
    """
    
    if reset_index == False:
        return df.sort_values(by=by, ascending=False).head(10)
    else:
        return df.sort_values(by=by, ascending=False).head(10).reset_index(drop=drop)