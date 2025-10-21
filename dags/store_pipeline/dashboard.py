import duckdb
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="E-Commerce Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🛒 E-Commerce Data Dashboard")
st.markdown("Data powered Airflow + dbt pipeline")

conn = duckdb.connect("/root/airflow/dags/store_pipeline/dev.duckdb", read_only=True)

df_sales = conn.execute("SELECT * FROM fact_sales").df()
df_products = conn.execute("SELECT product_id, product_title FROM products_dim").df()
df_merged = pd.merge(df_sales, df_products, on="product_id", how="left")

total_sales = df_merged["total_amount"].sum()
total_orders = df_merged["cart_id"].nunique()
unique_customers = df_merged["user_id"].nunique()

col1, col2, col3 = st.columns(3)
col1.metric(" Total Sales", f"${total_sales:,.2f}")
col2.metric(" Total Orders", f"{total_orders:,}")
col3.metric(" Unique Customers", f"{unique_customers:,}")

st.markdown("---")

st.header("Sales Analysis by Category")
sales_by_category = (
    df_merged.groupby("product_category", as_index=False)["total_amount"].sum()
)
fig1 = px.bar(
    sales_by_category,
    x="product_category",
    y="total_amount",
    color="product_category",
    title="Sales by Product Category",
    labels={"product_category": "Product Category", "total_amount": "Total Sales"},
)
st.plotly_chart(fig1, use_container_width=True)

st.header("Revenue Over Time")
df_merged["month"] = pd.to_datetime(df_merged["cart_date"]).dt.to_period("M").astype(str)
monthly_revenue = df_merged.groupby("month", as_index=False)["total_amount"].sum()

fig2 = px.line(
    monthly_revenue,
    x="month",
    y="total_amount",
    title="Monthly Revenue Trend",
    markers=True,
    labels={"month": "Month", "total_amount": "Total Revenue"},
)
st.plotly_chart(fig2, use_container_width=True)

st.header("Top Performing Products")
top_products = (
    df_merged.groupby("product_title", as_index=False)["total_amount"]
    .sum()
    .nlargest(10, "total_amount")
    .sort_values("total_amount", ascending=True)
)
fig3 = px.bar(
    top_products,
    y="product_title",
    x="total_amount",
    orientation='h',
    title="Top 10 Products by Sales",
    labels={"product_title": "Product", "total_amount": "Total Sales"},
)
st.plotly_chart(fig3, use_container_width=True)

conn.close()
