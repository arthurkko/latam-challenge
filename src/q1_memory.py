from typing import List, Tuple
from datetime import datetime
import json
import pandas as pd
import datetime
import sys
from memory_profiler import profile

@profile
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:

    # Get data from json file
    with open(file_path, 'r') as file:
        data_list = []
        for line in file:
            object_json = json.loads(line)
            data_list.append(object_json)
    del object_json

    # Transform it in a dataframe
    df_q1 = pd.DataFrame(data_list)[["date", "user"]]
    del data_list

    # Transform the values in the columns
    df_q1["date"] = df_q1.apply(lambda x: datetime.datetime.strptime(x.date, "%Y-%m-%dT%H:%M:%S%z").date(), axis=1)
    df_q1["user"] = df_q1.apply(lambda x: x.user["username"], axis=1)

    # Most tweeted dates
    top_dates = df_q1.groupby("date", as_index=False).count().sort_values(by=["user"], ascending=False).head(10)

    # Users with most tweets in a date
    dates = top_dates.date.to_list()
    top_users = df_q1.groupby(["date", "user"], as_index=False).size().set_index("date").loc[dates].sort_values(by="size", ascending=False).reset_index().drop_duplicates(subset=["date"])
    del dates
    del df_q1

    # Answer
    top_dates_dict = top_dates.set_index("date").to_dict()
    q1_result_df = top_users.copy()
    q1_result_df["tweets"] = [top_dates_dict["user"][d] for d in top_users.date]
    q1_result_df = q1_result_df.sort_values(by="tweets", ascending=False).reset_index(drop=True)
    del top_dates_dict
    del top_dates
    del top_users

    # Answer in a list
    date = q1_result_df["date"]
    user = q1_result_df["user"]
    q1_result = [(date.iloc[i], user.iloc[i]) for i in range(10)]
    del date
    del user

    return q1_result

if __name__=="__main__":
    file_path = sys.argv[1]
    q1_memory(file_path)