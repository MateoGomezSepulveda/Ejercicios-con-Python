import numpy as ap
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('WazeData.csv')

df.head()

df.size

df.info()

df.describe()

plt.figure(figsize=(10,2))
plt.title('Boxplot of monthly sessions')
sns.boxplot(data=None, x=data['sessions'], fliersize=1)

plt.figure(figsize=(5,3))
plt.title('histogram of ocurrence of a user opening the app during the month')
sns.histplot(df['sessions'])
median = df['sessions'].median()
plt.axvline(median, color='red', linestyle='--')
plt.text(75,1200, 'median=56.0', color='red')

plt.figure(figsize=(10,2))
plt.title('Boxplot of monthly drives')
sns.boxplot(data=None, x=data['drives'], fliersize=1)

# Histograma para analizar la frecuencia de los viajes realizados en el mes.
# Configura el lienzo (10x2) con su título para evaluar visualmente la forma de la 
# distribución y los rangos de viajes más comunes entre los usuarios.
# Crear una funccion que sirva como base para todos los histogramas
def histogrammer(column_str, median_text=true, **kwargs):
    median=round(df[column_str].median(), 1)
    plt.figure(figsize=(5,3))
    ax = sns.histoplot(x=df[column_str], **kwargs)
    plt.axvline(median, color='red', linestyle='--')
    if median_text==true:
        ax.text(0.25, 0.85, f'median={median}', color='red',
            ha='left', va='top', transform=ax.transAxes)
    else:
        print('Median:', median)
    plt.title(f'{column_str} histogram')

# Ejecutar
histogrammer('drives')

plt.figure(figsize=(10,2))
plt.title('Boxplot of total sessions')
sns.boxplot(data=None, x=data['total_sessions'], fliersize=1)

histogrammer('total_sessions')

plt.figure(figsize=(8,1))
plt.title('Boxplot Number of days since a user signed')
sns.boxplot(data=None, x=df['n_days_after_onboarding'], fliersize=1)

histogrammer('n_days_after_onboarding')

plt.figure(figsize=(8,1))
plt.title('Boxplot driven_km_drives')
sns.boxplot(data=None, x=df['driven_km_drives'], fliersize=1)

histogrammer('driven_km_drives')

plt.figure(figsize=(8,1))
plt.title('Duration minutes drives Boxplot')
sns.boxplot(data=None, x=df['duration_minutes_drives'], fliersize=1)

histogrammer('duration_minutes_drives')

plt.figure(figsize=(8,1))
plt.title('Activity days boxplot')
sns.boxplot(data=None, x=df['activity_days'], fliersize=1)

histogrammer('activity_days')

plt.figure(figsize=(8,1))
plt.title('driving_days box plot')
sns.boxplot(data=None, x=df['driving_days'], fliersize=1)

histogrammer('driving_days')

# Gráfico de pastel (Pie chart) para analizar la distribución de usuarios según su dispositivo.
# Corrige el pequeño error de dedo en el título original ('divice' -> 'device').
# Se utiliza .value_counts() para obtener los totales de cada tipo de dispositivo (iPhone vs. Android)
# y se configuran etiquetas dinámicas que muestran el nombre del dispositivo junto a su cantidad exacta.
plt.figure(figsize=(3,3))
data = df['device'].value_counts()

plt.pie(data,
        labels=[f'{data.index[0]}: {data.values[0]}',
                f'{data.index[1]}: {data.values[1]}'],
        autopct='%1.1f%%'
        )
plt.title('Users by device')

# Gráfico de pastel (Pie chart) para analizar la proporción de usuarios retenidos vs. la tasa de abandono (churn).
# Utiliza .value_counts() para contar cuántos usuarios pertenecen a cada categoría ('retained' vs. 'churned').
# Muestra etiquetas dinámicas con el total exacto por grupo (.values) y calcula el porcentaje con un decimal.

fig = plt.figure(figsize=(3,3))
data = df['label'].value_counts()

plt.pie(data,
        labels=[f'{data.index[0]}: {data.values[0]}',
                f'{data.index[1]}: {data.values[1]}'],
        autopct='%1.1f%%'
        )
