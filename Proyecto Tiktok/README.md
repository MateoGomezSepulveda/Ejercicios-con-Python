Proyecto TikTok
Curso 2 - Ir más allá de los números: Traducir datos en información (Insights)

El equipo de datos de TikTok aún se encuentra en las etapas iniciales de su proyecto más reciente. Hasta el momento, han completado una propuesta de proyecto y han utilizado Python para inspeccionar y organizar el conjunto de datos de TikTok.

Orion Rainier, científico de datos en TikTok, está complacido con el trabajo que ya has completado y solicita tu ayuda para realizar un Análisis Exploratorio de Datos (EDA) y la visualización de los mismos. El equipo directivo solicitó ver un cuaderno de Python (Jupyter Notebook) que muestre la estructuración y limpieza de los datos, así como cualquier visualización de matplotlib/seaborn graficada para ayudarnos a comprender la información. Como mínimo, incluye un gráfico que compare el conteo de reclamaciones (claims) frente al conteo de opiniones (opinions), así como diagramas de caja (boxplots) de las variables más importantes (como “duración del video” - video duration, “conteo de me gusta del video” - video like count, “conteo de comentarios del video” - video comment count, y “conteo de vistas del video” - video view count) para verificar la presencia de valores atípicos u outliers. Además, incluye un desglose de los conteos del “estado de baneo del autor” (author ban status).

Adicionalmente, el equipo directivo ha solicitado recientemente que todo EDA incluya visualizaciones en Tableau. Las visualizaciones de Tableau son particularmente útiles en los informes de estado para el cliente y los miembros de la junta directiva. Para estos datos, crea un panel (dashboard) de Tableau que muestre un conteo simple de reclamaciones versus opiniones, así como gráficos de barras apiladas de reclamaciones versus opiniones para variables como el conteo de vistas del video, conteo de 'me gusta', conteo de veces compartido (video share counts) y conteo de descargas (video download counts). Asegúrate de que sea fácil de entender para alguien que no sea experto en datos, y recuerda que el subdirector es una persona con discapacidad visual.

También notarás un correo electrónico de seguimiento de la líder de ciencia de datos, Willow Jaffey. Willow sugiere incluir un resumen ejecutivo de tu análisis para compartirlo con tus compañeros de equipo.

Se estructuró y preparó un cuaderno para ayudarte en este proyecto. Por favor, completa las siguientes preguntas.

Proyecto de fin de curso del Curso 2: Análisis exploratorio de datos
En esta actividad, examinarás los datos proporcionados y los prepararás para el análisis. También diseñarás una visualización de datos profesional que cuente una historia y ayude a tomar decisiones basadas en datos para las necesidades del negocio.

Por favor, ten en cuenta que la actividad de visualización en Tableau es opcional y no afectará la finalización de tu curso. Completar la actividad de Tableau te ayudará a practicar la planificación y el trazado de una visualización de datos basada en una necesidad comercial específica. La estructura de esta actividad está diseñada para emular las propuestas que probablemente se te asignarán en tu carrera como profesional de datos. Completar esta actividad te ayudará a prepararte para esos momentos profesionales.  

El propósito de este proyecto es realizar un análisis exploratorio de datos en un conjunto de datos proporcionado. Tu misión es continuar la investigación que comenzaste en el Curso 1 (C1) y realizar más EDA en estos datos con el objetivo de conocer más sobre las variables. Es de especial interés la información relacionada con lo que distingue a los videos de reclamación (claim) de los videos de opinión (opinion).  

El objetivo es explorar el conjunto de datos y crear visualizaciones.

Esta actividad consta de 4 partes:

Parte 1: Importaciones, enlaces y carga

Parte 2: Exploración de datos e Ingeniería de datos (Limpieza de datos)

Parte 3: Construcción de visualizaciones

Parte 4: Evaluar y compartir resultados

Sigue las instrucciones y responde a la pregunta de abajo para completar la actividad. Luego, completarás un resumen ejecutivo utilizando las preguntas enumeradas en el Documento de Estrategia PACE.

Asegúrate de completar esta actividad antes de avanzar. El siguiente elemento del curso te proporcionará un modelo ejemplar completado para que lo compares con tu propio trabajo.


### 1. Importación de Librerías

