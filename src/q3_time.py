from typing import List, Tuple
import pandas as pd
import sys

from utils.extract_json import extract_json
from utils.find_top10 import find_top10
from utils.df_to_list import df_to_list
from utils.dict_to_df import dict_to_df

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    
    df_q3 = extract_json(file_path=file_path, col=["mentionedUsers"])

    user_list = df_q3.mentionedUsers.tolist()
    del df_q3

    user_dict = {}
    for users in user_list:
        for user in users:
            username = user["username"]
            if username in user_dict:
                user_dict[username] += 1
            else:
                user_dict[username] = 1
    del user_list
    del users
    del user
    del username
    
    df_user = dict_to_df(user_dict, ["count"])
    del user_dict

    df_q3_result = find_top10(df_user, "count", True)
    del df_user

    q3_result = df_to_list(df_q3_result, ["index", "count"])
    del df_q3_result

    return q3_result


if __name__=="__main__":
    file_path = sys.argv[1]
    q3_time(file_path)