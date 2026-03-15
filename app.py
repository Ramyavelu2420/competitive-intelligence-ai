import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(
    page_title="MarketMind AI",
    layout="wide"
)

st.title("🧠 MarketMind AI - Competitive Intelligence System")
st.set_page_config(page_title="MarketMind AI", layout="wide")

st.markdown("AI powered monitoring of pricing trends, customer sentiment and competitor strategies.")

# -----------------------------
# LOAD DATA
# -----------------------------

@st.cache_data
def load_data():

    reviews = pd.read_csv("data/reviews.csv")
    products = pd.read_csv("data/products.csv")
    pricing = pd.read_csv("data/pricing_history.csv")

    reviews["review_date"] = pd.to_datetime(reviews["review_date"])
    pricing["date"] = pd.to_datetime(pricing["date"])

    return reviews, products, pricing


reviews, products, pricing = load_data()


# -----------------------------
# SIDEBAR
# -----------------------------

page = st.sidebar.selectbox(
    "Navigation",
    [
        "Dashboard",
        "Sentiment Analysis",
        "Complaint Analysis",
        "Product Rating",
        "Price Monitoring",
        "Cross Signal Intelligence",
        "AI Strategy"
    ]
)

st.sidebar.header("📊 Dataset Summary")

st.sidebar.write(f"Products: {len(products)}")
st.sidebar.write(f"Reviews: {len(reviews)}")
st.sidebar.write(f"Price Records: {len(pricing)}")

# -----------------------------
# DASHBOARD
# -----------------------------

if page == "Dashboard":

    st.header("📊 Market Overview")

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("Products", len(products))
    col2.metric("Reviews", len(reviews))
    col3.metric("Avg Rating", round(products["rating"].mean(),2))
    col4.metric("Avg Price", round(products["current_price"].mean(),2))

    
    st.markdown("---")

    st.subheader("Products by Category")

    fig = px.bar(
        products["category"].value_counts(),
        title="Category Distribution"
    )

    st.plotly_chart(fig,use_container_width=True)
    
    col1,col2 = st.columns(2)

# -----------------------------
# SENTIMENT ANALYSIS
# -----------------------------

if page == "Sentiment Analysis":

    st.header("📊 Sentiment Analysis")

    reviews["sentiment_category"] = pd.cut(
        reviews["sentiment_score"],
        bins=[-1,-0.1,0.1,1],
        labels=["Negative","Neutral","Positive"]
    )

    sentiment = reviews["sentiment_category"].value_counts()

    fig = px.pie(
        sentiment,
        values=sentiment.values,
        names=sentiment.index,
        title="Customer Sentiment"
    )

    st.plotly_chart(fig,use_container_width=True)

    st.subheader("Top Positive Products")

    top = reviews.groupby("product_id")["sentiment_score"].mean().sort_values(ascending=False).head(10)

    fig2 = px.bar(top)

    st.plotly_chart(fig2,use_container_width=True)



# -----------------------------
# COMPLAINT ANALYSIS
# -----------------------------

if page == "Complaint Analysis":

    st.header(" Complaint Topic Analysis")

    complaints = reviews[reviews["sentiment_score"] < -0.1]
    total_complaints = len(complaints)

    col1,col2 = st.columns(2)

    col1.metric("Total Complaints", total_complaints)
    col2.metric("Complaint Rate (%)", round((total_complaints/len(reviews))*100,2))
    

    topic_list = []

    for t in complaints["topics"].dropna():
        topic_list += t.split(",")

    topics = pd.Series(topic_list).value_counts()

    fig = px.bar(
        topics.head(10),
        title="Top Complaint Topics"
    )

    st.plotly_chart(fig,use_container_width=True)

    
# -----------------------------
# PRICE MONITORING
# -----------------------------

