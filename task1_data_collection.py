import requests
import json
import time
import os
from datetime import datetime

# API URL to get top story IDs
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"

headers = {"User-Agent": "TrendPulse/1.0"}

#Fetch top story IDs
response = requests.get(TOP_STORIES_URL, headers=headers, timeout=5)

if response.status_code != 200:
    print("Failed to fetch top stories")
    exit()

story_ids = response.json()

top_story_ids = story_ids[:500]

categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

all_stories = []
all_fetched_stories = []

# Current timestamp
collected_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


print("Fetching stories...")

for story_id in top_story_ids:
    url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch story {story_id}")
        continue

    story = response.json()
    all_fetched_stories.append(story)

print(f"Fetched {len(all_fetched_stories)} stories")


for category in categories:
    category_count = 0
    print(f"Processing category: {category}")

    for story in all_fetched_stories:
        title = story.get("title", "")
        title_lower = title.lower()

        # Skip if no title
        if not title:
            continue

        keywords = categories[category]

        # Check keyword match
        if any(keyword in title_lower for keyword in keywords):
            story_data = {
                "post_id": story.get("id"),
                "title": title,
                "category": category,
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by", "unknown"),
                "collected_at": collected_time
            }

            all_stories.append(story_data)
            category_count += 1

       
        if category_count == 25:
            break

    time.sleep(2)

if not os.path.exists("data"):
    os.makedirs("data")

#Save JSON file
current_date = datetime.now().strftime("%Y%m%d")
filename = f"data/trends_{current_date}.json"

with open(filename, "w") as f:
    json.dump(all_stories, f, indent=4)

# Final output
print(f"Collected {len(all_stories)} stories. Saved to {filename}")


"""
Fetching stories...
Fetched 500 stories
Processing category: technology
Processing category: worldnews
Processing category: sports
Processing category: science
Processing category: entertainment
Collected 112 stories. Saved to data/trends_20260414.json
"""