#  Restaurant Success Prediction

##  Project Overview

This project aims to analyze restaurant data and predict restaurant success based on various factors such as cost, reviews, services, and location.By combining Zomato web-scraped data with geographic insights from OpenStreetMap (OSM), it identifies key success factors like price-to-rating relationships and competition density.The dataset is built by integrating multiple data sources and performing Exploratory Data Analysis (EDA) and Feature Engineering to prepare it for machine learning.
# Problem Statement
The goal is to understand what makes a restaurant successful and build a model to predict restaurant ratings based on various features.

# Success Metric
Restaurant success is defined using:
Rating (Regression Problem)
Continuous target variable
Higher rating → More successful restaurant
Lower rating → Less successful restaurant

##  Key Features
* Extracts restaurant details (Price, Rating, Cuisine) from Zomato
* Enriches data with GPS coordinates and competition density using Overpass API (OSM)
* Merges datasets using Fuzzy String Matching to handle naming variations
* Visualizes market trends to identify success factors

##  Data Collection
###  Zomato Web Scraping
Restaurant data was collected using web scraping techniques.
**Extracted Features:**
* Name
* Cuisine
* Price
* Rating
* City & Area
* Average Cost for Two
* Online Delivery availability
* Table Booking
* Restaurant link

**Tools Used:**
* BeautifulSoup
* Requests

**Logic:**
* Iterates through multiple cities (Bangalore, Mumbai, etc.)
* Targets high-traffic restaurant areas

**Feature Engineering:**
* Created `hasOnlineDelivery` and `hasTableBooking`
* Extracted using text parsing and JSON-LD scripts

###   OpenStreetMap (OSM) Data
**Tools Used:**
* Overpass API
* BallTree (Scikit-Learn)

**Spatial Features:**
* Latitude
* Longitude

**Competition Density:**
* Calculated using Haversine distance
* Counts number of restaurants within a 1 km radius

###  Data Merging (Fuzzy Matching)
**Challenge:**
Zomato and OSM datasets often have naming differences
(e.g., *"McDonald's"* vs *"McDonald's India"*).

**Solution:**
* Used RapidFuzz (token sort ratio = 85%)
* Matched similar restaurant names across datasets

##  Exploratory Data Analysis (EDA)

###  Univariate Analysis
* Distribution of Ratings
* Price Distribution
* Top Cuisines
* Reviews Distribution
* Restaurants per City
###  Bivariate Analysis
* Reviews vs Rating
* Cost vs Rating
* Online Delivery vs Rating
* Table Booking vs Rating
* Competition Density vs Rating

##  Key Insights
* Market is highly saturated with budget-friendly restaurants
* Mid-range restaurants show strong growth potential
* Online delivery has minimal impact on ratings
* Table booking is positively correlated with higher ratings
* High competition density affects the ability to maintain high ratings.

# Feature Engineering & Preprocessing (Week 2)
Created Price_bucket using pd.cut to group prices into meaningful categories
Created location_tier using pd.qcut to represent market activity levels
Handled multi-label Cuisine using MultiLabelBinarizer and reduced to top categories
Applied ColumnTransformer:
StandardScaler → numerical features
OrdinalEncoder → ordered features
OneHotEncoder → categorical features
Performed train-test split before transformation to avoid data leakage

##  Tech Stack

**Languages:**
* Python
**Libraries:**
* Pandas
* NumPy
* Matplotlib
* Seaborn
* BeautifulSoup4
* RapidFuzz
* Scikit-learn (BallTree)

**APIs:**
* OpenStreetMap (Overpass API)

##  Next Steps
* Model Building (Regression & Classification)
* Model Evaluation
* Flask Deployment

##  Setup Instructions
1. Clone the repository:
git clone https://github.com/Aswathi04-ui/Restaurant-Success-Prediction.git
2. Install dependencies:
pip install pandas numpy matplotlib seaborn scikit-learn rapidfuzz
3. Run the notebook:
jupyter notebook





