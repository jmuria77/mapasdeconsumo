# -*- coding: utf-8 -*-
'''Análisis estadísticos de los datos'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Lectura de datos
DATOS = ('https://github.com/jmuria77/mapasdeconsumo/datos/')
# Diccionarios
habitos = {'Sí': 1.0, 'No': 0.0}
compras = {'Aumentado': 1.0, 'Disminuido': -1.0, 'Las mismas que antes': 0}
# Arrays de atributos
puntuaciones = ['Calidad', 'Variedad', 'Cercanía', 'Puntuación']
correlaciones = ['Edad', 'Hábitos', 'Compras', 'Puntuación']
# Carga de datos
datos = pd.read_csv(DATOS + 'datos.csv', encoding='utf-8', sep=',')
datos = datos.set_index('Referencia')
datos = datos.replace(habitos)
datos = datos.replace(compras)
pair = datos[puntuaciones]
corr = datos[correlaciones].corr(method='spearman')
# Diagrama de cajas
plt.figure()
sns.boxplot(data=pair, orient='h')
plt.xlim([0, 10])
plt.title('Análisis de algunas de las puntuaciones')
plt.tight_layout()
# Matriz de correlación de Spearman
plt.figure()
sns.set(font_scale=0.75)
sns.heatmap(corr, annot=True, cbar=False, fmt='.2f', cmap='icefire')
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.title('Correlación entre atributos relevantes')
plt.tight_layout()
# Gráfica pairplot
sns.pairplot(pair)
plt.tight_layout()
