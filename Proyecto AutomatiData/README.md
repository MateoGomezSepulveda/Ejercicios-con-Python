# Curso 2 Proyecto Automatidata  
## Curso 2 - Ve más allá de los números: Traduce los datos en información

Eres el nuevo profesional de datos en una firma ficticia de consultoría de datos: Automatidata. El equipo está en una etapa temprana del proyecto, habiendo completado apenas un plan de acción inicial y algunos trabajos preliminares en Python.  

Luana Rodríguez, la analista senior de datos en Automatidata, está satisfecha con el trabajo que ya has realizado y solicita tu ayuda con tareas de análisis exploratorio de datos (EDA) y visualización para el proyecto de la Comisión de Taxis y Limusinas de la Ciudad de Nueva York (New York City TLC), con el fin de obtener una comprensión general de cómo es el uso de taxis.  

El equipo directivo pide un notebook en Python que muestre la estructuración y limpieza de datos, así como visualizaciones con matplotlib/seaborn para ayudar a entender la información. Como mínimo, incluye un diagrama de caja (box plot) de las duraciones de los viajes y algunas gráficas de series temporales, como un desglose por trimestre o por mes.  

Además, el equipo directivo ha solicitado recientemente que todo EDA incluya visualizaciones en Tableau. Para estos datos de taxis, crea un dashboard en Tableau que muestre un mapa de la ciudad de Nueva York con los viajes de taxi/limusina por mes. Asegúrate de que sea fácil de entender para alguien sin conocimientos técnicos de datos, y recuerda que el subdirector de la NYC TLC es una persona con discapacidad visual.  

Un notebook ya fue estructurado y preparado para ayudarte en este proyecto. Por favor, completa las siguientes preguntas.  

## Curso 2 Proyecto final: Análisis exploratorio de datos  
En esta actividad, examinarás los datos proporcionados y los prepararás para el análisis. También diseñarás una visualización profesional que cuente una historia y ayude a tomar decisiones basadas en datos para necesidades empresariales.  

Ten en cuenta que la actividad de visualización en Tableau es opcional y no afectará la finalización del curso. Completarla te ayudará a practicar la planificación y el diseño de una visualización basada en una necesidad empresarial específica. La estructura de esta actividad está diseñada para emular las propuestas que probablemente se te asignen en tu carrera como profesional de datos. Completar esta actividad te ayudará a prepararte para esos momentos profesionales.  

El propósito de este proyecto es realizar un análisis exploratorio de datos (EDA) sobre un conjunto de datos proporcionado. Tu misión es continuar la investigación que comenzaste en el Curso 1 y realizar un análisis más profundo de estos datos con el objetivo de aprender más sobre las variables.  

El objetivo es limpiar el conjunto de datos y crear una visualización.  

### Esta actividad tiene 4 partes:  
1. Imports, enlaces y carga de datos  
2. Exploración de datos  
3. Construcción de visualizaciones  
4. Evaluar y compartir resultados  

Sigue las instrucciones y responde las preguntas que aparecen a continuación para completar la actividad. Luego, deberás realizar un Resumen Ejecutivo utilizando las preguntas listadas en el documento de estrategia PACE.  

Asegúrate de completar esta actividad antes de continuar. El siguiente elemento del curso te proporcionará un ejemplo completo para comparar con tu propio trabajo.  

Aquí tienes la traducción al español:  

## Tarea 2a. Exploración y limpieza de datos Decide qué columnas son aplicables  

El primer paso es evaluar tus datos. Revisa la página de Data Source en Tableau Public para tener una idea del tamaño, la forma y la composición del conjunto de datos. Luego respóndete estas preguntas:  

### Según nuestro escenario, ¿qué columnas de datos son más aplicables?  
### ¿Qué columnas puedo eliminar, sabiendo que no ayudarán a resolver el problema?  

Considera funciones que te ayudan a entender y estructurar los datos:  
- `head()`  
- `describe()`  
- `info()`  
- `groupby()`  
- `sortby()`  

Preguntas clave:  
### ¿Qué haces con los datos faltantes (si los hay)?  
### ¿Existen valores atípicos (*outliers*)? ¿Cuáles son y cómo podrías manejarlos?  
### ¿Qué te dicen las distribuciones de tus variables sobre la pregunta que estás haciendo o el problema que intentas resolver?  

Indicaciones finales: 
Comienza descubriendo el dataset usando `head()` y `size`.  

