import pandas as pd
import numpy as np
from os import chdir

from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.metrics import r2_score, mean_absolute_error, root_mean_squared_error

# chdir("./supervised_ml/wall_mart")
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

print(f"R2 (train)   : {r2_train}")
print(f"MAE (train)  : {mae_train}")
print(f"RMSE (train) : {rmse_train}")

print("----")
pred_test = regression.predict(X_test)
r2_test = r2_score(Y_test,pred_test)
mae_test = mean_absolute_error(Y_test, pred_test)
rmse_test = root_mean_squared_error(Y_test, pred_test)

print(f"R2 (test)   : {r2_test}")
print(f"MAE (test)  : {mae_test}")
print(f"RMSE (test) : {rmse_test}")
print("")
# print(regression.coef_)

## Du cours JEDHA
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

print("")
print("Recherche meilleur hyper parametres :")
params_ridge = {'alpha':[0.1,0.2,0.5,0.8,1.1,1.2,1.5,5,10]}
search_params_ridge = GridSearchCV(Ridge(),param_grid=params_ridge)
search_params_ridge.fit(X_train,Y_train)
best_alpha = search_params_ridge.best_params_['alpha']

print(f"Meilleur Alpha : {best_alpha}")
print("")
print("Using Ridge")
ridge = Ridge(alpha=best_alpha)
ridge.fit(X_train,Y_train)
y_pred_ridge = ridge.predict(X_test)

print(r2_score(Y_test,y_pred_ridge))
print("")

print('LASSO')

params_lasso = {"alpha": [0.001, 0.01, 0.05, 0.1, 0.5, 1.0, 5.0, 10.0]}
search_params_lasso = GridSearchCV(Lasso(),param_grid=params_lasso)
search_params_lasso.fit(X_train,Y_train)
best_alpha_lasso = search_params_lasso.best_params_['alpha']
print(f"Meilleur alpha pour Lasso : {best_alpha_lasso}")
print("Entrainement avec le meilleur LASSO possible")
lasso = Lasso(alpha=best_alpha_lasso)
lasso.fit(X_train,Y_train)
y_pred_lasso = lasso.predict(X_test)
print(f"R2 score : {r2_score(Y_test,y_pred_lasso)}")