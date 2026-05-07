import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns

# Page Config
st.set_page_config(
    page_title="PhonePe Transaction Insights",
    layout="wide"
)

# Title
st.title(" PhonePe Transaction Insights Dashboard")

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lokesh9090@",
    database="phonepe"
)

# Load Data
query = "SELECT * FROM aggregated_transaction"
df = pd.read_sql(query, conn)

# Sidebar Filters
st.sidebar.header("Filters")

state = st.sidebar.selectbox(
    "Select State",
    ["All"] + list(df['state'].unique())
)

year = st.sidebar.selectbox(
    "Select Year",
    ["All"] + sorted(df['year'].unique().tolist())
)

transaction_type = st.sidebar.selectbox(
    "Transaction Type",
    ["All"] + list(df['transaction_type'].unique())
)

# Apply Filters
filtered_df = df.copy()

if state != "All":
    filtered_df = filtered_df[
        filtered_df['state'] == state
    ]

if year != "All":
    filtered_df = filtered_df[
        filtered_df['year'] == year
    ]

if transaction_type != "All":
    filtered_df = filtered_df[
        filtered_df['transaction_type'] == transaction_type
    ]

# KPIs
st.subheader(" Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Transactions",
    int(filtered_df['transaction_count'].sum())
)

col2.metric(
    "Total Amount",
    f"{filtered_df['transaction_amount'].sum():,.0f}"
)

col3.metric(
    "States",
    filtered_df['state'].nunique()
)

# Top States Chart

st.subheader(" Top States by Transaction Amount")

top_states = (
    filtered_df.groupby('state')['transaction_amount']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig, ax = plt.subplots()

top_states.plot(
    kind='bar',
    ax=ax
)

plt.xticks(rotation=45)

st.pyplot(fig)

# Transaction Type Distribution

st.subheader("💳 Transaction Type Distribution")

type_data = (
    filtered_df.groupby('transaction_type')['transaction_count']
    .sum()
)

fig2, ax2 = plt.subplots()

type_data.plot(
    kind='pie',
    autopct='%1.1f%%',
    ax=ax2
)

st.pyplot(fig2)

# Yearly Trend

st.subheader(" Yearly Transaction Trend")

year_data = (
    filtered_df.groupby('year')['transaction_amount']
    .sum()
)

fig3, ax3 = plt.subplots()

year_data.plot(
    marker='o',
    ax=ax3
)

st.pyplot(fig3)


# Raw Data

st.subheader(" Dataset Preview")

st.dataframe(filtered_df)

# Close Connection
conn.close()