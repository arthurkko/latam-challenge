from typing import List, Tuple
from datetime import datetime
import json
import pandas as pd
import sys

from utils.extract_json import extract_json
from utils.groupby_and_count import groupby_and_count
from utils.find_top10 import find_top10
from utils.df_to_list import df_to_list

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    
    # Get data from json file
    df_q1 = extract_json(file_path=file_path, col=["date", "user"])

    # Transform the values in the columns
    df_q1["date"] = df_q1['date'].dt.date
    df_q1["user"] = df_q1.apply(lambda x: x.user["username"], axis=1)

    # Most tweeted dates
    grouped_date = groupby_and_count(df_q1, ["date"])
    top_dates = find_top10(grouped_date, "user")
    del grouped_date

    # Users with most tweets in a date
    dates = top_dates.date.to_list()
    top_users = groupby_and_count(df_q1, ["date", "user"])                                      # Group and Count
    top_users = top_users.set_index("date").loc[dates].sort_values(by="size", ascending=False)  # Filter the relevant dates and sort the result
    top_users = top_users.reset_index().drop_duplicates(subset=["date"])                        # Drop the df by dates, this will leave us the user that most tweeted in each day
    del dates
    del df_q1

    # Answer
    top_dates_dict = top_dates.set_index("date").to_dict()
    df_q1_result = top_users.copy()
    df_q1_result["tweets"] = [top_dates_dict["user"][d] for d in top_users.date]
    df_q1_result = find_top10(df_q1_result, "tweets", reset_index=True, drop=True)
    del top_dates_dict
    del top_dates
    del top_users

    # Answer in a list
    q1_result = df_to_list(df_q1_result, ["date", "user"])
    del df_q1_result

    return q1_result

if __name__=="__main__":
    file_path = sys.argv[1]
    q1_time(file_path)