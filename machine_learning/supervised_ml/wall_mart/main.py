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
print(data.dtypes)

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
print("modele trained")


pred = regression.predict(X_test)
r2 = r2_score(Y_test,pred)
mae = mean_absolute_error(Y_test, pred)
rmse = root_mean_squared_error(Y_test, pred)

print(f"R² (test)   : {r2:.4f}")
print(f"MAE (test)  : {mae:.2f}")
print(f"RMSE (test) : {rmse:.2f}")
