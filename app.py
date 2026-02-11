import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Dashboard", layout="wide")

st.title("Excel Dashboard")

# Load Excel
@st.cache_data
def load_data():
    df = pd.read_excel("Vipul Excel.xlsx")
    return df

df = load_data()

# Show raw data
with st.expander("View Raw Data"):
    st.dataframe(df)

# Sidebar Filters
st.sidebar.header("Filters")

# Example filter (change column name)
if "Category" in df.columns:
    category = st.sidebar.multiselect(
        "Select Category",
        df["Category"].unique(),
        default=df["Category"].unique()
    )
    df = df[df["Category"].isin(category)]

# KPIs
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

if "Amount" in df.columns:
    col1.metric("Total Amount", f"{df['Amount'].sum():,.2f}")

if "Quantity" in df.columns:
    col2.metric("Total Quantity", df["Quantity"].sum())

col3.metric("Rows", len(df))

# Charts
st.subheader("Charts")

if "Category" in df.columns and "Amount" in df.columns:
    fig = px.bar(df, x="Category", y="Amount", title="Amount by Category")
    st.plotly_chart(fig, use_container_width=True)

if "Date" in df.columns and "Amount" in df.columns:
    fig2 = px.line(df, x="Date", y="Amount", title="Trend Over Time")
    st.plotly_chart(fig2, use_container_width=True)
