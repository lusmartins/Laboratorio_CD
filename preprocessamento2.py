
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('C:/Users/Luciana/OneDrive/Documentos/Laboratório CD Projetos/Projeto_LABCD/all_grains_data.csv')

print(dataset.isnull().to_string())
print(dataset.isnull().sum())

dataset['commodity'] = dataset['commodity'].replace({'Rough Rice': 0, 'Soybean Oil': 1, 'Corn':2, 'Soybean': 3, 'KC HRW Wheat': 4, 'Oat':5})
dataset['date'] = pd.to_datetime(dataset['date'], format='%Y/%m/%d')
dataset['open'] = pd.to_numeric(dataset['open'], errors='coerce')
dataset['high'] = pd.to_numeric(dataset['high'], errors='coerce')
dataset['low'] = pd.to_numeric(dataset['low'], errors='coerce')
dataset['close'] = pd.to_numeric(dataset['close'], errors='coerce')
datasets = dataset.sort_values(by='date') #dataset organizado cronologicamente 
print(dataset)

min_volume = dataset['volume'].min()
max_volume = dataset['volume'].max()

min_intervalo = 0
max_intervalo = 10000
dataset['volume'] = ((dataset['volume'] - min_volume) / (max_volume - min_volume)) * (max_intervalo - min_intervalo) + min_intervalo

data = dataset
print(f'Dataset atualizado: \n{data}')
