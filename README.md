# Ejercicio: Validar y Limpiar Datos (Unicorn Companies)

Este README describe el archivo `Ejercicio_Validar_y_limpiar_Datos.py`, el flujo de limpieza de datos y los detalles de cada bloque de código, manteniendo los comentarios existentes y mejorando la comprensión general.

## 🧩 Propósito

- Cargar el dataset `data.csv` de empresas unicornio.
- Revisar tipos y valores atípicos.
- Corregir y normalizar columnas clave (fechas, industrias y duplicados).
- Agregar variables derivadas y transformaciones (categorías numéricas, dummies).
- Preparar datos para análisis posterior.

## 📦 Dependencias

- Python 3.8+
- numpy
- pandas
- seaborn
- matplotlib

Instalación recomendada (por ejemplo con pip):

```bash
pip install numpy pandas seaborn matplotlib
```

## 📁 Ruta del archivo principal

- `Curso Aalityc Datos/Ejercicio_Validar_y_limpiar_Datos.py`

## 🔍 Descripción paso a paso

### 1. Importaciones y configuración de pandas

```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
```

- Se importan librerías comunes para análisis y visualización.
- `pd.set_option('display.max_columns', None)` evita truncado de columnas en la salida.

### 2. Carga del CSV y vista inicial

```python
companies = pd.read_csv('data.csv')
companies.head()
```

- `data.csv` se carga en `companies`.
- `head()` muestra las primeras filas para verificar estructura.

### 3. Revisión de tipos de datos

```python
print(companies.dtypes)
```

- Revisar tipos para detectar si alguna columna necesita conversión antes de operaciones posteriores.

### 4. Conversión de fecha y columna derivada

```python
companies['Date Joined'] = pd.to_datetime(companies['Date Joined'])
companies['Year Joined'] = companies['Date Joined'].dt.year - companies['Year Founded']
```

- Convierto `Date Joined` a datetime.
- Creo `Year Joined` como años transcurridos desde la fundación hasta el join.

### 5. Validación de `Years To Unicorn`

```python
companies['Years To Unicorn'].describe()
companies[companies['Years To Unicorn'] < 0]
```

- Analizo estadísticas de `Years To Unicorn`.
- Identifico registros negativos, que son inconsistencias de datos.

### 6. Corrección puntual (InVision)

```python
companies.loc[companies['Company'] == 'InVision', 'Year Founded'] = 2011
companies[companies['Company'] == 'Invision']
```

- Se corrige dato incorrecto `Year Founded` para InVision (capitalización de nombre se revisa).
- Verificación de la fila modificada.

### 7. Recalcular `Years To Unicorn` y revalidar

```python
companies['Years To Unicorn'] = companies['Date Joined'].dt.year - companies['Year Founded']
companies['Years To Unicorn'].describe()
```

- Ajuste de valores una vez corregido `Year Founded`.
- Revisión estadística tras la recomputación.

### 8. Normalizar valores de `Industry`

```python
industry_list = ['Artificial intelligence', 'Other', 'E-commerce & direct-to-consumer', 'Fintech', ...]
set(companies['Industry']) - set(industry_list)

replacement_dict = {
  'Artificial Intelligence': 'Artificial intelligence',
  'Data management and analytics': 'Data management & analytics',
  'FinTech': 'Fintech'
}

companies['Industry'] = companies['Industry'].replace(replacement_dict)
set(companies['Industry']) - set(industry_list)
```

- Se define lista de industrias oficiales y se comparan valores actuales.
- Se crea `replacement_dict` para corregir inconsistencias.
- Se reemplazan valores y se vuelve a validar que el conjunto quede limpio.

### 9. Eliminación de duplicados

```python
companies[companies.duplicated(subset=['Company'], keep=False)]
companies = companies.drop_duplicates(subset=['Company'], keep='first')
```

- Identifica compañías repetidas.
- Mantiene solo la primera ocurrencia.

### 10. Variable `High Valuation`

```python
companies['High Valuation'] = pd.qcut(companies['Valuation'], 2, labels=['low', 'high'])
```

- Se crea categoría con cuantiles según valuación (`low`/`high`).

### 11. Conteo por continente

```python
companies['Continent'].value_counts()
```

- Se genera ranking de continuidad por cantidad de empresas.

### 12. Atlas numérico de continente y país

```python
continent_dict = {'North America': 1, 'Asia': 2, 'Europe': 3, 'South America': 4, 'Oceania': 5, 'Africa': 6}
companies['Continent Number'] = companies['Continent'].replace(continent_dict)
companies['Country/Region Numeric'] = companies['Country/Region'].astype('category').cat.codes
```

- `Continent Number`: mapea cada continente con un código numérico.
- `Country/Region Numeric`: convierte cada país/región a código categórico.

### 13. Industria a dummies (one-hot)

```python
industry_encoded = pd.get_dummies(companies['Industry'])
companies = pd.concat([companies, industry_encoded], axis=1)
companies.head()
```

- One-hot encoding para `Industry`.
- Concatenación de nuevas columnas en `companies`.

## 📌 Observaciones / Buenas prácticas

- No se sobrescribe el archivo original CSV; el DataFrame en memoria guarda los cambios.
- La variable `companies.head()` no altera datos, solo muestra vista previa.
- Para persistir resultados, guardar con `companies.to_csv('data_limpia.csv', index=False)` (no incluido en el original).
- Incluir controles extra si hay `NaN` en columnas clave (`Year Founded`, `Date Joined`, `Valuation`).

## ✅ Cómo ejecutar

1. Sitúate en la carpeta `Curso Aalityc Datos`.
2. Asegura `data.csv` en el mismo directorio.
3. Ejecuta:

```bash
python Ejercicio_Validar_y_limpiar_Datos.py
```

> Nota: el script actual no imprime resultados finales, solo llamas a métodos de inspección. Añade `print(companies.head())` o graficas con `seaborn` si quieres visualización permanente.

---

📘 Con este README quedará bien documentado tu ejercicio y será fácil revisar la lógica de datos paso a paso.