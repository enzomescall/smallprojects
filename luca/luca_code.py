import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('luca/data.csv', sep=';')

new_columns = {'Nome do Estabelecimento':'nome',
                     '1.2 Tipo de estabelecimento - originalmente destinado': 'tipo',
                     '1.3 Capacidade do estabelecimento | Regime fechado | Total': 'capacidade fechado',
                     '1.3 Capacidade do estabelecimento | Regime semiaberto | Total': 'capacidade semiaberto',
                     '1.3 Capacidade do estabelecimento | Regime aberto | Total': 'capacidade aberto',
                     '1.3 Capacidade do estabelecimento | Masculino | Total': 'capacidade masculina total',
                     '1.3 Capacidade do estabelecimento | Feminino | Total': 'capacidade feminina total',
                     '4.1 População prisional | Presos sentenciados - regime fechado | Total': 'população fechado',
                     '4.1 População prisional | Presos sentenciados - regime semiaberto | Total': 'população semiaberto',
                     '4.1 População prisional | Presos sentenciados - regime aberto | Total': 'população aberto',}

data.rename(columns=new_columns, inplace=True)

data['capacidade total'] = data['capacidade masculina total'] + data['capacidade feminina total'] # nao sei se isso ta certo

filtered_data = data[['nome', 'tipo', 'capacidade total',
                      'capacidade fechado', 'capacidade semiaberto', 'capacidade aberto',
                      'população fechado', 'população semiaberto', 'população aberto']]


# print(filtered_data.head())

filtered_data['percent_populacao_fechado'] = filtered_data['população fechado'] / filtered_data['capacidade fechado'] * 100
filtered_data['percent_populacao_semiaberto'] = filtered_data['população semiaberto'] / filtered_data['capacidade semiaberto'] * 100
filtered_data['percent_populacao_aberto'] = filtered_data['população aberto'] / filtered_data['capacidade aberto'] * 100

# o jeito q eu to fazendo aqui, se a populacao for maior que a capacidade, o valor vai ser negativo
filtered_data['raw_populacao_fechado'] = filtered_data['população fechado'] - filtered_data['capacidade fechado']
filtered_data['raw_populacao_semiaberto'] = filtered_data['população semiaberto'] - filtered_data['capacidade semiaberto']
filtered_data['raw_populacao_aberto'] = filtered_data['população aberto'] - filtered_data['capacidade aberto']

filtered_data.replace([np.inf, -np.inf], np.nan, inplace=True)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.hist(filtered_data['raw_populacao_fechado'], bins=10, edgecolor='black')
plt.xlabel('População Bruta Fechado')
plt.ylabel('Frequência')
plt.title('Histograma da População Bruta Fechado')

plt.subplot(1, 3, 2)
plt.hist(filtered_data['raw_populacao_semiaberto'], bins=10, edgecolor='black')
plt.xlabel('População Bruta Semiaberto')
plt.ylabel('Frequência')
plt.title('Histograma da População Bruta Semiaberto')

plt.subplot(1, 3, 3)
plt.hist(filtered_data['raw_populacao_aberto'], bins=10, edgecolor='black')
plt.xlabel('População Bruta Aberto')
plt.ylabel('Frequência')
plt.title('Histograma da População Bruta Aberto')

plt.tight_layout()
plt.show()