## Tarea 2b. Evaluar si las dimensiones y medidas son correctas
En la página de Data Source en Tableau, verifica nuevamente los tipos de datos de las columnas aplicables que seleccionaste en el paso anterior. Presta especial atención a las dimensiones y medidas para asegurarte de que sean correctas.

En Python, revisa los tipos de datos de las columnas. Pregúntate: ¿tienen sentido?

Revisa el enlace proporcionado en las instrucciones de la actividad anterior para crear la visualización requerida en Tableau.

## Importaciones de librerías

    import numpy as np 
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import datetime as dt

## 2. Carga de datos
    df = pd.read_csv('automatiData.csv')
leemos el archivo CSV 'automatiData.csv' y lo almacenamos en un DataFrame llamado 'df' utilizando la función 'read_csv' de pandas

## 3. Exploración de datos:
    df.head()
muestra las primeras filas del DataFrame 'df' utilizando el método head()

## 4. Información sobre los datos
    df.dtypes
 muestra los tipos de datos de cada columna en el DataFrame 'df' utilizando el atributo 'dtypes'

## 5. Descripción de los datos
    df.describe()
muestra estadísticas descriptivas de las columnas numéricas del DataFrame 'df' utilizando el método

## 6. Información adicional sobre los datos
    df.info()
muestra un resumen de la información del DataFrame 'df', incluyendo el número de filas,

## 7. Limpieza de datos
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
convierte las columnas 'tpep_pickup_datetime' y 'tpep_dropoff_datetime' a formato de fecha y hora utilizando la función 'to_datetime' de pandas

## 8. Visualización de Datos (Análisis Univariado).
    plt.figure(figsize=(10,2))
    plt.title('Trip Distance')
    sns.boxplot(data=None, x=df['trip_distance'], fliersize=1);
crea una figura de tamaño 10x2, establece el título 'Trip Distance' y utiliza la función 'boxplot' de seaborn para crear un diagrama de caja de la columna 'trip_distance' del DataFrame 'df', con un tamaño de marcador de 1 para los valores atípicos (fliersize=1)

## 9. Visualización de Datos (Análisis Bivariado).
    plt.figure(figsize=(15,5))
    plt.title('Histogram of Trip Distance')
    sns.histplot(df['trip_distance'], bins=range(0,26,1))
crea una figura de tamaño 15x5, establece el título 'Histogram of Trip Distance' y utiliza la función 'histplot' de seaborn para crear un histograma de la columna 'trip_distance' del DataFrame 'df', con los intervalos de los bins definidos por el rango de 0 a 25 con un paso de 1 (bins=range(0,26,1))

## 10. Visualización de Datos (Análisis Bivariado).
    plt.figure(figsize=(10,2))
    plt.title('Total Amount')
    sns.boxplot(data=None, x=df['total_amount'], fliersize=2)
crea una figura de tamaño 10x2, establece el título 'Total Amount' y utiliza la función 'boxplot' de seaborn para crear un diagrama de caja de la columna 'total_amount' del DataFrame 'df', con un tamaño de marcador de 2 para los valores atípicos (fliersize=2)

## 11. Visualización de Datos (Análisis Bivariado).
    plt.figure(figsize=(10,2))
    plt.title('Histogram of Total Amount')
    sns.histplot(df['total_amount'], bins=range(0,26,1))
crea una figura de tamaño 10x2, establece el título 'Histogram of Total Amount' y utiliza la función 'histplot' de seaborn para crear un histograma de la columna 'total_amount' del DataFrame 'df', con los intervalos de los bins definidos por el rango de 0 a 25 con un paso de 1 (bins=range(0,26,1))

## 12. Visualización de Datos (Análisis Bivariado).
    plt.figure(figsize=(10,2))
    plt.title('Tip Amount')
    sns.boxplot(data=None, x=df['tip_amount'], fliersize=1)
crea una figura de tamaño 10x2, establece el título 'Tip Amount' y utiliza la función 'boxplot' de seaborn para crear un diagrama de caja de la columna 'tip_amount' del DataFrame 'df', con un tamaño de marcador de 1 para los valores atípicos (fliersize=1)

## 13. Visualización de Datos (Análisis Bivariado).
    plt.figure(figsize=(10,2))
    plt.title('Histogram of Tip Amount')
    sns.histplot(df['tip_amount'], bins=range(0,16,1))
crea una figura de tamaño 10x2, establece el título 'Histogram of Tip Amount' y utiliza la función 'histplot' de seaborn para crear un histograma de la columna 'tip_amount' del DataFrame 'df', con los intervalos de los bins definidos por el rango de 0 a 15 con un paso de 1 (bins=range(0,16,1))

