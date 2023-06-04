import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from prophet.plot import plot_plotly, plot_components_plotly, add_changepoints_to_plot
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.metrics import mean_squared_error
import numpy as np


df_final = pd.read_csv('final_ward.csv')

ward = 'Barnet Vale'
fig,axs = plt.subplots(nrows=4, ncols=6,figsize=(30,10))


for i in range(len(df_final.columns.values[5:])):
    ward = df_final.columns.values[i+5]

    print(ward)
    df_ward = pd.DataFrame()

    df_ward[['ds', 'y']] = df_final[['ds', ward]]

    #df_ward['cap']=50


    m= Prophet()
    m.fit(df_ward)


    future = m.make_future_dataframe(periods=12, freq='m')
    future['cap']= 50

    forecast = m.predict(future)
    for col in ['yhat', 'yhat_lower', 'yhat_upper']:
        forecast[col] = forecast[col].clip(lower=0.0)
    hi = m.plot(forecast, ax=axs[divmod(i, 6)])
    axs[divmod(i, 6)].title.set_text(ward)
    #a=add_changepoints_to_plot(fig1.gca(), m, forecast)


plt.show()
