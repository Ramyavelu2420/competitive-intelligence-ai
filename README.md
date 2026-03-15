# 🧠 MarketMind AI - Competitive Intelligence System

## 📋 Overview

MarketMind AI is a comprehensive competitive intelligence system that analyzes grocery product reviews, monitors pricing trends, and provides AI-powered strategic recommendations for e-commerce businesses.

## 🎯 Key Features

### 📊 Data Collection
- **Amazon Grocery Scraper**: Collects real product reviews and pricing data
- **Sentiment Analysis**: VADER-based sentiment scoring for customer reviews
- **Topic Detection**: Identifies customer complaints (packaging, price, quality, etc.)
- **Price Monitoring**: Tracks historical pricing trends and promotions

### 🤖 Intelligence Features
- **Real-time Dashboard**: Interactive Streamlit dashboard
- **Sentiment Analysis**: Positive/Neutral/Negative sentiment breakdown
- **Complaint Detection**: Automatic identification of customer issues
- **Price Trend Analysis**: Historical pricing with promotion detection
- **AI Recommendations**: Strategic business suggestions
- **Alert System**: Real-time market alerts

## 📁 Project Structure

```
datathon/
├── 🤖 amazon_grocery_pipeline.py    # Main data collection pipeline
├── 📊 dashboard.py                  # Interactive Streamlit dashboard
├── 🚀 run_dashboard.py             # Dashboard launcher
├── 📋 requirements.txt              # Python dependencies
├── 📚 README.md                    # This file
└── 📂 data/                       # Generated datasets
    ├── grocery_reviews_dataset.csv   # 500+ customer reviews
    ├── products.csv                # 100 grocery products
    └── pricing_history.csv        # 9,000+ price records
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Required NLTK Data (Optional)
```python
import nltk
nltk.download('vader_lexicon')
```

## 🚀 Quick Start

### 1. Generate Datasets
```bash
python amazon_grocery_pipeline.py
```
This will:
- Scrape Amazon grocery reviews
- Generate products and pricing data
- Create 3 CSV files in `data/` folder

### 2. Launch Dashboard
```bash
python run_dashboard.py
```
This will:
- Start Streamlit server on port 8501
- Open browser automatically
- Display interactive dashboard

## 📊 Dashboard Features

### 1️⃣ Overview Metrics
- Total Products: 100
- Total Reviews: 500+
- Average Rating: 4.1
- Negative Reviews: Real-time count

### 2️⃣ Sentiment Analysis
- **Pie Chart**: Positive/Neutral/Negative distribution
- **Bar Chart**: Top products by sentiment score
- **Insight**: "Customers overall positive sentiment iruku"

### 3️⃣ Complaint Analysis
- **Topics**: Packaging, Price, Quality, Delivery, Taste, Freshness
- **Frequency Chart**: Most common complaint types
- **Alert**: "Most complaints packaging related ah iruku"

### 4️⃣ Product Rating Analysis
- **Top 10**: Highest rated products
- **Bottom 10**: Lowest rated products
- **Insights**: Best/Worst product identification

### 5️⃣ Price Monitoring
- **Trend Charts**: 90-day price history
- **Multi-Product**: Compare multiple products
- **Current Prices**: Real-time price display

### 6️⃣ Promotion Detection
- **Analysis**: Promotion rate vs normal pricing
- **Impact**: Sales spike detection
- **ROI**: Promotion effectiveness

### 7️⃣ Sentiment vs Price Correlation
- **Scatter Plot**: Price-Sentiment relationship
- **Trend Line**: Correlation analysis
- **Business Insight**: Premium vs value perception

### 8️⃣ AI Strategic Recommendations
- **Packaging Issues**: Quality improvement suggestions
- **Price Optimization**: Promotion strategies
- **Marketing Insights**: Leverage positive sentiment
- **Priority Levels**: 🔴 High / 🟡 Medium / 🟢 Low

### 9️⃣ Alert System
- **Price Drops**: 10%+ decrease detection
- **Review Spikes**: Negative review surge
- **Promotion Opportunities**: Under-promoted products

## 📈 Data Sources

### Amazon Grocery Categories
- Snacks (chips, biscuits, namkeen)
- Rice (basmati, brown, white)
- Oil (cooking, olive, coconut)
- Spices (turmeric, chilli, garam masala)
- Tea (green, black, herbal)
- Coffee (instant, powder, beans)
- Packaged Foods (pasta, noodles, canned)
- Beverages (juice, energy drinks)
- Breakfast Cereals (corn flakes, oats, muesli)

### Major Brands Covered
- Nestle, Britannia, Tata, Aashirvaad
- Fortune, Maggi, Kellogg's, Amul
- Parle, ITC

## 🤖 AI Intelligence Features

### Sentiment Analysis
- **VADER Analyzer**: Compound sentiment scoring (-1 to +1)
- **Categorization**: Positive/Neutral/Negative
- **Confidence**: Real-time sentiment confidence

### Topic Detection
- **Keywords**: Quality, Price, Packaging, Taste, Delivery, Freshness
- **Multi-Topic**: Multiple topics per review
- **Frequency**: Topic importance ranking

### Price Intelligence
- **Historical**: 90-day price tracking
- **Promotions**: Automatic discount detection
- **Trends**: Price fluctuation analysis

### Strategic Recommendations
- **Automated**: AI-generated business suggestions
- **Priority-Based**: High/Medium/Low urgency
- **Actionable**: Specific implementation steps

## 🎯 Business Value

### Competitive Intelligence
- **Market Monitoring**: Real-time competitor tracking
- **Price Wars**: Automatic price drop detection
- **Customer Insights**: Sentiment and complaint analysis
- **Strategic Planning**: Data-driven decision making

### Operational Benefits
- **Quality Control**: Early issue detection
- **Customer Satisfaction**: Sentiment improvement tracking
- **Revenue Optimization**: Promotion effectiveness
- **Risk Management**: Alert system for problems

## 🔧 Technical Architecture

### Data Pipeline
1. **Scraping Layer**: Amazon product data extraction
2. **Processing Layer**: Sentiment and topic analysis
3. **Storage Layer**: CSV-based data storage
4. **Intelligence Layer**: AI-powered analysis
5. **Visualization Layer**: Interactive dashboard

### Technologies Used
- **Backend**: Python, Pandas, NLTK
- **Web Scraping**: Requests, BeautifulSoup4
- **Frontend**: Streamlit, Plotly
- **Data Analysis**: NumPy, Sentiment Analysis

## 📊 Sample Dashboard Views

### Overview Section
```
🏪 Total Products: 100
📝 Total Reviews: 500
⭐ Avg Rating: 4.1
😠 Negative Reviews: 82
```

### Sentiment Distribution
```
Positive Reviews – 60%
Neutral – 25%
Negative – 15%
```

### Complaint Topics
```
Packaging complaints – 35%
Delivery complaints – 20%
Price complaints – 15%
```

### AI Recommendations
```
🔴 High: Improve packaging quality
🟡 Medium: Optimize promotion strategy
🟢 Low: Leverage high-rated products
```

## 🚨 Alert Examples

### Price Drop Alert
```
🚨 Alert: 📉 Product X: Price dropped 10%+
```

### Review Spike Alert
```
🚨 Alert: 😠 Negative review spike: 15 complaints in 7 days
```

### Promotion Opportunity
```
🚨 Alert: 🏷️ Promotion opportunity: 5 products need promotions
```

## 🎓 Presentation Tips

### For Judges/Investors
> "Our system continuously analyzes product reviews and pricing data. It detects customer complaints, monitors price changes, and automatically generates strategic recommendations for sellers."

### Key Talking Points
1. **Real-time Intelligence**: Continuous market monitoring
2. **AI-Powered Insights**: Automated analysis and recommendations
3. **Competitive Advantage**: Price and sentiment tracking
4. **Business Impact**: Data-driven decision making
5. **Scalability**: Handles thousands of products

### Demo Flow
1. **Data Collection**: Show scraping pipeline
2. **Dashboard Tour**: Walk through all 9 sections
3. **AI Features**: Highlight recommendations and alerts
4. **Business Value**: Explain ROI and competitive advantage

## 🔮 Future Enhancements

### Advanced Features
- **Multi-Platform**: Expand beyond Amazon
- **Real-time API**: Live data integration
- **Machine Learning**: Predictive analytics
- **Mobile App**: On-the-go intelligence
- **Integration**: ERP/CRM system connectivity

### Data Sources
- **Social Media**: Twitter, Instagram sentiment
- **Review Sites**: Yelp, Google Reviews
- **Market Data**: Stock levels, sales data
- **Competitor APIs**: Direct competitor monitoring

## 📞 Support & Contact

### Technical Support
- **Documentation**: This README file
- **Code Comments**: Inline explanations
- **Error Handling**: Graceful degradation
- **Logging**: Detailed error messages

### Business Inquiries
- **MarketMind AI Team**: Competitive Intelligence Experts
- **Use Case**: E-commerce, Retail, Market Research
- **Industries**: Grocery, FMCG, Consumer Products

---

## 🎯 Conclusion

MarketMind AI transforms raw product data into actionable business intelligence. By combining sentiment analysis, price monitoring, and AI recommendations, it provides e-commerce businesses with the competitive edge needed to thrive in today's dynamic market.

**System automatically business suggestion kudukuthu!** 🧠✨