## 14. Visualización de Datos (Análisis Bivariado).
    plt.figure(figsize=(12,7))
    plt.title('Tip Amount By Vendor')
    ax = sns.histplot(
        data=df,
        x="tip_amount",
        bins=range(0,21,1),
        hue="VendorID",
        multiple="stack",
    )

    ax.set_xticks(range(0,21,1))
    ax.set_xticklabels(range(0,21,1));
crea una figura de tamaño 12x7, establece el título 'Tip Amount By Vendor' y utiliza la función 'histplot' de seaborn para crear un histograma de la columna 'tip_amount' del DataFrame 'df', con los intervalos de los bins definidos por el rango de 0 a 20 con un paso de 1 (bins=range(0,21,1)), y separa las barras por la columna 'VendorID' utilizando el parámetro 'hue'. Luego, se establecen las marcas del eje x con los mismos intervalos utilizando 'set_xticks' y se etiquetan con los mismos valores utilizando 'set_xticklabels'.

## 15. Visualización de Datos (Análisis Bivariado).
    tips_over_ten = df[df['tip_amount'] > 10]
    plt.figure(figsize=(12,7))
    plt.title('Tip amount by vendor histogram');

    ax = sns.histplot(
        data=tips_over_ten, x='tip_amount', bins=range(10,21,1), 
        hue='VendorID', 
        multiple='stack'
        )

    ax.set_xticks(range(10,21,1))
    ax.set_xticklabels(range(10,21,1));
crea una figura de tamaño 12x7, establece el título 'Tip amount by vendor histogram' y utiliza la función 'histplot' de seaborn para crear un histograma de la columna 'tip_amount' del DataFrame 'tips_over_ten', que contiene solo las filas donde el valor de 'tip_amount' es mayor a 10. Los intervalos de los bins se definen por el rango de 10 a 20 con un paso de 1 (bins=range(10,21,1)), y las barras se separan por la columna 'VendorID' utilizando el parámetro 'hue'. Luego, se establecen las marcas del eje x con los mismos intervalos utilizando 'set_xticks' y se etiquetan con los mismos valores utilizando 'set_xticklabels'.

## 16. Visualización de Datos (Análisis Bivariado).
    df["passenger_count"].value_counts()
muestra el conteo de cada valor único en la columna 'passenger_count' del DataFrame 'df' utilizando el método 'value_counts()'

    mean_tips_by_passenger_count = df.groupby(['passenger_count']).mean()[['tip_amount']]
    mean_tips_by_passenger_count
agrupa el DataFrame 'df' por la columna 'passenger_count', calcula la media de las columnas numéricas para cada grupo utilizando el método 'mean()', y luego selecciona solo la columna 'tip_amount' para mostrar la media de las propinas por número de pasajeros. El resultado se almacena en el DataFrame 'mean_tips_by_passenger_count' y se muestra en pantalla.

## 17. Visualización de Datos (Análisis Bivariado).
    data = mean_tips_by_passenger_count.tail(-1)
    pal = sns.color_palette("Greens_d", len(data))
    rank = data['tip_amount'].argsort().argsort()
    plt.figure(figsize=(12,7))
    ax = sns.barplot(x=data.index,
                y=data['tip_amount'],
                palette=np.array(pal[::-1])[rank])
    ax.axhline(df['tip_amount'].mean(), ls='--', color='red', label='global mean')
    ax.legend()
    plt.title('Mean tip amount by passenger count', fontsize=16);
crea una figura de tamaño 12x7, establece el título 'Mean tip amount by passenger count' con un tamaño de fuente de 16, y utiliza la función 'barplot' de seaborn para crear un gráfico de barras que muestra la media de las propinas por número de pasajeros. El eje x se establece con los índices del DataFrame 'data', y el eje y se establece con los valores de la columna 'tip_amount' del DataFrame 'data'. La paleta de colores se define utilizando la función 'color_palette' de seaborn con el esquema "Greens_d" y se ordena según el ranking de las propinas. Además, se agrega una línea horizontal al gráfico que representa la media global de las propinas utilizando 'axhline', con un estilo de línea discontinua ('--'), color rojo, y una etiqueta 'global mean'. Finalmente, se muestra la leyenda del gráfico utilizando 'legend()'.

## 18. Visualización de Datos (Análisis Bivariado).
    df['month'] = df['tpep_pickup_datetime'].dt.month_name()