plt.title('Count of retained vs. churned')

# Histograma comparativo de días de conducción frente a días de actividad.
# Al pasar ambas columnas como una lista a plt.hist(), Matplotlib creará barras
# agrupadas lado a lado para cada contenedor (bin) del 0 al 32. Esto permite una
# comparación directa y visual de cómo se cruzan ambos comportamientos en el mes.
plt.figure(figsize=(12,4))
label = ['Días conducidos', 'Días de actividad']

plt.hist([df['driving_days'], df['activity_days']],
         bins=range(0, 33),
         label=label)

plt.xlabel('Days')
plt.ylabel('Count')
plt.legend()
plt.title('Días conducidos vs. Días de actividad');

# Imrpimir el numero maximo de dias para cada variable
print(df['driving_days'].max())
print(df['activity_days'].max())

# Gráfico de dispersión (Scatter plot) para analizar la relación entre días de conducción y días de actividad.
# Incluye una línea de referencia diagonal (y = x) en color rojo y trazo punteado.
# Permite identificar visualmente si existen usuarios que registran más días de conducción que de actividad,
# lo cual indicaría una anomalía o un error potencial en la captura de los datos.
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='driving_days', y='activity_days')
plt.title('Días conduciendo vs. Días activos')

# Pintar la línea de identidad diagonal desde el punto (0,0) hasta el (31,31)
plt.plot([0,31], [0,31], color='red', linestyle='--')

# Histograma agrupado (usando histplot) para analizar la retención y el abandono según el dispositivo.
# El argumento 'multiple="dodge"' separa las barras de 'retained' y 'churned' lado a lado en lugar de apilarlas.
# El parámetro 'shrink=0.9' añade un pequeño espacio entre los bloques de barras, mejorando la estética del gráfico.
plt.figure(figsize=(5,4))
sns.histplot(data=df,
             x='device',
             hue='label',
             multiple='dodge',
             shrink=0.9
             )
plt.title('Retention by device histogram');

# 1. Crear la nueva columna 'km_per_driving_day'
# Representa la distancia promedio conducida por cada día de manejo en el mes.
# Se obtiene dividiendo los kilómetros totales ('driven_km_drives') entre los días de conducción ('driving_days').
df['km_per_driving_day'] = df['driven_km_drives'] / df['driving_days']

# 2. Obtener el resumen estadístico descriptivo de la nueva columna
# Ejecuta .describe() para analizar métricas clave como la media, la mediana (50%),
# los valores mínimos/máximos y evaluar la dispersión de este nuevo promedio.
df['km_per_driving_day'].describe()

# 1. Reemplazar los valores infinitos (provocados por la división por cero) por 0.
# Utiliza df.loc para localizar las filas donde 'km_per_driving_day' sea igual a np.inf
# y asigna el valor de 0 en esa misma columna para limpiar los datos.
df.loc[df['km_per_driving_day'] == np.inf, 'km_per_driving_day'] = 0

# 2. Confirmar que el reemplazo funcionó correctamente.
# Al ejecutar nuevamente .describe(), la media y la desviación estándar ya no serán infinitas o NaN,
# y el valor máximo reflejará la distancia real más alta por día conducido.
df['km_per_driving_day'].describe()


# Configurar el tamaño del lienzo para que sea lo suficientemente ancho (12x5)
plt.figure(figsize=(12,5))
# Graficar el histograma de porcentaje apilado al 100%
sns.histplot(data=df,
             x='km_per_driving_day',         # Variable cuantitativa en el eje X
             bins=range(0, 1201, 20),         # Contenedores de 20 km en 20 km, limitando el máximo a 1200 km
             hue='label',                     # Separar visualmente por estado del usuario (retained vs. churned)
             multiple='fill')                 # Parámetro clave: escala las barras al 100% para mostrar proporciones

# Ajustar la etiqueta del eje Y para que muestre el símbolo de porcentaje de forma horizontal
plt.ylabel('%', rotation=0)

