import datetime
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

df['date'] = pd.to_datetime(df['date'])
# sirve para convertir la columna 'date' en un objeto de tipo datetime
df['month'] = df['date'].dt.month_name().str.slice(stop=3)
# crea una nueva columna 'month' que contiene el nombre del mes extraído de la columna 'date', y luego se corta a los primeros 3 caracteres para obtener la abreviatura del mes
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
df['month'] = pd.Categorical(df['month'], categories=months, ordered=True)
# convierte la columna 'month' en una categoría ordenada utilizando la lista de meses como categorías
df['year'] = df['date'].dt.strtimemp('%Y')
# crea una nueva columna 'year' que contiene el año extraído de la columna 'date

df_by_month = df.groupby('month')['month'].sum().reset_index()
# agrupa el DataFrame por la columna 'month' y suma los valores de la columna 'month' para cada mes, luego se restablece el índice del DataFrame resultante
df_by_month.head()

# Vamos a crear una columna para variables categoricas llamada nivel de ataque
df_by_month['attack_level'] = pd.qcut(df_by_month['number_of_attacks'],
                                     4,
                                     labels=['Mild', 'Scattered', 'High', 'Severe'])
# crea una nueva columna 'attack_level' que categoriza los valores de la columna 'number_of_attacks' en 4 categorías utilizando la función pd.cut, y asigna etiquetas a cada categoría
df_by_month.head()

#Codigo de nivel de ataque
# crea una nueva columna 'stike_level_code' que contiene los códigos numéricos correspondientes a las categorías de la columna 'strike_level' utilizando el atributo 'cat.codes'
df_by_month['stike_level_code'] = df_by_month['strike_level'].cat.codes
df_by_month.head()

#get_dummies se trata de una función de pandas que se utiliza para convertir variables categóricas en variables dummy o variables indicadoras. Esta función crea nuevas columnas para cada categoría única en la variable categórica, asignando un valor de 1 a la columna correspondiente si la fila pertenece a esa categoría y un valor de 0 en caso contrario. Esto es útil para preparar los datos para modelos de machine learning que requieren variables numéricas.
pd.get_dummies(df_by_month['strike_level'])


#crea un nuevo DataFrame 'df_by_month_plot' utilizando la función pivot para reorganizar los datos, donde las filas corresponden a los años, las columnas corresponden a los meses y los valores corresponden a los códigos de nivel de ataque. Luego se muestra las primeras filas del nuevo DataFrame utilizando el método head()
df_by_month_plot = df_by_month.pivot('year', 'month', 'strike_level_code')
df_by_month_plot.head()

# crea un mapa de calor utilizando la función heatmap de seaborn, donde los datos se toman del DataFrame 'df_by_month_plot', se utiliza la paleta de colores 'YlGnBu' y se habilita la anotación de los valores en cada celda del mapa de calor. Luego se muestra el gráfico utilizando plt.show()
ax = sns.heatmap(df_by_month_plot, camp='Blues')
colorbar = ax.collections[0].colorbar
colorbar.set_ticks([0.5, 1.5, 2.5, 3.5])
colorbar.set_ticklabels(['Mild', 'Scattered', 'High', 'Severe'])
plt.show()