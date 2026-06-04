# Proyecto TikTok
## Curso 2 - Ir más allá de los números: Traducir datos en información (Insights)

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


# PACE: Plan
Considera las preguntas en tu Documento de Estrategia PACE y las siguientes, cuando corresponda, para elaborar tu respuesta:

Identificar cualquier valor atípico:

### ¿Qué métodos son los mejores para identificar valores atípicos?
Usar medidas estadísticas como el rango intercuartílico (IQR), el Z‑score o visualizaciones como diagramas de caja.
### ¿Cómo tomas la decisión de conservar o excluir los valores atípicos de cualquier modelo futuro?
Depende del contexto: si reflejan un error o ruido, se excluyen; si representan casos reales y relevantes, se mantienen.

# Tarea 1. Importaciones, enlaces y carga  
Ve a Tableau Public. El siguiente enlace te ayudará a completar esta actividad. Mantén Tableau Public abierto mientras avanzas en los siguientes pasos.

Enlace a materiales de apoyo: Public Tableau: https://public.tableau.com/s/.
Ten en cuenta que el conjunto de datos de TikTok puede descargarse directamente desde este cuaderno yendo al menú superior en "Lab Files", entrando en la carpeta "/home/jovyan/work", seleccionando tiktok_dataset.csv y haciendo clic en "Download" encima de la lista de archivos.

Para el EDA de los datos, importa los paquetes más útiles, como:pandas,numpy, matplotlib.pyplot,seaborn

    import numpy as ap
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import datetime as dt

Luego, carga el conjunto de datos en un DataFrame. Lee los datos y guárdalos como un objeto DataFrame.
Lee el archivo CSV y lo transforma en un DataFrame (tabla estructurada) llamado 'data'

    data = pd.read_csv("tiktok_dataset.csv")

# PACE: Analyze¶  
Considera las preguntas en tu Documento de Estrategia PACE y las siguientes, cuando corresponda, para completar tu código.

## Tarea 2a: Exploración y limpieza de datos  
El primer paso es evaluar tus datos. Revisa la página de Data Source en Tableau Public para tener una idea del tamaño, la forma y la composición del conjunto de datos.

Considera funciones que te ayudan a entender y estructurar los datos:
Muestra las primeras 5 filas para una inspección visual rápida de las columnas
data.head()
.head()
.info()
.describe()
.groupby()
.sort_values()

Considera las siguientes preguntas mientras trabajas:

### ¿Qué haces con los datos faltantes (si los hay)?
Se imputan o eliminan según su impacto en el análisis.

### ¿Existen valores atípicos?
Sí, se detectan con métodos estadísticos y se decide mantenerlos o excluirlos según relevancia.

Comienza descubriendo, usando .head(), .size y .shape.

Devuelve la cantidad total de celdas de datos (filas multiplicadas por columnas)

    data.size

 Muestra las dimensiones exactas del dataset en formato (número de filas, número de columnas)

    data.shape

Imprime un resumen técnico: nombres de columnas, cantidad de datos no nulos y tipos de datos

    data.info()

El método describe()  proporciona un resumen estadístico de las columnas numéricas en un DataFrame.

    data.describe()

## Tarea 2b. Evaluar tipos de datos  
En Tableau, permaneciendo en la página de origen de datos, verifica dos veces los tipos de datos de las columnas en el conjunto de datos. Refiérete a las dimensiones y medidas en Tableau.

Revisa las instrucciones enlazadas en el documento de la Actividad anterior para crear la visualización requerida en Tableau.

## Tarea 2c. Seleccionar tipo(s) de visualización  
Selecciona los tipos de visualización de datos que te ayuden a entender y explicar la información.

Ahora que ya sabes qué columnas de datos vas a usar, es momento de decidir qué tipo de visualización tiene más sentido para el EDA del conjunto de datos de TikTok. ¿Qué tipo(s) de visualización serían más útiles? Considera la distribución de los datos.

