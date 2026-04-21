from flask import Flask,render_template,request
import pandas as pd 
import numpy as np 
import joblib
from dotenv import load_dotenv

load_dotenv()
app=Flask(__name__)

#load

model = joblib.load(os.path.join(os.path.dirname(__file__), 'model.pkl'))
#setup gemini ap
import os
from google import genai
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))





#home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    city              = request.form['city']
    area              = request.form['area']
    cuisine           = request.form['cuisine']
    price             = float(request.form['price'])
    reviews           = float(request.form['reviews'])
    has_delivery      = int(request.form.get('hasOnlineDelivery', 0))
    has_booking       = int(request.form.get('hasTableBooking', 0))
    cost_category     = request.form['cost_category']

#City restaurant count 
    city_count_map = {
        'Chennai':539, 'Bangalore':454, 'Kolkata':420,
        'Trichy':396, 'Hyderabad':344, 'Pune':336,
        'Mumbai':325, 'Kochi':322, 'Coimbatore':314,
        'Ahmedabad':210, 'Mangalore':200, 'Mysore':107,
        'Other':50
    }
    city_restaurant_count = city_count_map.get(city, 50)

    price_bucket = (
        'Budget'    if price <= 300 else
        'Mid-range' if price <= 600 else
        'Premium'   if price <= 1000 else
        'Luxury'
    )
    location_tier = (
        'High_activity'   if city_restaurant_count >= 380 else
        'Medium_activity' if city_restaurant_count >= 200 else
        'Low_activity'
    )
    input_data = pd.DataFrame([{
        'Price'               : price,
        'hasOnlineDelivery'   : has_delivery,
        'hasTableBooking'     : has_booking,
        'Reviews'             : reviews,
        'city_restaurant_count': city_restaurant_count,
        'Price_bucket'        : price_bucket,
        'location_tier'       : location_tier,
        'City'                : city,
        'Area'                : area,
        'Cost_Category'       : cost_category,
        # Cuisine binary columns — all 0, set matching one to 1
        'Cuisine_North Indian': 1 if cuisine == 'North Indian' else 0,
        'Cuisine_South Indian': 1 if cuisine == 'South Indian' else 0,
        'Cuisine_Chinese'     : 1 if cuisine == 'Chinese'      else 0,
        'Cuisine_Fast Food'   : 1 if cuisine == 'Fast Food'    else 0,
        'Cuisine_Cafe'        : 1 if cuisine == 'Cafe'         else 0,
        'Cuisine_Other'       : 1 if cuisine == 'Other'        else 0,

        'Cuisine_Desserts': 1 if cuisine == 'Desserts' else 0,
        'Cuisine_Beverages': 1 if cuisine == 'Beverages' else 0,
        'Cuisine_Continental': 1 if cuisine == 'Continental' else 0,

    # fallback
        'Cuisine_Other': 1 if cuisine == 'Other' else 0,
    }])
#Predict
    predicted_rating = round(float(model.predict(input_data)[0]), 2)

# Get GenAI business suggestions
    suggestions = get_genai_suggestions(
        city, cuisine, price, predicted_rating,
        has_delivery, has_booking, cost_category
    )
#Send everything to result page
    return render_template('result.html',
        rating      = predicted_rating,
        city        = city,
        cuisine     = cuisine,
        price       = price,
        suggestions = suggestions
    )
# ── GenAI function ──────────────────────────────────────────
def get_genai_suggestions(city, cuisine, price, rating,
                           delivery, booking, cost_cat):
    
    prompt = f"""
You are a restaurant business consultant in India.

A restaurant has these details:
- City: {city}
- Cuisine: {cuisine}
- Price for two: ₹{price}
- Has online delivery: {'Yes' if delivery else 'No'}
- Has table booking: {'Yes' if booking else 'No'}
- Cost category: {cost_cat}
- Predicted rating: {rating} out of 5

Based on this predicted rating of {rating}, give exactly 4 specific,
actionable business improvements this restaurant can make to increase
their rating. Be specific to their city and cuisine type.
Keep each suggestion to 1-2 sentences. Format as a numbered list.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text 

    except Exception:
       #fall back (so app never crashes)
        return f"""
1. Improve food quality and consistency for {cuisine} cuisine
2. Optimize pricing strategy in {city} based on competitors
3. Enhance customer service and reduce waiting time
4. Increase online visibility and delivery efficiency
"""

    return response.text

# Run the app
if __name__ == '__main__':
    app.run(debug=True)