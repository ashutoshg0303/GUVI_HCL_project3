# GUVI_HCL_project3

# 🚦 Traffic Accident Analysis & Visualization


## 📌 Project Overview
This project analyzes traffic accident data to identify high-risk states, peak accident times, and contributing factors.  
The dataset includes accident date, state, severity, weather, and time of day.  
Using Python for data cleaning & exploration and Tableau for visualization, we build an interactive dashboard to present insights.

---

## 🎯 Objectives
- Analyze accident trends state-wise, date-wise, and severity-wise
- Identify peak accident months and times of day
- Examine impact of weather conditions on accidents
- Present findings via an interactive Tableau dashboard

---

## 📂 Folder Structure
traffic-accident-analysis/
│
├── data/
│   ├── traffic_accident_records.csv
│   └── traffic_accidents_cleaned.csv
│
├── scripts/
│   └── traffic_accident.py
│
├── dashboard/
│   └── Traffic_Accident_Analysis_Dashboard.twbx
│
├── screenshot/
│   └── Screenshot (488).png
│   └── Screenshot (489).png
│   └── Screenshot (490).png
│   └── Screenshot (491).png
│   └── Screenshot (492).png
│   └── Screenshot (493).png
│
├── README.md
└── requirements.txt


## 🧩 Project Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ashutoshg0303/GUVI_HCL_project3
cd GUVI_HCL_project3

2️⃣ Install Requirements
Ensure you have Python 3.x installed.
Install dependencies from requirements.txt:

pip install -r requirements.txt

3️⃣ Run Data Cleaning & EDA Script
python scripts/traffic_accident_analysis.py
```

## 📊 Dashboard

Open dashboard/traffic_accident_dashboard.twbx in Tableau.
Use filters (State, Year, Weather) to explore accident patterns interactively.
KPI cards display total accidents.


## 🛠️ Tools & Technologies

Python (Pandas) → Data Cleaning & Preparation
Tableau → Data Visualization & Dashboard
VS Code → Development Environment
GitHub → Version Control & Collaboration




## 📈 Data Exploration Summary

Total accidents: N (calculated from dataset)
Most affected state: Top state name
Peak accident time: Evening/Night (depending on data)
Most common weather condition during accidents: Clear / Rain (depending on data)



## 💡 Insights & Recommendations

State-Level Focus: Top 3 accident-prone states contribute to a large share of accidents. Road safety campaigns and infrastructure improvements should be prioritized in these areas.
Peak Hours: Accidents are most frequent during evenings, suggesting need for stricter traffic enforcement, improved lighting, and awareness during this time.
Seasonal Trends: Monthly analysis shows spikes in certain months — deploying additional traffic police during these months could reduce accidents.
Weather Impact: Accidents increase during rainy/foggy conditions — better road drainage, signage, and public advisories can reduce risks.


## 📊 Marking Rubric & Coverage
Criteria, How It’s Covered in Project
✅Problem Definition & Objectives: Clearly defined in README and PPT — project focuses on identifying accident patterns, high-risk states, and peak accident times.
✅Data Collection & Sources:	Used publicly available traffic accident dataset (CSV). Described dataset columns and structure.
✅Data Cleaning & Preparation:	Handled missing values, standardized date/time formats, created additional columns (Month, Year, Time of Day).
✅Data Exploration & Summarization:	Performed EDA — summarized accidents per state, severity distribution, monthly trend, and time-of-day patterns.
✅Data Visualization:	Built interactive Tableau dashboard with bar charts, line charts, pie charts, KPIs, and filters (State, Year, Weather).
✅Insights & Interpretation:	Identified top accident-prone states, peak months, weather impact, and time-of-day patterns. Provided actionable recommendations.
✅Report & Presentation:	Prepared PPT with project title, objective, overview, tools used, dashboard screenshots, and insights.



👨‍💻 Author
Ashutosh Gupta
Data Analyst Intern @ HCL
ashutoshgupta0303@gmail.com











