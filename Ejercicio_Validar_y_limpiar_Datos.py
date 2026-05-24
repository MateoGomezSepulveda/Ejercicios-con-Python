import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# sirve para cargar un archivo CSV llamado 'data.csv' en un DataFrame de pandas llamado 'df'

pd.set_option('display.max_columns', None)
# establece la opción de pandas para mostrar todas las columnas del DataFrame sin truncar, lo

companies = pd.read_csv('data.csv')
# sirve para cargar un archivo CSV llamado 'data.csv' en un DataFrame de pandas llamado 'companies'

companies.head()
# muestra las primeras filas del DataFrame 'companies' utilizando el método head(), lo que permite obtener una vista previa de los datos y verificar su estructura y contenido.

#DATA CLEANING
print(companies.dtypes)
# muestra los tipos de datos de cada columna en el DataFrame 'companies' utilizando el atributo 'dtypes', lo que ayuda a identificar el tipo de datos de cada columna y verificar si es necesario realizar alguna conversión o limpieza de datos.

#MODIFY THE DATA TYPES
companies['Date Joined'] = pd.to_datetime(companies['Date Joined'])
# convierte la columna 'Date Joined' del DataFrame 'companies' en un objeto de tipo datetime utilizando la función pd.to_datetime, lo que permite realizar operaciones y análisis relacionados con fechas de manera más eficiente y precisa.

#CREATE A NEW COLUMN
companies['Year Joined'] = companies['Date Joined'].dt.year - companies['Year Founded']
# crea una nueva columna 'Year Joined' en el DataFrame 'companies' que calcula la diferencia entre el año de la columna 'Date Joined' y el año de la columna 'Year Founded', lo que puede proporcionar información sobre el tiempo que ha pasado desde que una empresa fue fundada hasta que se unió a la plataforma o servicio.

#INPUT VALIDATION
companies['Years To Unicorn'].describe()
# muestra un resumen estadístico de la columna 'Years To Unicorn' del DataFrame 'companies

companies[companies['Years To Unicorn'] < 0]
# filtra el DataFrame 'companies' para mostrar solo las filas donde los valores de la columna 'Years To Unicorn' son menores que 0, lo que puede ayudar a identificar posibles errores o valores atípicos en los datos relacionados con el tiempo que tarda una empresa en convertirse en un unicornio.

# Replace InVision's `Year Founded` value with 2011
companies.loc[companies['Company'] == 'InVision', 'Year Founded'] = 2011
# utiliza el método loc para localizar la fila del DataFrame 'companies' donde la columna 'Company' es igual a 'InVision', y luego asigna el valor 2011 a la columna 'Year Founded' para esa fila, lo que corrige el valor de año de fundación para la empresa InVision en el conjunto de datos.

# Verify the change was made properly
companies[companies['Company'] == 'Invision']
# filtra el DataFrame 'companies' para mostrar solo las filas donde la columna 'Company' es igual a 'InVision', lo que permite verificar si el cambio realizado en la columna 'Year Founded' para la empresa InVision se ha aplicado correctamente.

# Recalculate all values in the `Years To Unicorn` column
companies['Years To Unicorn'] = companies['Date Joined'].dt.year - companies['Year Founded']
# recalcula los valores de la columna 'Years To Unicorn' en el DataFrame 'companies' restando el año de la columna 'Year Founded' del año de la columna 'Date Joined', lo que actualiza los valores en esa columna después de corregir el año de fundación para la empresa InVision.

# Verify that there are no more negative values in the column
companies['Years To Unicorn'].describe()
# muestra un resumen estadístico de la columna 'Years To Unicorn' del DataFrame 'companies' después de recalcular los valores, lo que permite verificar si ya no hay valores negativos en esa columna y obtener información sobre la distribución de los datos.

#List provided by the company of the expected industry labels in the data
industry_list = ['Artificial intelligence', 'Other','E-commerce & direct-to-consumer', 'Fintech',\
       'Internet software & services','Supply chain, logistics, & delivery', 'Consumer & retail',\
       'Data management & analytics', 'Edtech', 'Health', 'Hardware','Auto & transportation', \
        'Travel', 'Cybersecurity','Mobile & telecommunications']
# crea una lista llamada 'industry_list' que contiene los nombres de las etiquetas de industria esperadas en los datos, lo que puede ser útil para validar y limpiar los datos relacionados con la industria de las empresas en el DataFrame 'companies'.


# Check which values are in `Industry` but not in `industry_list`
set(companies['Industry']) - set(industry_list)
# utiliza la función set para crear conjuntos a partir de la columna 'Industry' del DataFrame 'companies' y la lista 'industry_list', y luego realiza una operación de diferencia entre los dos conjuntos para identificar qué valores están presentes en la columna 'Industry' pero no están en la lista 'industry_list', lo que puede ayudar a identificar posibles errores o valores atípicos en los datos relacionados con la industria de las empresas.

# 1. Create `replacement_dict`
replacement_dict = {'Artificial Intelligence': 'Artificial intelligence',
                   'Data management and analytics': 'Data management & analytics',
                   'FinTech': 'Fintech'
                   }
