import pandas as pd
import numpy as np

df_clean = pd.read_csv("data/trends_clean.csv")

#Load and Explore
print(f"Loaded data: {df_clean.shape}")
print(f"First 5 rows:\n {df_clean.head(5)}")
print(f"Average Score: {df_clean['score'].mean()}")
print(f"Average Comments: {df_clean['num_comments'].mean()}")

#Basic Analysis with NumPy
scores = df_clean["score"].values


score_mean = np.mean(scores)
score_median = np.median(scores)
score_std = np.std(scores)
score_max = np.max(scores)
score_min = np.min(scores)
top_category = df_clean["category"].value_counts().idxmax()
max_comments = df_clean["num_comments"].max()
top_story = df_clean[df_clean["num_comments"] == max_comments]
title = top_story["title"].iloc[0]
#top_title = df_clean.loc[top_comments, "title"]
df_clean["engagement"] = df_clean["num_comments"] / (df_clean["score"] + 1)
df_clean["is_popular"] = df_clean["score"] > score_mean

df_clean.to_csv("data/trends_analysed.csv", index=False)

print("----NumPy Stats----")
print(f"Mean Score: {score_mean}")
print(f"Median Score: {score_median}")
print(f"Std Score: {score_std}")
print(f"Max Score: {score_max}")
print(f"Min Score: {score_min}")

print(f"Most Stories in {top_category} ({len(top_category)})")

print("Saved to data/trends_analysed.csv")

"""
Loaded data: (91, 7)
First 5 rows:
     post_id  ...         collected_at
0  47768195  ...  2026-04-14 23:44:22
1  47768133  ...  2026-04-14 23:44:22
2  47767676  ...  2026-04-14 23:44:22
3  47766370  ...  2026-04-14 23:44:22
4  47767606  ...  2026-04-14 23:44:22

[5 rows x 7 columns]
Average Score: 147.43956043956044
Average Comments: 71.73626373626374
----NumPy Stats----
Mean Score: 147.43956043956044
Median Score: 65.0
Std Score: 208.29444547896424
Max Score: 1398
Min Score: 5
Most Stories in technology (10)
Saved to data/trends_analysed.csv
"""