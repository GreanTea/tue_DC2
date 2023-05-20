import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from prophet.plot import plot_plotly, plot_components_plotly





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

future = m.make_future_dataframe(periods=200, freq='m')
future['cap']= 700
print(future)

forecast = m.predict(future)
for col in ['yhat', 'yhat_lower', 'yhat_upper']:
    forecast[col] = forecast[col].clip(lower=0.0)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])

fig1 = m.plot(forecast)

fig2 = m.plot_components(forecast)

plot_plotly(m, forecast)

plot_components_plotly(m, forecast)

plt.show()
