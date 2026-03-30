# Restaurant-Success-Prediction
##Project Overview
This project aims to analyze restaurant data and predict restaurant success based on various factors such as cost, reviews, services, and location.By combining Zomato web-scraped data with geographic insights from OpenStreetMap (OSM), it identifies key success factors like price-to-rating ratios and competition density.The dataset is built by combining data from multiple sources and performing exploratory data analysis (EDA) to understand key patterns influencing restaurant ratings.

-Extracts restaurant details (Price, Rating, Cuisine) from Zomato.
-Enriches that data with GPS coordinates and competition density using the Overpass API (OSM).
-Synchronizes two different datasets using Fuzzy String Matching to account for naming variations.
-Visualizes market trends to define what makes a restaurant successful in a crowded market.

##Data Collection
###Zomato Web Scraping
Restaurant data was collected using web scraping techniques:
Extracted features:
Name,Cuisine,Price,Rating,City & Area.Average Cost for Two,Online Delivery availability,Table Booking 
Restaurant link
Tools: BeautifulSoup, Requests.
Logic: Iterates through multiple cities (Bangalore, Mumbai, etc.) and specific high-traffic areas.
Feature Engineering: Extracted hasOnlineDelivery and hasTableBooking by parsing unstructured text cards and JSON-LD scripts.
###OpenStreetMap (OSM) Data
Tools: Overpass API, BallTree (from Scikit-Learn).
Spatial Analysis: Fetched latitude/longitude for restaurants.
Competition Density: Used a Haversine-based BallTree algorithm to count how many competitors exist within a 1km radius for every single restaurant.
###Data Merging (Fuzzy Logic),Data Integration
Challenge: Zomato and OSM often name the same restaurant differently (e.g., "McDonald's" vs "McDonald's India").
Solution: Implemented Rapidfuzz with a token sort ratio threshold of 85%. This allowed for a high-accuracy merge across different data sources.Fuzzy matching helps find the closest matching name between datasets.
###Exploratory Data Analysis (EDA)
Univariate Analysis:Distribution of Ratings,Price  distribution,Topcuisines,Reviews,distribution,Restaurants per city.
distribution:Reviews vs Rating,Cost vs Rating,Online Delivery vs Rating,Table Booking vs Rating
Competition Density vs Rating.
Key Insights:
-Identified that the market is heavily saturated with budget-friendly options, making the "mid-range" a potential blue ocean.
-Discovered that while delivery doesn't significantly impact ratings, table bookings correlate with higher customer satisfaction.
-Analyzed how high competition density affects a restaurant's ability to maintain a 4.5 + rating.
##Tech Stack
-Languages: Python
-Libraries: Pandas, NumPy, Matplotlib, Seaborn, BeautifulSoup4, RapidFuzz, Scikit-Learn (BallTree)
-APIs: Overpass API (OpenStreetMap).
###Next Steps:
-Data Cleaning & Preprocessing
-Feature Engineering
-Model Building (Regression & Classification)
-Model Evaluation
-Flask Deployment
##Setup Instructions
1.Clone the repository:
git clone https://github.com/Aswathi04-ui/Restaurant-Success-Prediction.git
2.Install dependencies:
pip install pandas numpy matplotlib seaborn scikit-learn rapidfuzz
3.Run the notebook:
jupyter notebook
##Note:
-latitude, longitude, and competition density features were included to enhance the dataset. Their usefulness will be evaluated during modeling, and they may be retained or dropped based on performance.
-Missing values exist due to:
Incomplete matches between Zomato and OSM datasets
Missing geographic data
These values are intentionally retained and will be handled during preprocessing.
##Success Metric
Restaurant success is defined using:
Rating (Regression Problem)
Continuous target variable
Higher rating ,more successful restaurant



