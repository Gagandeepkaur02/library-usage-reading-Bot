import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Library Usage & Reading Habit Bot", layout="wide")

st.title("📚 Library Usage & Reading Habit Bot")
st.write(
    "This bot analyzes student library usage and reading habits using structured data "
    "and provides meaningful insights through classification and visualizations."
)

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    return pd.read_csv("library_data.csv")

data = load_data()

st.subheader("📄 Student Library Data")
st.dataframe(data)

# ---------------- READING HABIT LOGIC ----------------
def reading_level(books, hours):
    if books >= 7 and hours >= 15:
        return "Active Reader"
    elif books >= 3 and hours >= 6:
        return "Moderate Reader"
    else:
        return "Low Reader"

data["Reading_Level"] = data.apply(
    lambda x: reading_level(x["Books_Borrowed"], x["Reading_Hours"]),
    axis=1
)

# ---------------- FILTER SECTION ----------------
st.subheader("🔍 Filter Data")

col1, col2 = st.columns(2)

with col1:
    grade_filter = st.multiselect(
        "Select Grade(s):",
        options=sorted(data["Grade"].unique()),
        default=sorted(data["Grade"].unique())
    )

with col2:
    genre_filter = st.multiselect(
        "Select Genre(s):",
        options=data["Genre"].unique(),
        default=data["Genre"].unique()
    )

filtered_data = data[
    (data["Grade"].isin(grade_filter)) &
    (data["Genre"].isin(genre_filter))
]

st.subheader("📊 Filtered Data with Reading Levels")
st.dataframe(filtered_data)

# ---------------- VISUALIZATION 1: MONTHLY BORROWING ----------------
st.subheader("📈 Monthly Borrowing Trend")

monthly_trend = (
    filtered_data.groupby("Month")["Books_Borrowed"]
    .sum()
    .reindex(["January", "February", "March", "April", "May", "June"])
)

plt.figure()
monthly_trend.plot(kind="line", marker="o")
plt.xlabel("Month")
plt.ylabel("Books Borrowed")
plt.title("Monthly Library Usage")
st.pyplot(plt)

# ---------------- VISUALIZATION 2: GENRE POPULARITY ----------------
st.subheader("📚 Genre Popularity")

genre_popularity = filtered_data["Genre"].value_counts()

plt.figure()
genre_popularity.plot(kind="bar")
plt.xlabel("Genre")
plt.ylabel("Number of Students")
plt.title("Genre Preference Distribution")
st.pyplot(plt)

# ---------------- VISUALIZATION 3: READING LEVEL DISTRIBUTION ----------------
st.subheader("🎯 Reading Habit Classification")

level_dist = filtered_data["Reading_Level"].value_counts()

plt.figure()
level_dist.plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.ylabel("")
plt.title("Reading Habit Levels")
st.pyplot(plt)

# ---------------- INSIGHTS ----------------
st.subheader("🧠 Key Insights")

st.write("• Active Readers demonstrate consistent library engagement.")
st.write("• Genre popularity helps librarians plan book procurement.")
st.write("• Monthly trends assist in evaluating reading initiatives.")
st.write("• Low Readers can be supported through targeted reading programs.")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("📘 Prototype Bot | Dummy data generated using Python | Streamlit Dashboard")
