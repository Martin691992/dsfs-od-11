import joblib
import pandas as pd



model = joblib.load("infe_rental_price.joblib")

prediction = pd.DataFrame([{
    "model_key":"Renault", "mileage":45000, "engine_power":90, "fuel":"diesel",
    "paint_color":"black", "car_type":"hatchback",
    "private_parking_available":True, "has_gps":True, "has_air_conditioning":True,
    "automatic_car":False, "has_getaround_connect":False,
    "has_speed_regulator":True, "winter_tires":False
}])

y_pred = model.predict(prediction)

print(y_pred)