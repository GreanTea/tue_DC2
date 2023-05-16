from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import numpy as np


data = pd.read_csv('final.csv')
data['ds'] = pd.to_datetime(data['ds'])

train_data = data[:-12]
test_data = data[-12:]

model = ARIMA(train_data['y'], order=(1, 1, 1))
model_fit = model.fit()

forecast_values = model_fit.forecast(steps=12)

mae = np.mean(np.abs(test_data['y'] - forecast_values))

mse = np.mean((test_data['y'] - forecast_values) ** 2)

rmse = np.sqrt(mse)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)

