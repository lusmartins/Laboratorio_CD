import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from preprocessamento2 import data

var_qualitativas = data[['ticker', 'commodity']]
var_quantitativas = data[['open', 'high', 'low', 'close', 'volume']]
############################################################################

medias = var_quantitativas.mean()
#print(medias)
medias.plot(kind='bar', color = "darkred", edgecolor= 'black')
plt.xlabel('Variáveis')
plt.ylabel('Médias')
plt.title('Médias das Variáveis Quantitativas')
for i, v in enumerate(medias.values):
    plt.text(i, v, f'{v:.2f}', ha='center', va='bottom', fontsize=10)
plt.xticks(rotation=45)  # Rotação dos rótulos para melhor legibilidade
plt.show()

############################################################################
mediana = var_quantitativas.median()
print(mediana)
df_melted = pd.melt(var_quantitativas)
plt.figure(figsize=(12, 6))  
sns.boxplot(x='variable', y='value', data=df_melted, color="darkred")
plt.xlabel('Variáveis')
plt.ylabel('Mediana')
plt.title('Mediana das Variáveis Quantitativas')
plt.xticks(rotation=45)  
plt.show()

###########################################################################

moda = var_quantitativas.mode().iloc[0]
print(f'Moda: \n{moda}')
moda.plot(kind='bar', color = "darkred", edgecolor= 'black')  
plt.xlabel('Variáveis')
plt.ylabel('Moda')
plt.title('Moda das Variáveis Quantitativas')
for i, v in enumerate(moda.values):
    plt.text(i, v, f'{v:.2f}', ha='center', va='bottom', fontsize=10)
plt.xticks(rotation=45)  # Rotação dos rótulos para melhor legibilidade
plt.show()

############################################################################
dp = var_quantitativas.std()
print(dp)
dp.plot(kind='bar', color = "darkred", edgecolor= 'black') 
plt.xlabel('Variáveis')
plt.ylabel('Desvio Padrão')
plt.title('Desvio Padrão das Variáveis Quantitativas')
plt.xticks(rotation=45)  
for i, v in enumerate(dp.values):
    plt.text(i, v, f'{v:.2f}', ha='center', va='bottom', fontsize=10)
plt.xticks(rotation=45)  
plt.show()

############################################################################
maximo = var_quantitativas.max()
#print(f'Máximo: \n{maximo}')
minimo = var_quantitativas.min()
#print(f'Minimo: \n{minimo}')

n_maximos = maximo
print(n_maximos)
n_minimos = minimo
print(n_minimos)
barWidth = 0.25
indice = np.arange(len(var_quantitativas))
plt.figure(figsize = (10,5))
barra1 = np.arange(len(n_maximos))
barra2 = [x + barWidth for x in barra1]

plt.bar(barra1, n_maximos, color = "darkred", width = barWidth, label= 'Máximos')
plt.bar(barra2, n_minimos, color = "red", width = barWidth, label= 'Mínimos')

plt.xlabel("Variáveis")
plt.xticks([b + barWidth for b in range(len(n_maximos))], var_quantitativas)
plt.ylabel('Máximos e Mínimos')
plt.title('Máximos e Mínimos das Variáveis Quantitativas')
plt.legend()

for i, v in enumerate(n_maximos):
    plt.text(i, v+5, f'{v:.2f}', ha='center', va='bottom', fontsize=10)
plt.xticks(rotation=45) 
for i, v in enumerate(n_minimos):
    plt.text(i + barWidth, v+5, f'{v:.2f}', ha='center', va='bottom', fontsize=10)
plt.xticks(rotation=45) 
plt.show()

############################################################################
quartis = var_quantitativas.quantile([0.25, 0.50, 0.75])
print(f'Quartis: \n{quartis}')

plt.boxplot(quartis)
plt.xlabel('Variáveis')
plt.ylabel('Quartis')
plt.title('Quartis das Variáveis Quantitativas')
nomes_variaveis = ['open', 'high', 'low', 'close', 'volume']
plt.xticks(range(1, len(nomes_variaveis) + 1), nomes_variaveis)
plt.show()

############################################################################
# matriz de correlação de toda a tabela #
matriz_correlacao = data.corr()
#print(matriz_correlacao.to_string())plt.boxplot(var_quantitativas)
plt.figure(figsize=(10, 8))
sns.heatmap(matriz_correlacao, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de Correlação')
plt.show()

############################################################################
#gráfico de relação entre o preço máximo durante o pagão e o preço de mercado no dia #
plt.scatter(var_quantitativas['high'], var_quantitativas['open'], color = "darkred", edgecolor= 'black')
plt.xlabel('Preço máximo')
plt.ylabel('Preço de Abertura')
plt.title('Relação entre o Preço Máximo e o Preço de Abertura')
plt.show()

#gráfico de relação entre o preço máximo durante o pagão e o volume de negociação #
plt.scatter(var_quantitativas['high'], var_quantitativas['volume'], color = "darkred", edgecolor= 'black')
plt.xlabel('Preço máximo')
plt.ylabel('Volume de Negociação')
plt.title('Relação entre Volume e Preço Máximo')
plt.show()

############################################################################
#gráfico de relação entre o volume de contratos durante o tempo#
plt.plot(data['date'], var_quantitativas['volume'], label='Volume', color = "darkred")
plt.xlabel('Data de Registros')
plt.ylabel('Volume de Negociações')
plt.title('Volume de negociações ao Longo do Tempo')
plt.show()

############################################################################ 
#gráficos de frequencias de todas as variáveis qualitativas

fig, axs = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Distribuição de Dados')

axs[0, 0].hist(data['open'], bins=30, color='darkred', edgecolor='black')
axs[0, 0].set_title('Preços de Abertura')
axs[0, 0].set_xlabel('Preço')
axs[0, 0].set_ylabel('Frequência')

axs[0, 1].hist(data['close'], bins=30, color='darkred', edgecolor='black')
axs[0, 1].set_title('Preços de Fechamento')
axs[0, 1].set_xlabel('Preço')
axs[0, 1].set_ylabel('Frequência')

axs[0, 2].hist(data['high'], bins=30, color='darkred', edgecolor='black')
axs[0, 2].set_title('Preços Máximos')
axs[0, 2].set_xlabel('Preço')
axs[0, 2].set_ylabel('Frequência')


axs[1, 0].hist(data['low'], bins=30, color='darkred', edgecolor='black')
axs[1, 0].set_title('Preços Mínimos')
axs[1, 0].set_xlabel('Preço')
axs[1, 0].set_ylabel('Frequência')


axs[1, 1].hist(data['volume'], bins=30, color='darkred', edgecolor='black')
axs[1, 1].set_title('Volume de Negociação')
axs[1, 1].set_xlabel('Volume')
axs[1, 1].set_ylabel('Frequência')

fig.delaxes(axs[1, 2])

plt.tight_layout()
plt.show()