import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="PhonePe Pulse Dashboard",
    layout="wide"
)

st.title("PhonePe Pulse Data Visualization Dashboard")

# =========================================================
# MYSQL CONNECTION
# =========================================================

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lokesh9090@",
    database="phonepe"
)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("Dashboard Filters")

dataset = st.sidebar.selectbox(
    "Select Dataset",
    (
        "Aggregated Transaction",
        "Aggregated User",
        "Aggregated Insurance",
        "Map User",
        "Map Map",
        "Map Insurance",
        "Top User",
        "Top Map",
        "Top Insurance"
    )
)

# =========================================================
# LOAD TABLES
# =========================================================

table_mapping = {
    "Aggregated Transaction": "aggregated_transaction",
    "Aggregated User": "aggregated_user",
    "Aggregated Insurance": "aggregated_insurance",
    "Map User": "map_user",
    "Map Map": "map_map",
    "Map Insurance": "map_insurance",
    "Top User": "top_user",
    "Top Map": "top_map",
    "Top Insurance": "top_insurance"
}

table_name = table_mapping[dataset]

df = pd.read_sql(
    f"SELECT * FROM {table_name}",
    conn
)

# =========================================================
# FILTERS
# =========================================================

if "state" in df.columns:

    state = st.sidebar.selectbox(
        "Select State",
        ["All"] + sorted(df["state"].unique().tolist())
    )

    if state != "All":
        df = df[df["state"] == state]

if "year" in df.columns:

    year = st.sidebar.selectbox(
        "Select Year",
        ["All"] + sorted(df["year"].unique().tolist())
    )

    if year != "All":
        df = df[df["year"] == year]

if "quarter" in df.columns:

    quarter = st.sidebar.selectbox(
        "Select Quarter",
        ["All"] + sorted(df["quarter"].unique().tolist())
    )

    if quarter != "All":
        df = df[df["quarter"] == quarter]

if "transaction_type" in df.columns:

    transaction = st.sidebar.selectbox(
        "Transaction Type",
        ["All"] + sorted(df["transaction_type"].unique().tolist())
    )

    if transaction != "All":
        df = df[df["transaction_type"] == transaction]

# =========================================================
# KPI SECTION
# =========================================================

st.subheader("Key Performance Indicators")

col1, col2, col3 = st.columns(3)

# TRANSACTION TABLES

if "transaction_amount" in df.columns:

    col1.metric(
        "Total Amount",
        f"₹ {df['transaction_amount'].sum():,.0f}"
    )

if "transaction_count" in df.columns:

    col2.metric(
        "Transaction Count",
        f"{df['transaction_count'].sum():,.0f}"
    )

# USER TABLES

if "registered_users" in df.columns:

    col3.metric(
        "Registered Users",
        f"{df['registered_users'].sum():,.0f}"
    )

# =========================================================
# BAR CHART
# =========================================================

st.subheader("Top 10 Analysis")

fig, ax = plt.subplots(figsize=(10,5))

# TRANSACTION AMOUNT

if "transaction_amount" in df.columns:

    top = (
        df.groupby("state")["transaction_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    top.plot(
        kind="bar",
        ax=ax
    )

    plt.ylabel("Amount")

# REGISTERED USERS

elif "registered_users" in df.columns:

    if "brand" in df.columns:

        top = (
            df.groupby("brand")["registered_users"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

    elif "district" in df.columns:

        top = (
            df.groupby("district")["registered_users"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

    else:

        top = (
            df.groupby("pincode")["registered_users"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

    top.plot(
        kind="bar",
        ax=ax
    )

    plt.ylabel("Users")

# INSURANCE

elif "insurance_amount" in df.columns:

    if "district" in df.columns:

        top = (
            df.groupby("district")["insurance_amount"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

    else:

        top = (
            df.groupby("state")["insurance_amount"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

    top.plot(
        kind="bar",
        ax=ax
    )

    plt.ylabel("Insurance Amount")

st.pyplot(fig)

# =========================================================
# LINE CHART
# =========================================================

if "year" in df.columns:

    st.subheader("Yearly Trend")

    fig2, ax2 = plt.subplots(figsize=(10,5))

    if "transaction_amount" in df.columns:

        yearly = (
            df.groupby("year")["transaction_amount"]
            .sum()
        )

    elif "insurance_amount" in df.columns:

        yearly = (
            df.groupby("year")["insurance_amount"]
            .sum()
        )

    elif "registered_users" in df.columns:

        yearly = (
            df.groupby("year")["registered_users"]
            .sum()
        )

    yearly.plot(
        marker="o",
        ax=ax2
    )

    st.pyplot(fig2)

# =========================================================
# DATAFRAME
# =========================================================

st.subheader("Dataset Preview")

st.dataframe(df)

# =========================================================
# CLOSE CONNECTION
# =========================================================

conn.close()