# crea un diccionario llamado 'replacement_dict' que mapea los valores incorrectos o inconsistentes en la columna 'Industry' del DataFrame 'companies' a los valores correctos o consistentes que se encuentran en la lista 'industry_list', lo que puede ser útil para reemplazar los valores incorrectos en la columna 'Industry' y limpiar los datos relacionados con la industria de las empresas.

# 2. Replace the incorrect values in the `Industry` column
companies['Industry'] = companies['Industry'].replace(replacement_dict)
# utiliza el método replace para reemplazar los valores incorrectos en la columna 'Industry' del DataFrame 'companies' utilizando el diccionario 'replacement_dict', lo que actualiza los valores en esa columna para que sean consistentes con la lista de etiquetas de industria esperadas.


# 3. Verify that there are no longer any elements in `Industry` that are not in `industry_list`
set(companies['Industry']) - set(industry_list)
# utiliza la función set para crear conjuntos a partir de la columna 'Industry' del DataFrame 'companies' y la lista 'industry_list', y luego realiza una operación de diferencia entre los dos conjuntos para verificar que ya no hay valores en la columna 'Industry' que no estén en la lista 'industry_list', lo que confirma que los valores incorrectos han sido reemplazados correctamente.


# Isolate rows of all companies that have duplicates
companies[companies.duplicated(subset=['Company'], keep=False)]
# utiliza el método duplicated para identificar filas duplicadas en el DataFrame 'companies' basándose en la columna 'Company', y luego filtra el DataFrame para mostrar solo las filas que tienen duplicados utilizando el argumento keep=False, lo que puede ayudar a identificar posibles problemas de duplicación en los datos relacionados con las empresas.

# Drop rows of duplicate companies after their first occurrence
companies = companies.drop_duplicates(subset=['Company'], keep='first')
# utiliza el método drop_duplicates para eliminar las filas duplicadas en el DataFrame 'companies' basándose en la columna 'Company', manteniendo solo la primera ocurrencia de cada empresa utilizando el argumento keep='first', lo que ayuda a limpiar los datos eliminando las filas duplicadas relacionadas con las empresas.

# Create new `High Valuation` column
companies['High Valuation'] = pd.qcut(companies['Valuation'], 2, labels = ['low', 'high'])
# crea una nueva columna 'High Valuation' en el DataFrame 'companies' que categoriza los valores de la columna 'Valuation' en dos grupos utilizando la función pd.qcut, asignando las etiquetas 'low' y 'high' a cada grupo, lo que puede ser útil para analizar y comparar las empresas según su valoración.

# Rank the continents by number of unicorn companies
companies['Continent'].value_counts()
# utiliza el método value_counts para contar la cantidad de empresas unicornio en cada continente según la columna 'Continent' del DataFrame 'companies', lo que permite clasificar los continentes según el número de empresas unicornio que tienen.

# Create numeric `Continent Number` column
continent_dict = {'North America': 1,
                  'Asia': 2,
                  'Europe': 3,
                  'South America': 4,
                  'Oceania': 5,
                  'Africa': 6
                 }
companies['Continent Number'] = companies['Continent'].replace(continent_dict)
companies.head()
# crea una nueva columna 'Continent Number' en el DataFrame 'companies' que asigna un número a cada continente utilizando un diccionario de mapeo llamado 'continent_dict', lo que puede ser útil para convertir la columna 'Continent' en una representación numérica que facilite el análisis y la visualización de los datos relacionados con los continentes de las empresas unicornio. Luego se muestra las primeras filas del DataFrame actualizado utilizando el método head() para verificar los cambios realizados.

# Create `Country/Region Numeric` column
# Create numeric categories for Country/Region
companies['Country/Region Numeric'] = companies['Country/Region'].astype('category').cat.codes
# crea una nueva columna 'Country/Region Numeric' en el DataFrame 'companies' que asigna un código numérico a cada categoría única en la columna 'Country/Region' utilizando el método astype('category') para convertir la columna en una categoría y luego accediendo al atributo cat.codes para obtener los códigos numéricos correspondientes, lo que puede ser útil para convertir la columna 'Country/Region' en una representación numérica que facilite el análisis y la visualización de los datos relacionados con los países o regiones de las empresas unicornio.



# Convert `Industry` to numeric data
# Create dummy variables with Industry values
industry_encoded = pd.get_dummies(companies['Industry'])
# crea un nuevo DataFrame llamado 'industry_encoded' que contiene variables dummy para cada categoría única en la columna 'Industry' del DataFrame 'companies' utilizando la función pd.get_dummies, lo que convierte la columna 'Industry' en una representación numérica con columnas separadas para cada categoría de industria.

# Combine `companies` DataFrame with new dummy Industry columns
companies = pd.concat([companies, industry_encoded], axis=1)
# combina el DataFrame original 'companies' con el nuevo DataFrame 'industry_encoded' que contiene las variables dummy para la columna 'Industry' utilizando la función pd.concat, especificando axis=1 para concatenar las columnas, lo que agrega las nuevas columnas de variables dummy al DataFrame 'companies' para facilitar el análisis y la visualización de los datos relacionados con las industrias de las empresas unicornio.

companies.head()
# muestra las primeras filas del DataFrame 'companies' después de agregar las nuevas columnas de variables dummy para la columna 'Industry', lo que permite verificar los cambios realizados y obtener una vista previa de los datos actualizados.