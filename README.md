# 🚀 TrendPulse: What's Actually Trending Right Now

## 📌 Project Overview

TrendPulse is a complete **data pipeline project** that collects, processes, analyzes, and visualizes trending stories from Hacker News.

The project is built in 4 stages:

```
Task 1 → Task 2 → Task 3 → Task 4
Collect → Clean → Analyze → Visualize
```

This project demonstrates practical skills in:

* API integration
* Data cleaning using Pandas
* Data analysis using Pandas & NumPy
* Data visualization using Matplotlib

---

## 🧱 Project Structure

```
trendpulse/
│
├── task1_data_collection.py
├── task2_data_processing.py
├── task3_analysis.py
├── task4_visualization.py
│
├── data/
│   ├── trends_YYYYMMDD.json
│   ├── trends_clean.csv
│   ├── trends_analysed.csv
│
├── outputs/
│   ├── chart1_top_stories.png
│   ├── chart2_categories.png
│   ├── chart3_scatter.png
│   ├── dashboard.png
```

---

## ⚙️ Task 1: Data Collection

* Fetched top 500 stories using Hacker News API
* Retrieved story details (title, score, comments, author)
* Categorized stories into:

  * Technology
  * World News
  * Sports
  * Science
  * Entertainment
* Stored up to 25 stories per category
* Saved output as JSON

📁 Output:

```
data/trends_YYYYMMDD.json
```

---

## 🧹 Task 2: Data Processing

* Loaded JSON into Pandas DataFrame
* Cleaned the data:

  * Removed duplicates
  * Dropped missing values
  * Converted data types
  * Filtered low-quality stories (score < 5)
  * Cleaned text (removed whitespace)
* Saved cleaned data as CSV

📁 Output:

```
data/trends_clean.csv
```

---

## 📊 Task 3: Data Analysis

* Performed analysis using Pandas and NumPy:

  * Mean, median, standard deviation of scores
  * Highest and lowest scoring stories
  * Most popular category
  * Most commented story
* Created new columns:

  * `engagement` → comments per upvote
  * `is_popular` → above average score
* Saved analyzed dataset

📁 Output:

```
data/trends_analysed.csv
```

---

## 📈 Task 4: Data Visualization

Created 3 charts using Matplotlib:

1. **Top 10 Stories by Score**

   * Horizontal bar chart

2. **Stories per Category**

   * Bar chart

3. **Score vs Comments**

   * Scatter plot with color differentiation

📊 Bonus:

* Combined all charts into a **dashboard**

📁 Output:

```
outputs/
├── chart1_top_stories.png
├── chart2_categories.png
├── chart3_scatter.png
├── dashboard.png
```

---

## 🛠️ Technologies Used

* Python
* Requests (API calls)
* Pandas (data processing)
* NumPy (analysis)
* Matplotlib (visualization)
* Git & GitHub (version control)

---

## 🚀 How to Run the Project

1. Clone the repository:

```
git clone https://github.com/<your-username>/trendpulse-<name>.git
cd trendpulse-<name>
```

2. Install dependencies:

```
pip install pandas numpy matplotlib requests
```

3. Run tasks in order:

```
python task1_data_collection.py
python task2_data_processing.py
python task3_analysis.py
python task4_visualization.py
```

---

## 🎯 Key Learnings

* Working with real-world APIs
* Handling missing and inconsistent data
* Performing statistical analysis
* Creating meaningful visualizations
* Building an end-to-end data pipeline

---

## 📌 Future Improvements

* Use parallel processing to speed up API calls
* Add more advanced visualizations (Seaborn/Plotly)
* Build a web dashboard (Streamlit)
* Automate daily data collection

---

## 👨‍💻 Author

Rakesh Bestha

---

## ⭐ Conclusion

TrendPulse is a complete hands-on project that showcases the ability to build a real-world data pipeline from data collection to visualization.

---
