# app.py
import streamlit as st
from datetime import datetime
import pandas as pd
import pydeck as pdk

# Set page title
st.set_page_config(page_title="Trip Fare Predictor", layout="wide")

st.title("Trip Fare Predictor")

# Sidebar for inputs
st.sidebar.header("Trip Details")

# Pickup Date and Time
pickup_date = st.sidebar.date_input("Pickup Date", datetime.now().date())
pickup_time = st.sidebar.time_input("Pickup Time", datetime.now().time())
pickup_datetime = datetime.combine(pickup_date, pickup_time)

# Other trip details
locations = ["Downtown", "Airport", "Train Station", "University", "Mall", "Stadium"]
pickup_location = st.sidebar.selectbox("Pickup Location", locations)
dropoff_location = st.sidebar.selectbox("Dropoff Location", locations)

passenger_count = st.sidebar.number_input("Passenger Count", min_value=1, max_value=10, value=1)
distance_km = st.sidebar.number_input("Distance (km)", min_value=0.1, value=5.0)

# Display user inputs
st.subheader("Selected Trip Details")
st.write("Pickup Date & Time:", pickup_datetime)
st.write("Pickup Location:", pickup_location)
st.write("Dropoff Location:", dropoff_location)
st.write("Passenger Count:", passenger_count)
st.write("Distance (km):", distance_km)

# Simple fare calculation
base_fare = 10.00
per_km_rate = 15.00
passenger_surcharge = 9.00 * (passenger_count - 1)
estimated_fare = base_fare + (distance_km * per_km_rate) + passenger_surcharge

st.subheader("Estimated Fare")
st.write(f"${estimated_fare:.2f}")

# --- Map visualization with route ---
# Predefined coordinates for example locations
location_coords = {
    "Downtown": (40.7128, -74.0060),
    "Airport": (40.6413, -73.7781),
    "Train Station": (40.7506, -73.9935),
    "University": (40.7291, -73.9965),
    "Mall": (40.7580, -73.9855),
    "Stadium": (40.8296, -73.9262)
}

pickup_coord = location_coords.get(pickup_location, (40.7128, -74.0060))
dropoff_coord = location_coords.get(dropoff_location, (40.7128, -74.0060))

# Create a DataFrame for the points
points_df = pd.DataFrame({
    "lat": [pickup_coord[0], dropoff_coord[0]],
    "lon": [pickup_coord[1], dropoff_coord[1]],
    "type": ["Pickup", "Dropoff"]
})

# Create a DataFrame for the route line
route_df = pd.DataFrame({
    "start_lat": [pickup_coord[0]],
    "start_lon": [pickup_coord[1]],
    "end_lat": [dropoff_coord[0]],
    "end_lon": [dropoff_coord[1]]
})

# Define deck.gl layers
point_layer = pdk.Layer(
    "ScatterplotLayer",
    data=points_df,
    get_position='[lon, lat]',
    get_color='[255, 0, 0]' ,
    get_radius=300,
    pickable=True
)

line_layer = pdk.Layer(
    "LineLayer",
    data=route_df,
    get_source_position='[start_lon, start_lat]',
    get_target_position='[end_lon, end_lat]',
    get_color='[0, 0, 255]',
    get_width=5
)

# Set the map view
view_state = pdk.ViewState(
    latitude=(pickup_coord[0]+dropoff_coord[0])/2,
    longitude=(pickup_coord[1]+dropoff_coord[1])/2,
    zoom=12,
    pitch=0
)

# Render the map
st.subheader("Trip Map")
r = pdk.Deck(layers=[point_layer, line_layer], initial_view_state=view_state)
st.pydeck_chart(r)