```python
import numpy as ap
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt

# ==========================================
# 2. CARGA DE DATOS Y EXPLORACIÓN INICIAL
# ==========================================

# Lee el archivo CSV y lo transforma en un DataFrame (tabla estructurada) llamado 'data'
data = pd.read_csv("tiktok_dataset.csv")

# Muestra las primeras 5 filas para una inspección visual rápida de las columnas
data.head()

# Devuelve la cantidad total de celdas de datos (filas multiplicadas por columnas)
data.size

# Muestra las dimensiones exactas del dataset en formato (número de filas, número de columnas)
data.shape

# Imprime un resumen técnico: nombres de columnas, cantidad de datos no nulos y tipos de datos
data.info()

#El método describe()  proporciona un resumen estadístico de las columnas numéricas en un DataFrame. 
data.describe()

# Crea un gráfico de caja horizontal alargado (10x2) para analizar cómo se distribuye la duración de los videos.
# Sirve para identificar de un vistazo el rango central de los datos, la mediana y detectar la presencia de valores atípicos (outliers).
plt.figure(figsize=(10,2))
plt.title('Video Duration Sec')
sns.boxplot(data=None, x=data['video_duration_sec'], fliersize=1)
![alt text](image-5.png)

# Crea un histograma con barras detalladas de 1 en 1 segundo para analizar la frecuencia de la duración de los videos.
# Ayuda a identificar visualmente qué rangos de tiempo son los más comunes y si existen picos o patrones específicos.
plt.figure(figsize=(10,2))
plt.title('Histrogram of Video duration sec')
sns.histplot(data['video_duration_sec'], bins=range(0,26,1))


# Gráfico de caja (Boxplot) para analizar la distribución de vistas en los videos.
# Configura un lienzo alargado (10x2) con título, y reduce el tamaño de los
# puntos atípicos (fliersize=1) para mantener la visualización limpia y estilizada.
plt.figure(figsize=(10,2))
plt.title('video view count')
sns.boxplot(data=None, x=data['video_view_count'], fliersize=1)

# Histograma para analizar la frecuencia de las vistas de los videos.
# Configura un lienzo alargado (10x2) con título y agrupa los datos en barras (bins)
# de 1 en 1, desde 0 hasta 25 vistas, para ver exactamente cuántos videos caen en cada rango.
plt.figure(figsize=(10,2))
plt.title('Histogram video view count')
sns.histplot(data['video_view_count'], bins=range(0,26,1))

# Gráfico de caja (Boxplot) para analizar la distribución de los 'likes' en los videos.
# Configura el lienzo alargado (10x2) con su título, y mantiene los puntos atípicos 
# pequeños (fliersize=1) para identificar de forma limpia los videos con interacciones inusuales.
plt.figure(figsize=(10,2))
plt.title('video like count')
sns.boxplot(data=None, x=data['video_like_count'], fliersize=1)

# Histograma para analizar la frecuencia de los 'likes' en los videos.
# Configura el lienzo alargado (10x2) con su título y agrupa los likes en barras (bins)
# de 1 en 1, desde 0 hasta 25, para ver la cantidad exacta de videos que recibieron cada número de likes.
plt.figure(figsize=(10,2))
plt.title('Histogram video like count')
sns.histplot(data['video_like_count'], bins=range(0,26,1))

# Gráfico de caja (Boxplot) para analizar la distribución de comentarios en los videos.
# Configura el lienzo alargado (10x2) con título y usa 'fliersize=1' para que los 
# videos con ráfagas atípicas de comentarios no saturen la visualización.
plt.figure(figsize=(10,2))
plt.title('boxplot video comment count')
sns.boxplot(data=None, x=data['video_comment_count'], fliersize=1)

# Histograma para analizar la frecuencia de los comentarios en los videos.
# Configura el lienzo alargado (10x2) con título y agrupa los comentarios en barras
# de 1 en 1, desde 0 hasta 25, para evaluar el nivel exacto de conversación por video.
plt.figure(figsize=(10,2))
plt.title('Histogram video comment count')
sns.histplot(data['video_comment_count'], bins=range(0,26,1))

# Gráfico de caja (Boxplot) para analizar la distribución de las veces que se compartieron los videos.
# Configura el lienzo alargado (10x2) con título y usa 'fliersize=1' para compactar visualmente 
# los puntos de los videos que se volvieron extremadamente virales al ser compartidos.
plt.figure(figsize=(10,2))
plt.title(' boxplot video share count')
sns.boxplot(data=None, x=data['video_share_count'], fliersize=1)

# Histograma para analizar la frecuencia de las veces que se compartieron los videos.
# Configura el lienzo alargado (10x2) con título y agrupa las comparticiones en barras
# de 1 en 1, desde 0 hasta 25, para identificar con qué frecuencia la gente comparte el contenido.
plt.figure(figsize=(10,2))
plt.title('Histogram video share count')
sns.histplot(data['video_share_count'], bins=range(0,26,1) )

# Gráfico de caja (Boxplot) para analizar la distribución de las descargas de los videos.
# Configura el lienzo alargado (10x2) con título y usa 'fliersize=1' para mantener limpia 
# la visualización de los datos extremos donde los videos fueron descargados masivamente.
plt.figure(figsize=(10,2))
plt.title('Boxplot video download count')
sns.boxplot(data=None, x=data['video_download_count'], fliersize=1)

# Histograma para analizar la frecuencia de las descargas de los videos.
# Configura el lienzo alargado (10x2) con título y agrupa las descargas en barras
# de 1 en 1, desde 0 hasta 25, para ver qué tan común es que los usuarios guarden el contenido.
plt.figure(figsize=(10,2))
plt.title('Histogram video download count') # Nota: Se corrigió 'plt.figure' por 'plt.title' para que imprima el texto en la gráfica
sns.histplot(data['video_download_count'], bins=range(0,26,1))

# Gráfico de barras (Countplot) para contar la frecuencia de cada categoría en 'claim_status'.
# Configura un lienzo intermedio (8x4) con título y muestra de forma directa y visual
# cuántos videos pertenecen a cada estado de reclamación (por ejemplo: "reclamado" o "no reclamado").
plt.figure(figsize=(8,4))
plt.title('Histogram Claim status')
sns.countplot(x="claim_status", data=data)

# Gráfico de barras agrupado para cruzar el estado de reclamación con el estado del autor.
# Configura un lienzo alargado (10x2) y usa 'hue' para desglosar cada estado de reclamación 
# ('claim_status') mostrando cuántos autores están activos, baneados o bajo revisión.
plt.figure(figsize=(10,2))
plt.title('Claim Status by Author Ban Status')
sns.countplot(data=data, x='claim_status', hue='author_ban_status')

# Gráfico de barras que muestra la mediana de vistas según el estado de baneo del autor.
# 1. Agrupa los datos por 'author_ban_status' y calcula el valor central (mediana) de las vistas para cada grupo.
# 2. Configura un lienzo de 10x2, genera el gráfico con las categorías en X y los valores en Y, y etiqueta los ejes.
median_views = data.groupby('author_ban_status')['video_view_count'].median()
plt.figure(figsize=(10,2))
plt.title('Median View Counts by Author Ban Status')
sns.barplot(x=median_views.index, y=median_views.values)
plt.xlabel('Author Ban status')
plt.ylabel('Median view count')

# Gráfico de barras que muestra la mediana de vistas según el estado de reclamación del video.
# 1. Agrupa los datos por 'claim_status' y calcula el valor central (mediana) de las vistas para cada estado.
# 2. Configura un lienzo de 10x2, grafica las categorías frente a sus medianas y asigna etiquetas claras a los ejes.
median_views_clain = data.groupby('claim_status')['video_view_count'].median()
plt.figure(figsize=(10,2))
plt.title('Median vew counts by claim status')
sns.barplot(x=median_views_clain.index, y=median_views_clain.values)
plt.xlabel('claim status')
plt.ylabel('median view count')

# Gráfico de pastel (Pie chart) para analizar la proporción de vistas totales según el estado de reclamación.
# 1. Agrupa por 'claim_status' y suma todas las vistas ('video_view_count') de cada categoría.
# 2. Configura un lienzo cuadrado (66) e imprime el pastel mostrando los porcentajes con un decimal ('%1.1f%%'),
#    empezando a 90 grados y aplicando una paleta de colores personalizada (azul y rosa).
views_by_claim = data.groupby('claim_status')['video_view_count'].sum()
plt.figure(figsize=(6,6))
plt.title('Proportion of total view by claim status')
plt.pie(views_by_claim.values, labels=views_by_claim.index, autopct='%1.1f%%', startangle=90, colors=["#66b3ff","#ff9999"])

# Bucle 'for' para automatizar el conteo de valores atípicos (outliers) en las métricas principales.
# En cada iteración, calcula estadísticamente el Rango Intercuartílico (IQR), define un umbral adaptativo
# basado en la fórmula (mediana + 1.5 * IQR) y cuenta cuántos videos superan ese límite para cada columna.
count_colums = [
    'video_view_count',
    'video_like_count',
    'video_share_count',
    'video_download_count',
    'video_comment_count'
]

for col in count_colums:
    #calcular IQR
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    
    #calcular mediana
    median = data[col].median()
    
    #umbral de outlier ( median + 1.5 * IQR)
    threshold = median + 1.5 * IQR
    
    #contar cuantos valores superan el umbral
    outlier_count = (data[col] > threshold).sum()
    
    print(f'Number of outlers, {col}: {outlier_count}')



# Gráfico de dispersión (Scatterplot) para analizar la relación entre vistas y likes por estado de reclamación.
# Configura un lienzo balanceado (8x6) y dibuja puntos donde cada uno representa un video. 
# Usa 'hue' para colorear por 'claim_status' y 'alpha=0.6' para dar transparencia y ver la acumulación de datos.
plt.figure(figsize=(8,6))
plt.title('video views vs likes by claim status')
sns.scatterplot(data=data, x='video_view_count', y='video_like_count', hue='claim_status', alpha=0.6)

plt.xlabel('video view count')
plt.ylabel('video like count')


# Gráfico de dispersión (Scatterplot) exclusivo para videos categorizados como 'opinion'.
# Configura un lienzo (8x6) y filtra el DataFrame original en línea para mostrar solo la relación 
# vistas vs. likes de este subgrupo, pintando los puntos de naranja con transparencia (alpha=0.6).
plt.figure(figsize=(8,6))
plt.title('video views vs likes (opinion videos only)')

sns.scatterplot(data=data[data['claim_status'] == 'opinion'], x='video_view_count', y='video_like_count', color='orange', alpha=0.6)

plt.xlabel('video view count')
plt.ylabel('video like count')