import pandas as pd
import numpy as np

df_data = pd.read_json("data/trends_20260414.json")

print(f"Loaded {len(df_data)} stories from {'data/trends_YYYYMMDD.json'}")

df_data.info()

df_data = df_data.drop_duplicates("post_id")
print(f"After removing duplicates: {len(df_data)}")

df_data = df_data.dropna(subset=["post_id", "title", "score"])
print(f"After removing missing values: {len(df_data)}")

df_data[["score", "num_comments"]] = df_data[["score", "num_comments"]].astype(int)

df_data = df_data[df_data["score"] >= 5].dropna()
print(f"After removing low scores: {len(df_data)}")
                           
df_data["title"] = df_data["title"].str.strip()

#Save as CSV
df_data.to_csv("data/trends_clean.csv", index=False)
print(f"Saved {len(df_data)} rows to data/trends_clean.csv")

#Summary
print(df_data["category"].value_counts())


