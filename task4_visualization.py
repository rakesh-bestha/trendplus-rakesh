import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/trends_analysed.csv")

if not os.path.exists("outputs"):
    os.makedirs("outputs")

#Chart-1
top_10 = df.sort_values(by="score",ascending=False).head(10)
top_10["short_title"] = top_10["title"].str[:50]
plt.figure()
plt.barh(top_10["short_title"], top_10["score"])
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.savefig("outputs/chart1_top_stories.png")
plt.show()

#Chart-2

category_counts = df["category"].value_counts()
plt.figure()
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")
plt.savefig("outputs/chart2_categories.png")
plt.show()

#chart-3

popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.figure()
plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
plt.xlabel("Score")
plt.ylabel("Comments")
plt.title("Score vs Comments")
plt.legend()
plt.savefig("outputs/chart3_scatter.png")
plt.show()

#Dashboard

fig, axes = plt.subplots(1,3, figsize=(18,5))

axes[0].barh(top_10["short_title"], top_10["score"])
axes[0].set_title("Top Stories")

axes[1].bar(category_counts.index, category_counts.values)
axes[1].set_title("Categories")

axes[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axes[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axes[2].set_title("Score vs Comments")
axes[2].legend()

plt.suptitle("TrendPlus Dashboard")
plt.savefig("outputs/dashboard.png")
plt.show()
