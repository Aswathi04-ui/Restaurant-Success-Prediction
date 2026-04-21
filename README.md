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
# Zomato
* Collected restaurant data using web scraping techniques
* Extracted key features: Name, Cuisine, Price, Rating, Location, and Services
* Scraped multiple cities focusing on high-traffic restaurant areas
* Used BeautifulSoup and Requests for data extraction
* Created features like hasOnlineDelivery and hasTableBooking
* Parsed data using HTML structure and JSON-LD scripts

# OpenStreetMap (OSM) & Data Merging
* Used Overpass API to collect geographic data (latitude & longitude)
* Applied BallTree to perform spatial analysis
*Calculated competition density (restaurants within 1 km radius) using Haversine distance
* Faced naming inconsistencies between datasets
* Used RapidFuzz (token sort ratio = 85%) for fuzzy matching
* Successfully merged Zomato and OSM data for enriched analysis
# Feature Engineering & Preprocessing 
* Created Price_bucket using pd.cut to group prices into meaningful categories
* Created location_tier using pd.qcut to represent market activity levels
* Handled multi-label Cuisine using MultiLabelBinarizer and reduced to top categories
* Applied ColumnTransformer:
* StandardScaler → numerical features
* OrdinalEncoder → ordered features
* OneHotEncoder → categorical features
* Performed train-test split before transformation to avoid data leakage
## Model Selection
* DecisionTree Regressor
* Random Forest Regressor
* XGBoost Regressor
Best Model: XGBoost Regressor
Chosen based on superior performance on evaluation metrics.
## Evaluation Metrics
Model performance was evaluated using:
R² Score
Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)
## Visualization
A scatter plot of Actual vs Predicted values was used to evaluate model performance.
Points close to the diagonal line indicate better predictions.
## Feature Importance
Feature importance analysis was performed using the XGBoost model to identify key factors influencing predictions.
Top features include:
city,Area
## Success Prediction APP
A Flask-based web application that predicts restaurant ratings using a trained machine learning model. It also uses Generative AI to suggest improvements based on user inputs, helping businesses enhance performance and customer satisfaction.

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


##  Setup Instructions
1. Clone the repository:
git clone https://github.com/Aswathi04-ui/Restaurant-Success-Prediction.git
2. Install dependencies:
pip install pandas numpy matplotlib seaborn scikit-learn rapidfuzz
3. Run the notebook:
jupyter notebook





