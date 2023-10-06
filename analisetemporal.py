
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from preprocessamento2 import data

time_series_data_milho = data[data['commodity'] == 2][['date', 'open']]
time_series_data_trigo = data[data['commodity'] == 4][['date', 'open']]

time_series_data_milho['date'] = pd.to_datetime(time_series_data_milho['date'], format='%Y%m%d')
time_series_data_trigo['date'] = pd.to_datetime(time_series_data_trigo['date'], format='%Y%m%d')

time_series_data_milho.set_index('date', inplace=True)
time_series_data_trigo.set_index('date', inplace=True)

X_milho = sm.add_constant(range(len(time_series_data_milho)))
y_milho = time_series_data_milho['open']
model_milho = sm.OLS(y_milho, X_milho).fit()

X_trigo = sm.add_constant(range(len(time_series_data_trigo)))
y_trigo = time_series_data_trigo['open']
model_trigo = sm.OLS(y_trigo, X_trigo).fit()

const_milho, trend_milho = model_milho.params[0], model_milho.params[1]
const_trigo, trend_trigo = model_trigo.params[0], model_trigo.params[1]

time_series_data_milho['trend_line'] = const_milho + trend_milho * range(len(time_series_data_milho))
time_series_data_trigo['trend_line'] = const_trigo + trend_trigo * range(len(time_series_data_trigo))

plt.figure(figsize=(12, 6))
plt.plot(time_series_data_milho.index, time_series_data_milho['open'], label='Preços de Abertura (Milho)', color='darkred')
plt.plot(time_series_data_trigo.index, time_series_data_trigo['open'], label='Preços de Abertura (Trigo KC HRW)', color='darkblue')
plt.plot(time_series_data_milho.index, time_series_data_milho['trend_line'], linestyle='--', color='darkred')
plt.plot(time_series_data_trigo.index, time_series_data_trigo['trend_line'], linestyle='--', color='darkblue')
plt.xlabel('Data')
plt.ylabel('Preços de Abertura')
plt.title('Análise de Tendência Temporal - Preços de Abertura (Milho vs. Trigo KC HRW)')
plt.legend()
plt.show()