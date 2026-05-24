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
(image.png)

# Devuelve la cantidad total de celdas de datos (filas multiplicadas por columnas)
data.size
(image-1.png)
# Muestra las dimensiones exactas del dataset en formato (número de filas, número de columnas)
data.shape

# Imprime un resumen técnico: nombres de columnas, cantidad de datos no nulos y tipos de datos
data.info()


