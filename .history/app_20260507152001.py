import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# PAGE CONFIG

st.set_page_config(
    page_title="PhonePe Pulse Dashboard",
    layout="wide"
)

st.title(" PhonePe Pulse Data Visualization Dashboard")

# MYSQL CONNECTION

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lokesh9090@",
    database="phonepe"
)

# SIDEBAR

st.sidebar.title("Dashboard Filters")

dataset = st.sidebar.selectbox(
    "Select Dataset",
    (
        "Aggregated Transaction",
        "Aggregated User",
        "Aggregated Insurance",
        "Map User",
        "Map Transaction",
        "Map Insurance",
        "Top User",
        "Top Transaction",
        "Top Insurance"
    )
)

# TABLE MAPPING

table_mapping = {
    "Aggregated Transaction": "aggregated_transaction",
    "Aggregated User": "aggregated_user",
    "Aggregated Insurance": "aggregated_insurance",
    "Map User": "map_user",
    "Map Transaction": "map_map",
    "Map Insurance": "map_insurance",
    "Top User": "top_user",
    "Top Transaction": "top_map",
    "Top Insurance": "top_insurance"
}

table_name = table_mapping[dataset]

# LOAD DATA

df = pd.read_sql(
    f"SELECT * FROM {table_name}",
    conn
)

# FILTERS

if "state" in df.columns:

    state = st.sidebar.selectbox(
        "Select State",
        ["All"] + sorted(df["state"].astype(str).unique().tolist())
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
        ["All"] + sorted(df["transaction_type"].astype(str).unique().tolist())
    )

    if transaction != "All":
        df = df[df["transaction_type"] == transaction]

# KPI SECTION

st.subheader(" Key Performance Indicators")

col1, col2, col3 = st.columns(3)

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

if "registered_users" in df.columns:

    col3.metric(
        "Registered Users",
        f"{df['registered_users'].sum():,.0f}"
    )

if "insurance_amount" in df.columns:

    col3.metric(
        "Insurance Amount",
        f"₹ {df['insurance_amount'].sum():,.0f}"
    )

# TOP 10 CHART

st.subheader(" Top 10 Analysis")

fig, ax = plt.subplots(figsize=(10,5))

try:

    # TRANSACTION TABLES

    if "transaction_amount" in df.columns:

        if "district" in df.columns:

            top = (
                df.groupby("district")["transaction_amount"]
                .sum()
                .sort_values(ascending=False)
                .head(10)
            )

        elif "entity_name" in df.columns:

            top = (
                df.groupby("entity_name")["transaction_amount"]
                .sum()
                .sort_values(ascending=False)
                .head(10)
            )

        else:

            top = (
                df.groupby("state")["transaction_amount"]
                .sum()
                .sort_values(ascending=False)
                .head(10)
            )

        ax.bar(top.index.astype(str), top.values)

        plt.xticks(rotation=45)

        plt.ylabel("Transaction Amount")

    # USER TABLES

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

        ax.bar(top.index.astype(str), top.values)

        plt.xticks(rotation=45)

        plt.ylabel("Registered Users")

    # INSURANCE TABLES

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

        ax.bar(top.index.astype(str), top.values)

        plt.xticks(rotation=45)

        plt.ylabel("Insurance Amount")

    st.pyplot(fig)

except Exception as e:

    st.error(f"Chart Error: {e}")

# YEARLY TREND

if "year" in df.columns:

    st.subheader("📈 Yearly Trend")

    fig2, ax2 = plt.subplots(figsize=(10,5))

    try:

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

        ax2.plot(
            yearly.index,
            yearly.values,
            marker="o"
        )

        plt.xticks(yearly.index)

        st.pyplot(fig2)

    except Exception as e:

        st.error(f"Trend Chart Error: {e}")

# DATAFRAME

st.subheader("📂 Dataset Preview")

st.dataframe(df)

# CLOSE CONNECTION

conn.close()