Gráfico de líneas
Gráfico de barras
Diagrama de caja (box plot)
Histograma
Mapa de calor (heat map)
Diagrama de dispersión (scatter plot)
Mapa geográfico

# PACE: Construct
Considera las preguntas en tu Documento de Estrategia PACE para reflexionar sobre la etapa de Construcción.

## Tarea 3. Construir visualizaciones  
Ahora que has evaluado tus datos, es momento de graficar tus visualizaciones.

video_duration_sec  
Crea un diagrama de caja (box plot) para examinar la dispersión de los valores en la columna video_duration_sec.

    plt.figure(figsize=(10,2))
    plt.title('Video Duration Sec')
    sns.boxplot(data=None, x=data['video_duration_sec'], fliersize=1)
    ![alt text](image-5.png)
Crea un gráfico de caja horizontal alargado (10x2) para analizar cómo se distribuye la duración de los videos.
Sirve para identificar de un vistazo el rango central de los datos, la mediana y detectar la presencia de valores atípicos (outliers).

## Create a histogram

    plt.figure(figsize=(10,2))
    plt.title('Histrogram of Video duration sec')
    sns.histplot(data['video_duration_sec'], bins=range(0,26,1))
Crea un histograma con barras detalladas de 1 en 1 segundo para analizar la frecuencia de la duración de los videos.
Ayuda a identificar visualmente qué rangos de tiempo son los más comunes y si existen picos o patrones específicos.

### Pregunta: ¿Qué notas sobre la duración y distribución de los videos?
La distribución de los videos muestra que la mayoría tienen una duración corta, concentrándose en pocos segundos, y que la frecuencia disminuye a medida que aumenta la duración.

## video_view_count  
Crea un diagrama de caja para examinar la dispersión de los valores en la columna video_view_count.

    plt.figure(figsize=(10,2))
    plt.title('video view count')
    sns.boxplot(data=None, x=data['video_view_count'], fliersize=1)
Gráfico de caja (Boxplot) para analizar la distribución de vistas en los videos.
Configura un lienzo alargado (10x2) con título, y reduce el tamaño de los
puntos atípicos (fliersize=1) para mantener la visualización limpia y estilizada.

Crea un histograma de los valores en la columna video_view_count para explorar más a fondo la distribución de esta variable.

    plt.figure(figsize=(10,2))
    plt.title('Histogram video view count')
    sns.histplot(data['video_view_count'], bins=range(0,26,1))
Histograma para analizar la frecuencia de las vistas de los videos.
Configura un lienzo alargado (10x2) con título y agrupa los datos en barras (bins)
de 1 en 1, desde 0 hasta 25 vistas, para ver exactamente cuántos videos caen en cada rango.

### Pregunta: ¿Qué notas sobre la distribución de esta variable?
La distribución está muy sesgada, con muchos videos que tienen pocas visualizaciones y unos pocos con valores extremadamente altos. Esto indica la presencia de outliers y una concentración en el rango bajo.

## video_like_count
Crea un diagrama de caja para examinar la dispersión de los valores en la columna video_like_count.

    plt.figure(figsize=(10,2))
    plt.title('video like count')
    sns.boxplot(data=None, x=data['video_like_count'], fliersize=1)
Gráfico de caja (Boxplot) para analizar la distribución de los 'likes' en los videos.
Configura el lienzo alargado (10x2) con su título, y mantiene los puntos atípicos 
pequeños (fliersize=1) para identificar de forma limpia los videos con interacciones inusuales.

Crea un histograma de los valores en la columna video_like_count para explorar más a fondo la distribución de esta variable.

    plt.figure(figsize=(10,2))
    plt.title('Histogram video like count')
    sns.histplot(data['video_like_count'], bins=range(0,26,1))
Histograma para analizar la frecuencia de los 'likes' en los videos.
Configura el lienzo alargado (10x2) con su título y agrupa los likes en barras (bins)
de 1 en 1, desde 0 hasta 25, para ver la cantidad exacta de videos que recibieron cada número de likes.

