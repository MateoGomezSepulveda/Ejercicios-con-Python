# Por que debemos valdiar los datos de entrada? 
# 1) mejoramos el rendimiento del modelo, 2) evitamos errores en el proceso de entrenamiento.
# puede ayudar a prevenir problemas como valores faltantes, valores atipicos, datos inconsistentes o datos que no cumplen con los requisitos del modelo.
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns   

# sirve para cargar un archivo CSV llamado 'data.csv' en un DataFrame de pandas llamado 'df'
df.head()

# muestra los tipos de datos de cada columna en el DataFrame 'df' utilizando el atributo 'dtypes'
print(df.dtypes)

# convierte la columna 'date' del DataFrame 'df' en un objeto de tipo datetime utilizando la función pd.to_datetime, lo que permite realizar operaciones y análisis relacionados con fechas de manera más eficiente y precisa.
df['date'] = pd.to_datetime(df['date'])

# muestra el número de valores faltantes en cada columna del DataFrame 'df' utilizando el método isnull() para identificar los valores nulos y sum() para contar la cantidad de valores faltantes en cada columna.
df.isnull().sum()

# muestra un resumen estadístico de todas las columnas del DataFrame 'df', incluyendo tanto las columnas numéricas como las categóricas, utilizando el método describe() con el argumento include='all'.
df.describe(include='all')

# crea un rango de fechas completo desde el 1 de enero de 2018 hasta el 31 de diciembre de 2023 utilizando la función pd.date_range, y luego utiliza el método difference() para encontrar las fechas que están presentes en el rango completo pero no están presentes en la columna 'date' del DataFrame 'df'. Esto puede ayudar a identificar fechas faltantes en los datos.
full_date_range = pd.date_range(start = '2018-0101', end = '2023-12-31')
full_date_range.difference(df['date'])

# crea un gráfico de caja (boxplot) utilizando la función boxplot de seaborn, donde el eje y representa la columna 'number_of_strikes' del DataFrame 'df'. Este tipo de gráfico es útil para visualizar la distribución de los datos, identificar valores atípicos y comparar diferentes grupos o categorías. El argumento showfliers=False se utiliza para ocultar los valores atípicos en el gráfico, lo que puede ayudar a enfocarse en la distribución general de los datos sin que los valores extremos distorsionen la visualización.
sns.boxplot(y = df['number_of_strikes']), showfliers = False

#
df_points = df[['latitude', 'longitude']].drop_duplicates()
df_points.head()


df_points = df[['latitude', 'longitude']].drop_duplicates()
p = px.scatter_geo(df_points, lat='latitude', lon='longitude')
p.show()
#








