import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from prophet.plot import plot_plotly, plot_components_plotly, add_changepoints_to_plot
#from stldecompose import decompose, forecast
#from stldecompose.forecast_funcs import (naive,
#                                         drift,
#                                         mean,
#                                         seasonal_naive)
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.metrics import mean_squared_error



#def get_date_from_index(index):
#    start_date = datetime(2011, 1, 1)  # Starting date: January 1, 2011
#    date = start_date + timedelta(days=index)
#    return date.strftime("20%y-%m-%d")  # Format the date as desired

df_temp = pd.read_csv('data/final.csv')[['ds','y']]

#fig = plt.figure()
#ax = plt.axes()

#ax.plot(df_temp['ds'], df_temp['y'])

#plt.show()

#for x in range(len(df_temp)):
#    df_temp['ds'][x]= get_date_from_index(x)


print(df_temp)
df_temp['cap']=700
m= Prophet(growth='logistic')
m.fit(df_temp)

future = m.make_future_dataframe(periods=0, freq='m')
future['cap']= 700
print(future)

forecast = m.predict(future)
for col in ['yhat', 'yhat_lower', 'yhat_upper']:
    forecast[col] = forecast[col].clip(lower=0.0)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])
print(forecast['trend'])

fig0 = plt.figure()
ax = plt.axes()
ax.plot(df_temp['ds'], (df_temp['y']-forecast['trend']))

plt.title('Detrended amount of burglaries per month')

residuals = df_temp['y'] - forecast['yhat']
fig_acf = plot_acf(residuals, lags =40)

MSE = mean_squared_error(df_temp['y'], forecast['yhat'])
print("The mean squared error is {}".format(MSE))

fig_pacf = plot_pacf(residuals, lags =40)

fig1 = m.plot(forecast)

a=add_changepoints_to_plot(fig1.gca(), m, forecast)

fig2 = m.plot_components(forecast)

plot_plotly(m, forecast)

plot_components_plotly(m, forecast)

plt.show()
