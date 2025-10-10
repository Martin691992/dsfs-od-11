import joblib
import pandas as pd
import sys
import os


if __name__ == "__main__":
    arguments = sys.argv
    if len(arguments) == 0 :
        print("Vous devez fournir un argument")
    else:
        data = arguments[1]
        # print(os.getcwd())
        model = joblib.load("src/lib/server/inference/infe_rental_price.joblib")

        ex_prediction = pd.DataFrame([{
            "model_key":"Renault", "mileage":45000, "engine_power":90, "fuel":"diesel",
            "paint_color":"black", "car_type":"hatchback",
            "private_parking_available":True, "has_gps":True, "has_air_conditioning":True,
            "automatic_car":False, "has_getaround_connect":False,
            "has_speed_regulator":True, "winter_tires":False
        }])

        y_pred = model.predict(ex_prediction)
        print(y_pred)