if page == "Price Monitoring":

    st.header("💰 Price Monitoring")

    products["product_name"] = (
        products["brand"] + " " +
        products["model"] + " " +
        products["variant"]
    )

    st.subheader("Select products to monitor prices:")

    selected_product = st.selectbox(
        "Choose Product",
        products["product_name"]
    )

    product_id = products[
        products["product_name"] == selected_product
    ]["product_id"].values[0]

    data = pricing[
        pricing["product_id"] == product_id
    ]

    st.subheader("📈 Product Price Trend Chart for Selected Product")

    fig = px.line(
        data,
        x="date",
        y="price",
        color="platform",
        title=f"Price Trend - {selected_product}"
    )

    st.plotly_chart(fig,use_container_width=True)

   
    
    
# -----------------------------
# PRODUCT RATING
# -----------------------------

if page == "Product Rating":

    st.header("⭐ Product Rating Analysis")

    best_product = products.loc[products["rating"].idxmax()]
    worst_product = products.loc[products["rating"].idxmin()]

    col1,col2 = st.columns(2)

    with col1:
        st.success(f"""
        Best Rated Product

        {best_product['brand']} {best_product['model']}

        Rating: {best_product['rating']}
        """)

    with col2:
        st.error(f"""
        Worst Rated Product

        {worst_product['brand']} {worst_product['model']}

        Rating: {worst_product['rating']}
        """)

    st.subheader("📊 Rating Statistics")

    col1,col2,col3 = st.columns(3)

    col1.metric("Average Rating", round(products["rating"].mean(),2))
    col2.metric("Median Rating", round(products["rating"].median(),2))
    col3.metric("Total Reviews", int(products["review_count"].sum()))

    st.subheader("Product Rating Distribution")

    fig = px.histogram(
        products,
        x="rating",
        nbins=10,
        title="Rating Distribution"
    )

    st.plotly_chart(fig,use_container_width=True)


# -----------------------------
# CROSS SIGNAL INTELLIGENCE
# -----------------------------

if page == "Cross Signal Intelligence":

    st.header("🧠 Market Signal Detection")

    complaints = reviews[reviews["sentiment_score"] < -0.1]

    complaint_rate = len(complaints)/len(reviews)

    price_change = pricing.groupby("product_id")["price"].apply(
        lambda x: (x.iloc[-1]-x.iloc[0])/x.iloc[0]
    )

    avg_price_drop = price_change.mean()

    col1,col2 = st.columns(2)

    col1.metric("Complaint Rate", round(complaint_rate*100,2))
    col2.metric("Avg Price Change", round(avg_price_drop*100,2))

    if complaint_rate > 0.2 and avg_price_drop < -0.1:

        st.error("⚠ Market Opportunity Detected")

        st.write(
        """
        High complaints detected while prices dropping.

        Competitors may capture dissatisfied customers.
        """
        )

    else:

        st.success("Market stable")



# -----------------------------
# AI STRATEGY ENGINE
# -----------------------------

if page == "AI Strategy":

    st.header("🤖 AI Strategic Recommendations")

    strategies = []

    # packaging complaints
    packaging = reviews[reviews["topics"].str.contains("packaging",na=False)]

    if len(packaging) > 10:

        strategies.append(
            {
                "Issue":"Packaging Complaints",
                "Strategy":"Improve packaging material and supplier quality"
            }
        )

    # price war
    price_var = pricing.groupby("product_id")["price"].std().mean()

    if price_var > 20:

        strategies.append(
            {
                "Issue":"Price War Detected",
                "Strategy":"Introduce promotions and bundle offers"
            }
        )

    # rating drop
    low_rating = products[products["rating"] < 3.5]

    if len(low_rating) > 0:

        strategies.append(
            {
                "Issue":"Low Rated Products",
                "Strategy":"Improve product quality or reposition brand"
            }
        )

    for s in strategies:

        st.info(
            f"""
Issue: {s['Issue']}

Recommended Action:
{s['Strategy']}
"""
        )