# Asignar el título descriptivo al gráfico
plt.title('Tasa de abandono según el promedio de kilómetros recorridos por día');



# Configurar el tamaño del lienzo (12x5) para observar con claridad la tendencia mensual
plt.figure(figsize=(12,5))

# Graficar el histograma de porcentaje apilado para evaluar la fidelidad según los días de uso
sns.histplot(data=df,
             x='driving_days',         # Variable cuantitativa discreta en el eje X (días del mes)
             bins=range(1, 32),        # Contenedores para agrupar los datos del día 1 al 31
             hue='label',              # Segmentar por estado del usuario (retained vs. churned)
             multiple='fill',          # Escalar todas las barras al 100% para mostrar la tasa de abandono
             discrete=True)            # Parámetro clave: alinea las barras exactamente sobre cada número entero (día)

# Ajustar la etiqueta del eje Y para representar el porcentaje de forma horizontal
plt.ylabel('%', rotation=0)

# Asignar el título descriptivo al gráfico
plt.title('Abandonos por número de días conducidos');


df['percent_sessions_in_last_month'] = df['sessions'] / df['total_sessions']


df['percent_sessions_in_last_month'].median()

# 1. Configurar el tamaño del lienzo para una vista compacta y alargada (8x2).
# 2. Asignar el título descriptivo al gráfico de distribución.
# 3. Graficar el histograma de la proporción de sesiones del último mes.
# 4. Calcular de forma independiente la mediana de los datos (percentil 50%).
# 5. Dibujar una línea vertical en la posición de la mediana para marcar el centro.
# 6. Configurar la línea de color rojo y estilo discontinuo ('--') para que resalte.
plt.figure(figsize=(8,2))
plt.title('Histogram of percent sessions in last month')
sns.histplot(df['percent_sessions_in_last_month'])
media = df['percent_sessions_in_last_month'].median()
plt.axvline(media, color='red', linestyle='--');


# variable media de la columna 'n_days_after_onboarding'
df['n_days_after_onboarding'].median()

# 1. Filtrar el dataframe para conservar solo los usuarios con un 40% o más de sesiones en el último mes.
# 2. Configurar el tamaño del lienzo en proporciones compactas (5x2).
# 3. Asignar el título descriptivo para identificar el histograma de días desde el registro.
# 4. Graficar la distribución de la columna 'n_days_after_onboarding' para el segmento filtrado.
data = df.loc[df['percent_sessions_in_last_month'] >= 0.4]
plt.figure(figsize=(5,2))
plt.title('Histogram n_days_after_onboarding')
sns.histplot(x=data['n_days_after_onboarding']);


# 1. Definir una función para imputar valores atípicos (outliers) utilizando un percentil como umbral.
# 2. Calcular el valor de corte (threshold) correspondiente al percentil indicado usando el método .quantile().
# 3. Localizar las filas donde el valor supera el umbral y reemplazarlas con ese mismo valor límite.
# 4. Imprimir un reporte en consola alineado a la derecha con el nombre de la columna, el percentil y su umbral.
def outlier_imputer(column_name, percentile):
    # Calcular el valor del percentil especificado (ej. 0.95 para el percentil 95)
    threshold = df[column_name].quantile(percentile)
    # Reemplazar cualquier valor que supere el umbral con el valor del umbral
    df.loc[df[column_name] > threshold, column_name] = threshold
    # Mostrar el resultado en pantalla con un formato limpio y alineado (| columna | percentil | umbral)
    print('{:>25} | percentile: {} | threshold: {}'.format(column_name, percentile, threshold))


# 1. Iterar a través de la lista de columnas numéricas que presentaron valores atípicos severos.
# 2. Aplicar la función 'outlier_imputer' en cada iteración para limitar los datos al percentil 95 (0.95).
# 3. La función modificará el DataFrame 'df' en sitio e imprimirá un reporte de los umbrales aplicados.

for column in ['sessions', 'drives', 'total_sessions',
               'driven_km_drives', 'duration_minutes_drives']:
    outlier_imputer(column, 0.95)