crea una nueva columna 'month' en el DataFrame 'df' que contiene el nombre del mes extraído de la columna 'tpep_pickup_datetime' utilizando el atributo 'dt.month_name()'

## 19. Visualización de Datos (Análisis Bivariado).
    df['day'] = df['tpep_pickup_datetime'].dt.day_name()
crea una nueva columna 'day' en el DataFrame 'df' que contiene el nombre del día de la semana extraído de la columna 'tpep_pickup_datetime' utilizando el atributo 'dt.day_name()'

## 20. Visualización de Datos (Análisis Bivariado).
    monthly_rides = df['month'].value_counts()
    monthly_rides
cuenta el número de ocurrencias de cada valor único en la columna 'month' del DataFrame 'df' utilizando el método 'value_counts()' y almacena el resultado en la variable 'monthly_rides', que se muestra en pantalla.

## 21. Visualización de Datos (Análisis Bivariado).
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
            'August', 'September', 'October', 'November', 'December']

    monthly_rides = monthly_rides.reindex(index=month_order)
    monthly_rides
define un orden específico para los meses del año utilizando una lista 'month_order', y luego reordena el Series 'monthly_rides' utilizando el método 'reindex()' con el índice definido por 'month_order'. El resultado se almacena nuevamente en 'monthly_rides' y se muestra en pantalla.

## 22. Visualización de Datos (Análisis Bivariado).
    monthly_rides.index
muestra el índice del Series 'monthly_rides', que contiene los nombres de los meses del año en el orden definido por 'month_order'

## 23. Visualización de Datos (Análisis Bivariado).
    plt.figure(figsize=(12,7))
    ax = sns.barplot(x=monthly_rides.index, y=monthly_rides)
    ax.set_xticklabels(month_order)
    plt.title('Ride count by month', fontsize=16);
crea una figura de tamaño 12x7, establece el título 'Ride count by month' con un tamaño de fuente de 16, y utiliza la función 'barplot' de seaborn para crear un gráfico de barras que muestra el conteo de viajes por mes. El eje x se establece con los índices del Series 'monthly_rides', que contienen los nombres de los meses del año, y el eje y se establece con los valores del Series 'monthly_rides', que contienen el conteo de viajes. Además, se establecen las etiquetas del eje x utilizando 'set_xticklabels()' con la lista 'month_order' para asegurarse de que los meses se muestren en el orden correcto.

## 24. Visualización de Datos (Análisis Bivariado).
    daily_rides = df['day'].value_counts()
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    daily_rides = daily_rides.reindex(index=day_order)
    daily_rides
cuenta el número de ocurrencias de cada valor único en la columna 'day' del DataFrame 'df' utilizando el método 'value_counts()', define un orden específico para los días de la semana utilizando una lista 'day_order', y luego reordena el Series 'daily_rides' utilizando el método 'reindex()' con el índice definido por 'day_order'. El resultado se almacena nuevamente en 'daily_rides' y se muestra en pantalla.

## 25. Visualización de Datos (Análisis Bivariado).
    plt.figure(figsize=(12,7))
    ax = sns.barplot(x=daily_rides.index, y=daily_rides)
    ax.set_xticklabels(day_order)
    ax.set_ylabel('Count')
    plt.title('Ride count by day', fontsize=16);
crea una figura de tamaño 12x7, establece el título 'Ride count by day' con un tamaño de fuente de 16, y utiliza la función 'barplot' de seaborn para crear un gráfico de barras que muestra el conteo de viajes por día de la semana. El eje x se establece con los índices del Series 'daily_rides', que contienen los nombres de los días de la semana, y el eje y se establece con los valores del Series 'daily_rides', que contienen el conteo de viajes. Además, se establecen las etiquetas del eje x utilizando 'set_xticklabels()' con la lista 'day_order' para asegurarse de que los días se muestren en el orden correcto, y se establece la etiqueta del eje y como 'Count' utilizando 'set_ylabel()'.

## 26. Visualización de Datos (Análisis Bivariado).
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    total_amount_day = df.groupby('day').sum()[['total_amount']]
    total_amount_day = total_amount_day.reindex(index=day_order)
    total_amount_day
