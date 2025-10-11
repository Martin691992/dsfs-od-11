import joblib
import pandas as pd
import json
import sys
import os


if __name__ == "__main__":
    # print(os.getcwd())
    arguments = sys.argv
    if len(arguments) == 0 :
        print("Vous devez fournir un argument")
    else:
        data = arguments[1].split(',')
        data_dict ={}
        for i in data : 
            data_dict[i.split(':')[0]] = i.split(':')[1]

        for i in data_dict:
            if data_dict[i] == "True":
                data_dict[i] = True
            elif data_dict[i] == "False":
                data_dict[i] = False

        model = joblib.load("src/lib/server/inference/infe_rental_price.joblib")
        ex_prediction = pd.DataFrame([data_dict])
        y_pred = model.predict(ex_prediction)
        print(y_pred)