### Pregunta: ¿Qué notas sobre la distribución de esta variable?
La distribución está asimétrica, con muchos valores bajos y unos pocos muy altos. Esto muestra concentración en el rango bajo y presencia de outliers que elevan la variabilidad.

## video_comment_count
Crea un diagrama de caja para examinar la dispersión de los valores en la columna video_comment_count.

    plt.figure(figsize=(10,2))
    plt.title('boxplot video comment count')
    sns.boxplot(data=None, x=data['video_comment_count'], fliersize=1)
Gráfico de caja (Boxplot) para analizar la distribución de comentarios en los videos.
Configura el lienzo alargado (10x2) con título y usa 'fliersize=1' para que los 
videos con ráfagas atípicas de comentarios no saturen la visualización.

Crea un histograma de los valores en la columna video_comment_count para explorar más a fondo la distribución de esta variable.

    plt.figure(figsize=(10,2))
    plt.title('Histogram video comment count')
    sns.histplot(data['video_comment_count'], bins=range(0,26,1))
Histograma para analizar la frecuencia de los comentarios en los videos.
Configura el lienzo alargado (10x2) con título y agrupa los comentarios en barras
de 1 en 1, desde 0 hasta 25, para evaluar el nivel exacto de conversación por video.

### Pregunta: ¿Qué notas sobre la distribución de esta variable?
La variable video_comment_count muestra una distribución muy sesgada: la mayoría de los videos tienen pocos comentarios, mientras que unos pocos alcanzan cifras muy altas. Esto indica concentración en valores bajos y presencia de outliers que representan videos con gran interacción.

## video_share_count
Crea un diagrama de caja para examinar la dispersión de los valores en la columna video_share_count.

    plt.figure(figsize=(10,2))
    plt.title(' boxplot video share count')
    sns.boxplot(data=None, x=data['video_share_count'], fliersize=1)
Gráfico de caja (Boxplot) para analizar la distribución de las veces que se compartieron los videos.
Configura el lienzo alargado (10x2) con título y usa 'fliersize=1' para compactar visualmente 
los puntos de los videos que se volvieron extremadamente virales al ser compartidos.

Crea un histograma de los valores en la columna video_share_count para explorar más a fondo la distribución de esta variable.

    plt.figure(figsize=(10,2))
    plt.title('Histogram video share count')
    sns.histplot(data['video_share_count'], bins=range(0,26,1) )
Histograma para analizar la frecuencia de las veces que se compartieron los videos.
Configura el lienzo alargado (10x2) con título y agrupa las comparticiones en barras
de 1 en 1, desde 0 hasta 25, para identificar con qué frecuencia la gente comparte el contenido.

### Pregunta: ¿Qué notas sobre la distribución de esta variable?
La variable video_share_count presenta una distribución desbalanceada: la mayoría de los videos tienen muy pocas veces que fueron compartidos, mientras que unos pocos alcanzan números muy altos. Esto refleja un patrón sesgado hacia valores bajos, con presencia de outliers que representan videos con gran viralidad.

## video_download_count
Crea un diagrama de caja para examinar la dispersión de los valores en la columna video_download_count

    plt.figure(figsize=(10,2))
    plt.title('Boxplot video download count')
    sns.boxplot(data=None, x=data['video_download_count'], fliersize=1)
Gráfico de caja (Boxplot) para analizar la distribución de las descargas de los videos.
Configura el lienzo alargado (10x2) con título y usa 'fliersize=1' para mantener limpia 
la visualización de los datos extremos donde los videos fueron descargados masivamente.

Crea un histograma de los valores en la columna video_download_count para explorar más a fondo la distribución de esta variable.

    plt.figure(figsize=(10,2))
    plt.title('Histogram video download count') # Nota: Se corrigió 'plt.figure' por 'plt.title' para que imprima el texto en la gráfica
    sns.histplot(data['video_download_count'], bins=range(0,26,1))
