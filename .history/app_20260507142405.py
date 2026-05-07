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
# SIDEBAR MENU
# =========================================================

menu = st.sidebar.selectbox(
    "Select Dataset",
    [
        "Aggregated Transaction",
        "Aggregated User",
        "Aggregated Insurance",
        "Map User",
        "Map Map",
        "Map Insurance",
        "Top User",
        "Top Map",
        "Top Insurance"
    ]
)

# =========================================================
# AGGREGATED TRANSACTION
# =========================================================

if menu == "Aggregated Transaction":

    df = pd.read_sql(
        "SELECT * FROM aggregated_transaction",
        conn
    )

    st.header("Aggregated Transaction")

    col1, col2 = st.columns(2)

    col1.metric(
        "Total Transactions",
        int(df["transaction_count"].sum())
    )

    col2.metric(
        "Total Amount",
        f"₹ {df['transaction_amount'].sum():,.0f}"
    )

    top = (
        df.groupby("state")["transaction_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots()

    top.plot(
        kind="bar",
        ax=ax
    )

    st.pyplot(fig)

    st.dataframe(df)

# =========================================================
# AGGREGATED USER
# =========================================================

elif menu == "Aggregated User":

    df = pd.read_sql(
        "SELECT * FROM aggregated_user",
        conn
    )

    st.header("Aggregated User")

    col1, col2 = st.columns(2)

    col1.metric(
        "Registered Users",
        int(df["registered_users"].sum())
    )

    col2.metric(
        "App Opens",
        int(df["app_opens"].sum())
    )

    top = (
        df.groupby("brand")["registered_users"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots()

    top.plot(
        kind="bar",
        ax=ax
    )

    st.pyplot(fig)

    st.dataframe(df)

# =========================================================
# AGGREGATED INSURANCE
# =========================================================

elif menu == "Aggregated Insurance":

    df = pd.read_sql(
        "SELECT * FROM aggregated_insurance",
        conn
    )

    st.header("Aggregated Insurance")

    col1, col2 = st.columns(2)

    col1.metric(
        "Insurance Count",
        int(df["insurance_count"].sum())
    )

    col2.metric(
        "Insurance Amount",
        f"₹ {df['insurance_amount'].sum():,.0f}"
    )

    top = (
        df.groupby("state")["insurance_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots()

    top.plot(kind="bar", ax=ax)

    st.pyplot(fig)

    st.dataframe(df)

# =========================================================
# MAP USER
# =========================================================

elif menu == "Map User":

    df = pd.read_sql(
        "SELECT * FROM map_user",
        conn
    )

    st.header("Map User")

    top = (
        df.groupby("district")["registered_users"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots()

    top.plot(kind="bar", ax=ax)

    st.pyplot(fig)

    st.dataframe(df)

# =========================================================
# MAP MAP
# =========================================================

elif menu == "Map Map":

    df = pd.read_sql(
        "SELECT * FROM map_map",
        conn
    )

    st.header("Map Transaction")

    top = (
        df.groupby("district")["transaction_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots()

    top.plot(kind="bar", ax=ax)

    st.pyplot(fig)

    st.dataframe(df)

# =========================================================
# MAP INSURANCE
# =========================================================

elif menu == "Map Insurance":

    df = pd.read_sql(
        "SELECT * FROM map_insurance",
        conn
    )

    st.header("Map Insurance")

    top = (
        df.groupby("district")["insurance_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots()

    top.plot(kind="bar", ax=ax)

    st.pyplot(fig)

    st.dataframe(df)

# =========================================================
# TOP USER
# =========================================================

elif menu == "Top User":

    df = pd.read_sql(
        "SELECT * FROM top_user",
        conn
    )

    st.header("Top User")

    top = (
        df.groupby("pincode")["registered_users"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots()

    top.plot(kind="bar", ax=ax)

    st.pyplot(fig)

    st.dataframe(df)

# =========================================================
# TOP MAP
# =========================================================

elif menu == "Top Map":

    df = pd.read_sql(
        "SELECT * FROM top_map",
        conn
    )

    st.header("Top Transaction")

    top = (
        df.groupby("entity_name")["transaction_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots()

    top.plot(kind="bar", ax=ax)

    st.pyplot(fig)

    st.dataframe(df)

# =========================================================
# TOP INSURANCE
# =========================================================

elif menu == "Top Insurance":

    df = pd.read_sql(
        "SELECT * FROM top_insurance",
        conn
    )

    st.header("Top Insurance")

    top = (
        df.groupby("insurance_name")["insurance_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots()

    top.plot(kind="bar", ax=ax)

    st.pyplot(fig)

    st.dataframe(df)

# =========================================================
# CLOSE CONNECTION
# =========================================================

conn.close()