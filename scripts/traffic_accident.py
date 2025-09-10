import pandas as pd

# 1️⃣ Load Dataset
df = pd.read_csv("traffic_accident_records.csv")

print("🔍 Original Dataset Shape:", df.shape)
print("🔍 Columns:", df.columns.tolist())

# 2️⃣ Handle Missing Values
df = df.dropna(subset=["State", "Date", "Weather"])  # Drop rows missing key info
print("✅ Removed rows with missing State, Date, or Weather")

# 3️⃣ Standardize Columns
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Hour"] = pd.to_datetime(df["Time"], format="%H:%M", errors="coerce").dt.hour

# 4️⃣ Feature Engineering
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day

# Function to categorize time of day
def time_of_day(hour):
    if pd.isna(hour):
        return "Unknown"
    elif 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 21:
        return "Evening"
    else:
        return "Night"

df["Time_of_Day"] = df["Hour"].apply(time_of_day)

# Clean state names
df["State"] = df["State"].str.title()

# 5️⃣ Exploratory Data Analysis (EDA)

print("\n📊 ----- EDA Summary -----")
# Total number of accidents
print("Total Accidents:", len(df))

# Accidents per state
print("\nAccidents per State:")
print(df["State"].value_counts())

# Accidents by severity
if "Severity" in df.columns:
    print("\nAccidents by Severity:")
    print(df["Severity"].value_counts())

# Accidents per Time of Day
print("\nAccidents by Time of Day:")
print(df["Time_of_Day"].value_counts())

# Monthly Accident Trend
monthly_trend = df.groupby("Month")["State"].count()
print("\nMonthly Accident Trend:")
print(monthly_trend)

# 6️⃣ Save Cleaned Dataset
df.to_csv("traffic_accidents_cleaned.csv", index=False)
print("\n✅ Data Cleaning + EDA Completed. Cleaned dataset saved as 'traffic_accidents_cleaned.csv'")