Histograma para analizar la frecuencia de las descargas de los videos.
Configura el lienzo alargado (10x2) con título y agrupa las descargas en barras
de 1 en 1, desde 0 hasta 25, para ver qué tan común es que los usuarios guarden el contenido.

### Pregunta: ¿Qué notas sobre la distribución de esta variable?
La variable video_download_count muestra una distribución concentrada en valores bajos: la mayoría de los videos tienen pocas descargas, mientras que unos pocos alcanzan cifras muy altas. Esto refleja un patrón sesgado hacia la baja frecuencia, con presencia de outliers que representan videos con gran popularidad o demanda

## Estado de reclamo por estado de verificación  
Ahora, crea un histograma con cuatro barras: una para cada combinación de estado de reclamo y estado de verificación.

    plt.figure(figsize=(8,4))
    plt.title('Histogram Claim status')
    sns.countplot(x="claim_status", data=data)
Gráfico de barras (Countplot) para contar la frecuencia de cada categoría en 'claim_status'.
Configura un lienzo intermedio (8x4) con título y muestra de forma directa y visual
cuántos videos pertenecen a cada estado de reclamación (por ejemplo: "reclamado" o "no reclamado").

### Pregunta: ¿Qué notas sobre el número de usuarios verificados en comparación con los no verificados? ¿Y cómo afecta eso a su probabilidad de publicar opiniones?
Hay menos usuarios verificados que no verificados. Los no verificados tienden a publicar más opiniones, mientras que los verificados muestran menor frecuencia en este tipo de publicaciones. Esto sugiere que la verificación está asociada con un comportamiento más moderado en la generación de contenido de opinión.

## Estado de reclamo según estado de baneo del autor  
El curso anterior utilizó una instrucción groupby() para examinar el conteo de cada estado de reclamo para cada estado de baneo del autor. Ahora, usa un histograma para comunicar la misma información.

    plt.figure(figsize=(10,2))
    plt.title('Claim Status by Author Ban Status')
    sns.countplot(data=data, x='claim_status', hue='author_ban_status')
Gráfico de barras agrupado para cruzar el estado de reclamación con el estado del autor.
Configura un lienzo alargado (10x2) y usa 'hue' para desglosar cada estado de reclamación 
('claim_status') mostrando cuántos autores están activos, baneados o bajo revisión.

### Pregunta: ¿Qué notas sobre el número de autores activos en comparación con los autores baneados tanto para reclamos como para opiniones?
Los autores activos superan claramente a los baneados en ambos tipos de contenido. En los reclamos, la diferencia es muy marcada: la mayoría proviene de autores activos y los baneados apenas aportan. En las opiniones, también predominan los activos, aunque los baneados tienen una presencia algo mayor que en los reclamos, pero siguen siendo minoría.
En síntesis, la participación está dominada por los autores activos, lo que muestra que el baneo limita bastante la generación de contenido.

## Mediana de vistas según estado de baneo  
Crea un gráfico de barras con tres barras: una para cada estado de baneo del autor. La altura de cada barra debe corresponder con la mediana del número de vistas de todos los videos con ese estado de baneo del autor.

    median_views = data.groupby('author_ban_status')['video_view_count'].median()
    plt.figure(figsize=(10,2))
    plt.title('Median View Counts by Author Ban Status')
    sns.barplot(x=median_views.index, y=median_views.values)
    plt.xlabel('Author Ban status')
    plt.ylabel('Median view count')
Gráfico de barras que muestra la mediana de vistas según el estado de baneo del autor.
1. Agrupa los datos por 'author_ban_status' y calcula el valor central (mediana) de las vistas para cada grupo.
2. Configura un lienzo de 10x2, genera el gráfico con las categorías en X y los valores en Y, y etiqueta los ejes.

