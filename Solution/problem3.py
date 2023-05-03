#importing libraries
import pandas as pd
# from google.colab import drive
import numpy as np


#PreProcessing
import sklearn
import joblib

# Models
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error


models=[]
mae_models=[]
mse_models=[]

def test_eval(algorithm, mae,mse):
    models.append(algorithm)
    mae_models.append(mae)
    mse_models.append(mse)

def randomForest(X_train, X_test, y_train, y_test):
    model=RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    test_eval("Random Forest", mae,mse)
    return model

def preprocessing(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    # Remove rows with NaN values
    df.dropna(inplace=True)
    return df

def split_data(df, features, target):
    X = df[features]
    y = df[target]
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

if __name__ == '__main__':
    #location='data/problem2/output/output.parquet'
    location = input("Enter data input location: ")
    df = pd.read_parquet(location)
    df = df.iloc[:3000]
    features = ['vol_moving_avg', 'adj_close_rolling_med']
    target = 'Volume'
    df = preprocessing(df)
    X_train, X_test, y_train, y_test = split_data(df, features, target)
    model = randomForest(X_train, X_test, y_train, y_test)

    eval_ros_df = pd.DataFrame({'model': models,
                                'mae': mae_models,
                                'mse': mse_models})
    # Save the model as a pickle in a file
    joblib.dump(model, 'model.pkl')