define un orden específico para los días de la semana utilizando una lista 'day_order', agrupa el DataFrame 'df' por la columna 'day', calcula la suma de las columnas numéricas para cada grupo utilizando el método 'sum()', y luego selecciona solo la columna 'total_amount' para mostrar la suma total de los montos por día de la semana. El resultado se almacena en el DataFrame 'total_amount_day', que se reordena utilizando el método 'reindex()' con el índice definido por 'day_order' para asegurarse de que los días se muestren en el orden correcto, y se muestra en pantalla.

## 27. Visualización de Datos (Análisis Bivariado).
    plt.figure(figsize=(12,7))
    ax = sns.barplot(x=total_amount_day.index, y=total_amount_day['total_amount'])
    ax.set_xticklabels(day_order)
    ax.set_ylabel('Revenue (USD)')
    plt.title('Total revenue by day', fontsize=16);
crea una figura de tamaño 12x7, establece el título 'Total revenue by day' con un tamaño de fuente de 16, y utiliza la función 'barplot' de seaborn para crear un gráfico de barras que muestra el ingreso total por día de la semana. El eje x se establece con los índices del DataFrame 'total_amount_day', que contienen los nombres de los días de la semana, y el eje y se establece con los valores de la columna 'total_amount' del DataFrame 'total_amount_day', que contienen la suma total de los montos por día. Además, se establecen las etiquetas del eje x utilizando 'set_xticklabels()' con la lista 'day_order' para asegurarse de que los días se muestren en el orden correcto, y se establece la etiqueta del eje y como 'Revenue (USD)' utilizando 'set_ylabel()'.

## 28. Visualización de Datos (Análisis Bivariado).
    total_amount_month = df.groupby('month').sum()[['total_amount']]
    total_amount_month = total_amount_month.reindex(index=month_order)
    total_amount_month
agrupa el DataFrame 'df' por la columna 'month', calcula la suma de las columnas numéricas para cada grupo utilizando el método 'sum()', y luego selecciona solo la columna 'total_amount' para mostrar la suma total de los montos por mes. El resultado se almacena en el DataFrame 'total_amount_month', que se reordena utilizando el método 'reindex()' con el índice definido por 'month_order' para asegurarse de que los meses se muestren en el orden correcto, y se muestra en pantalla.

## 29. Visualización de Datos (Análisis Bivariado).
    plt.figure(figsize=(12,7))
    ax = sns.barplot(x=total_amount_month.index, y=total_amount_month['total_amount'])
    plt.title('Total revenue by month', fontsize=16);
crea una figura de tamaño 12x7, establece el título 'Total revenue by month' con un tamaño de fuente de 16, y utiliza la función 'barplot' de seaborn para crear un gráfico de barras que muestra el ingreso total por mes. El eje x se establece con los índices del DataFrame 'total_amount_month', que contienen los nombres de los meses del año, y el eje y se establece con los valores de la columna 'total_amount' del DataFrame 'total_amount_month', que contienen la suma total de los montos por mes.

## 30. Visualización de Datos (Análisis Bivariado).
    df['PULocationID'].nunique()
    df['DOLocationID'].nunique()
muestra el número de valores únicos en la columna 'DOLocationID' del DataFrame 'df' utilizando el método 'nunique()'

## 31. Visualización de Datos (Análisis Bivariado).
    distance_by_dropoff = df.groupby('DOLocationID').mean()[['trip_distance']]
agrupa el DataFrame 'df' por la columna 'DOLocationID', calcula la media de las columnas numéricas para cada grupo utilizando el método 'mean()', y luego selecciona solo la columna 'trip_distance' para mostrar la distancia promedio por ubicación de destino. El resultado se almacena en el DataFrame 'distance_by_dropoff' y se muestra en pantalla.

## 32. Visualización de Datos (Análisis Bivariado).
    distance_by_dropoff = distance_by_dropoff.sort_values(by='trip_distance')
    distance_by_dropoff 
ordena el DataFrame 'distance_by_dropoff' por la columna 'trip_distance' utilizando el método 'sort_values()' y muestra el resultado en pantalla. Esto permite identificar las ubicaciones de destino con las distancias promedio más bajas y más altas.

## 33. Visualización de Datos (Análisis Bivariado).
    plt.figure(figsize=(14,6))
    ax = sns.barplot(x=distance_by_dropoff.index, 
                    y=distance_by_dropoff['trip_distance'],
                    order=distance_by_dropoff.index)
    ax.set_xticklabels([])
    ax.set_xticks([])
    plt.title('Mean trip distance by drop-off location', fontsize=16);