### Pregunta: ¿Qué notas sobre la mediana de vistas de los autores no activos en comparación con la de los autores activos? Con base en ese hallazgo, ¿qué variable podría ser un buen indicador del estado de reclamo?
La mediana de vistas de los autores no activos suele ser más baja que la de los autores activos, lo que refleja que los activos generan contenido con mayor alcance. A partir de esa diferencia, el estado de baneo del autor podría ser una buena variable para indicar o predecir el estado de reclamo

    median_views_clain = data.groupby('claim_status')['video_view_count'].median()
    plt.figure(figsize=(10,2))
    plt.title('Median vew counts by claim status')
    sns.barplot(x=median_views_clain.index, y=median_views_clain.values)
    plt.xlabel('claim status')
    plt.ylabel('median view count')
Gráfico de barras que muestra la mediana de vistas según el estado de reclamación del video.
1. Agrupa los datos por 'claim_status' y calcula el valor central (mediana) de las vistas para cada estado.
2. Configura un lienzo de 10x2, grafica las categorías frente a sus medianas y asigna etiquetas claras a los ejes.

## Vistas totales según estado de reclamo  
Crea un gráfico de pastel que represente las proporciones de vistas totales para los videos de reclamos y las vistas totales para los videos de opiniones.

    views_by_claim = data.groupby('claim_status')['video_view_count'].sum()
    plt.figure(figsize=(6,6))
    plt.title('Proportion of total view by claim status')
    plt.pie(views_by_claim.values, labels=views_by_claim.index, autopct='%1.1f%%', startangle=90, colors=["#66b3ff","#ff9999"])
Gráfico de pastel (Pie chart) para analizar la proporción de vistas totales según el estado de reclamación.
1. Agrupa por 'claim_status' y suma todas las vistas ('video_view_count') de cada categoría.
2. Configura un lienzo cuadrado (66) e imprime el pastel mostrando los porcentajes con un decimal ('%1.1f%%'),
empezando a 90 grados y aplicando una paleta de colores personalizada (azul y rosa).

### Pregunta: ¿Qué notas sobre el conteo total de vistas según el estado de reclamo?  
Los videos con estado de reclamo concentran la gran mayoría de las vistas, mientras que los videos de opinión

# Tarea 4. Determinar valores atípicos (outliers)  
Al construir modelos predictivos, la presencia de valores atípicos puede ser problemática. Por ejemplo, si intentaras predecir el número de vistas de un video en particular, los videos con un número extremadamente alto de vistas podrían introducir sesgos en el modelo. Además, algunos outliers podrían indicar problemas en la captura o el registro de los datos.

El objetivo final del proyecto de TikTok es construir un modelo que prediga si un video es un reclamo o una opinión. El análisis realizado indica que el nivel de interacción de un video está fuertemente correlacionado con su estado de reclamo. No hay razón para creer que los valores en los datos de TikTok hayan sido capturados erróneamente, y se alinean con lo esperado en redes sociales: una pequeña proporción de videos obtiene niveles de interacción muy altos. Esa es la naturaleza del contenido viral.

No obstante, es buena práctica identificar cuántos de tus datos podrían considerarse outliers. La definición de un outlier puede variar según los detalles del proyecto, y ayuda contar con conocimiento del dominio para decidir un umbral. Has aprendido que una forma común de determinar outliers en una distribución normal es calcular el rango intercuartílico (IQR) y establecer un umbral de 1.5 * IQR por encima del tercer cuartil.

En este conjunto de datos de TikTok, los valores de las variables de conteo no siguen una distribución normal, sino que están fuertemente sesgados hacia la derecha. Una forma de modificar el umbral de outliers es calcular la mediana de cada variable y luego sumar 1.5 * IQR. Esto da como resultado un umbral mucho más bajo que si se usara el tercer cuartil.

Escribe un bucle for que itere sobre los nombres de las columnas de cada variable de conteo. En cada iteración:

