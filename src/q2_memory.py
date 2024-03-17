from typing import List, Tuple
import pandas as pd
import sys
import emoji

from utils.extract_json import extract_json
from utils.find_top10 import find_top10
from utils.df_to_list import df_to_list

from memory_profiler import profile

@profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]:

    # Extract data
    df_q2 = extract_json(file_path=file_path, col=["content"])

    # Make a list of emojis
    emoji_list = [emoji.distinct_emoji_list(content) for content in df_q2.content if emoji.emoji_count(content)>0]
    del df_q2

    # Dict: {emoji_str: count, ...}
    emoji_dict = {}
    for emojis in emoji_list:
        for emj in emojis:
            if emj in emoji_dict:
                emoji_dict[emj] += 1
            else:
                emoji_dict[emj] = 1
    del emoji_list
    
    # Dict -> Dataframe
    df_emoji = pd.DataFrame.from_dict(emoji_dict, orient="index", columns=["count"])
    del emoji_dict

    # Top 10 in dataframe form
    df_q2_result = find_top10(df=df_emoji, by="count", reset_index=True)

    # Top 10 List
    q2_result = df_to_list(df=df_q2_result, cols=["index", "count"])
    del df_q2_result

    return q2_result

if __name__=="__main__":
    file_path = sys.argv[1]
    q2_memory(file_path)