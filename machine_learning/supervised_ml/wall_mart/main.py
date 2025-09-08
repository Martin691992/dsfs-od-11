import pandas as pd
import numpy as np
from os import curdir, listdir, chdir

from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, root_mean_squared_error

chdir("./supervised_ml/wall_mart")
data = pd.read_csv('./data/clean_data.csv',index_col=0)
data = data.drop('Date',axis=1)
print(data.head())

target = "Weekly_Sales"
X = data.drop(columns=[target])
y = data[target]

X_train, X_test, Y_train, Y_test = train_test_split(X,y,test_size=0.2, random_state=42)

cat_features = ["Holiday_Flag","Store"]
numeric_features = ["Temperature","Fuel_Price","CPI","Unemployment","year","month","day","day_of_week"]

numeric_tranformer = Pipeline(steps=[("scaler", StandardScaler())])
cat_transformer = Pipeline(steps=[("encoder",OneHotEncoder(drop="first"))])
preprocessor = ColumnTransformer(transformers=[
    ("num",numeric_tranformer,numeric_features),
    ('cat',cat_transformer,cat_features)])

X_train = preprocessor.fit_transform(X_train)
X_test = preprocessor.transform(X_test)


regression = LinearRegression()
regression.fit(X_train,Y_train)

pred_train = regression.predict(X_train)
r2_train = r2_score(Y_train,pred_train)
mae_train = mean_absolute_error(Y_train, pred_train)
rmse_train = root_mean_squared_error(Y_train, pred_train)

print(f"R² (train)   : {r2_train}")
print(f"MAE (train)  : {mae_train}")
print(f"RMSE (train) : {rmse_train}")

print("----")
pred_test = regression.predict(X_test)
r2_test = r2_score(Y_test,pred_test)
mae_test = mean_absolute_error(Y_test, pred_test)
rmse_test = root_mean_squared_error(Y_test, pred_test)

print(f"R² (test)   : {r2_test}")
print(f"MAE (test)  : {mae_test}")
print(f"RMSE (test) : {rmse_test}")

print(regression.coef_)
column_names = []
for name, pipeline, features_list in preprocessor.transformers_: # loop over pipelines
    if name == 'num': # if pipeline is for numeric variables
        features = features_list # just get the names of columns to which it has been applied
    else: # if pipeline is for categorical variables
        features = pipeline.named_steps['encoder'].get_feature_names_out() # get output columns names from OneHotEncoder
    column_names.extend(features) # concatenate features names
        
coefs = pd.DataFrame(index = column_names, data = regression.coef_.transpose(), columns=["coefficients"])

feature_importance = abs(coefs).sort_values(by = 'coefficients')
print(feature_importance.head(10))