Calcula el IQR de la columna
Calcula la mediana de la columna
Calcula el umbral de outliers (mediana + 1.5 * IQR)
Calcula el número de videos cuyo conteo en esa columna excede el umbral
Imprime: "Número de outliers, {nombre_columna}: {conteo_outliers}"

Ejemplo:
Número de outliers, video_view_count: ___
Número de outliers, video_like_count: ___
Número de outliers, video_share_count: ___
Número de outliers, video_download_count: ___
Número de outliers, video_comment_count: ___

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
Bucle 'for' para automatizar el conteo de valores atípicos (outliers) en las métricas principales.
En cada iteración, calcula estadísticamente el Rango Intercuartílico (IQR), define un umbral adaptativo
basado en la fórmula (mediana + 1.5 * IQR) y cuenta cuántos videos superan ese límite para cada columna.

## Scatterplot
### Crear un diagrama de dispersión de video_view_count versus video_like_count según claim_status

    plt.figure(figsize=(8,6))
    plt.title('video views vs likes by claim status')
    sns.scatterplot(data=data, x='video_view_count', y='video_like_count', hue='claim_status', alpha=0.6)

    plt.xlabel('video view count')
    plt.ylabel('video like count')
Gráfico de dispersión (Scatterplot) para analizar la relación entre vistas y likes por estado de reclamación.
Configura un lienzo balanceado (8x6) y dibuja puntos donde cada uno representa un video. 
Usa 'hue' para colorear por 'claim_status' y 'alpha=0.6' para dar transparencia y ver la acumulación de datos.

### Crear un diagrama de dispersión de video_view_count versus video_like_count

    plt.figure(figsize=(8,6))
    plt.title('video views vs likes (opinion videos only)')

    sns.scatterplot(data=data[data['claim_status'] == 'opinion'], x='video_view_count', y='video_like_count', color='orange', alpha=0.6)

    plt.xlabel('video view count')
    plt.ylabel('video like count')
Gráfico de dispersión (Scatterplot) exclusivo para videos categorizados como 'opinion'.
Configura un lienzo (8x6) y filtra el DataFrame original en línea para mostrar solo la relación 
vistas vs. likes de este subgrupo, pintando los puntos de naranja con transparencia (alpha=0.6).

# PACE: Ejecutar  
Considera las preguntas en tu Documento de Estrategia PACE para reflexionar sobre la etapa de Ejecución.

## Tarea 5a. Resultados y evaluación  
Habiendo construido visualizaciones en Tableau y en Python, ¿qué has aprendido sobre el conjunto de datos? ¿Qué otras preguntas han surgido a partir de tus visualizaciones que deberías investigar?

Consejo profesional: Ponte en la perspectiva de tu cliente, ¿qué querría saber?

Usa las siguientes celdas de código para realizar cualquier análisis exploratorio adicional (EDA). También utiliza este espacio para asegurarte de que tus visualizaciones sean claras, fáciles de entender y accesibles.

Pregúntate: ¿Consideraste el color, el contraste, el énfasis y el etiquetado?

A partir de las visualizaciones en Tableau y Python, se pueden destacar varios aprendizajes:

El conjunto de datos muestra una clara relación entre el estado de reclamo y el nivel de interacción (vistas, likes, comentarios).

Los videos de reclamos tienden a concentrar más vistas y participación que los de opinión, lo que confirma su mayor alcance.

Se observa una distribución sesgada en las variables de conteo, con algunos valores extremos que representan contenido viral.

Además, las visualizaciones abren nuevas preguntas:

¿Qué factores adicionales, como la duración del video o el estado de verificación del autor, influyen en el nivel de interacción?

¿Existen patrones temporales (por ejemplo, fechas de publicación) que afecten la probabilidad de que un video sea reclamo u opinión?

Finalmente, es importante cuidar la presentación visual: usar colores contrastantes para diferenciar categorías, etiquetas claras en los ejes y títulos descriptivos que faciliten la interpretación. Esto asegura que el cliente pueda comprender rápidamente los hallazgos y tomar decisiones basadas en ellos.