crea una figura de tamaño 14x6, establece el título 'Mean trip distance by drop-off location' con un tamaño de fuente de 16, y utiliza la función 'barplot' de seaborn para crear un gráfico de barras que muestra la distancia promedio por ubicación de destino. El eje x se establece con los índices del DataFrame 'distance_by_dropoff', que contienen los IDs de las ubicaciones de destino, y el eje y se establece con los valores de la columna 'trip_distance' del DataFrame 'distance_by_dropoff', que contienen la distancia promedio por ubicación de destino. Además, se ocultan las etiquetas y las marcas del eje x utilizando 'set_xticklabels([])' y 'set_xticks([])' para mejorar la legibilidad del gráfico debido a la gran cantidad de ubicaciones.

## 34. Visualización de Datos (Análisis Bivariado).
#1. Generate random points on a 2D plane from a normal distribution

    test = np.round(np.random.normal(10, 5, (3000, 2)), 1)
    midway = int(len(test)/2)  # Calculate midpoint of the array of coordinates
    start = test[:midway]      # Isolate first half of array ("pick-up locations")
    end = test[midway:]        # Isolate second half of array ("drop-off locations")

## 2. Calculate Euclidean distances between points in first half and second half of array
    distances = (start - end)**2           
    distances = distances.sum(axis=-1)
    distances = np.sqrt(distances)
## 3. Group the coordinates by "drop-off location", compute mean distance
    test_df = pd.DataFrame({'start': [tuple(x) for x in start.tolist()],
                    'end': [tuple(x) for x in end.tolist()],
                    'distance': distances})
    data = test_df[['end', 'distance']].groupby('end').mean()
    data = data.sort_values(by='distance')
## 4. Plot the mean distance bet ween each endpoint ("drop-off location") and all points it connected to
    plt.figure(figsize=(14,6))
    ax = sns.barplot(x=data.index,
                    y=data['distance'],
                    order=data.index)
    ax.set_xticklabels([])
    ax.set_xticks([])
    ax.set_xlabel('Endpoint')
    ax.set_ylabel('Mean distance to all other points')
    ax.set_title('Mean distance between points taken randomly from normal distribution');

1. Genera puntos aleatorios en un plano 2D a partir de una distribución normal
2. Calcula las distancias euclidianas entre los puntos de la primera mitad y la segunda mitad del array
3. Agrupa las coordenadas por "ubicación de destino", calcula la distancia media
4. Grafica la distancia media entre cada punto final ("ubicación de destino") y todos los puntos a los que se conectó.

## 35. Resumen Ejecutivo
    df['DOLocationID'].max() - len(set(df['DOLocationID'])) 
calcula la diferencia entre el valor máximo de la columna 'DOLocationID' del DataFrame 'df' y el número de valores únicos en esa columna utilizando la función 'set()' para obtener los valores únicos. Esto puede indicar si hay IDs de ubicación de destino faltantes o si hay IDs que no se utilizan en el conjunto de datos.

## 36. Visualización de Datos (Análisis Bivariado).
    plt.figure(figsize=(16,4))
DOLocationID column is numeric, so sort in ascending order

    sorted_dropoffs = df['DOLocationID'].sort_values()
Convert to string

    sorted_dropoffs = sorted_dropoffs.astype('str')
### Plot
    sns.histplot(sorted_dropoffs, bins=range(0, df['DOLocationID'].max()+1, 1))
    plt.xticks([])
    plt.xlabel('Drop-off locations')
    plt.title('Histogram of rides by drop-off location', fontsize=16);
1. Crea una figura de tamaño 16x4 para el gráfico.
2. Ordena la columna 'DOLocationID' del DataFrame 'df' en orden ascendente utilizando el método 'sort_values()' y almacena el resultado en la variable 'sorted_dropoffs'.
3. Convierte la variable 'sorted_dropoffs' a tipo de dato string utilizando

## 37. Visualización de Datos (Análisis Bivariado).
    df['trip_duration'] = (df['tpep_dropoff_datetime']-df['tpep_pickup_datetime'])
crea una nueva columna 'trip_duration' en el DataFrame 'df' que contiene la duración del viaje calculada como la diferencia entre las columnas 'tpep_dropoff_datetime' y 'tpep_pickup_datetime'. El resultado es un objeto de tipo timedelta que representa la duración del viaje.

## 38. Visualización de Datos (Análisis Bivariado).
    df.head(10)
muestra las primeras 10 filas del DataFrame 'df' utilizando el método 'head(10)' para verificar que la nueva columna 'trip_duration' se haya creado correctamente y contiene los valores esperados.
