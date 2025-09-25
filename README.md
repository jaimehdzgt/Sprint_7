# Sprint_7 — Análisis interactivo de anuncios de vehículos usados (Streamlit)

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Render-3fb950?logo=render)](https://sprint-7-8nqu.onrender.com)
[![Repositorio](https://img.shields.io/badge/GitHub-jaimehdzgt%2FSprint__7-24292e?logo=github)](https://github.com/jaimehdzgt/Sprint_7)

Aplicación web construida con **Streamlit** para explorar de forma interactiva un conjunto de datos de anuncios de vehículos usados en Estados Unidos. Permite realizar un análisis exploratorio rápido de variables clave (por ejemplo, `price`, `odometer`) y comparar su comportamiento por distintos atributos del dataset.

> **Objetivo**: acercar un EDA (Exploratory Data Analysis) a perfiles de negocio mediante una interfaz simple, filtros rápidos y visualizaciones inmediatas.

---

## ✨ Características

* **Carga y preprocesamiento** del dataset local (`vehicles_us.csv`).
* **Exploración interactiva** de variables numéricas clave (p. ej., precio y kilometraje).
* **Comparativas por categorías** (estado del título, tipo de combustible, transmisión, etc., según disponibilidad de columnas en el dataset).
* **Gráficas inmediatas** (distribuciones, tendencias y relaciones básicas) para responder preguntas comunes del negocio.
* **Tabla filtrable** para inspeccionar observaciones específicas.

> Nota: las visualizaciones exactas dependen de las columnas presentes en `vehicles_us.csv`. El objetivo es ofrecer una base sólida para EDA que puedas adaptar a tus necesidades.

---

## 🧩 Estructura del repositorio

```
Sprint_7/
├─ app.py                 # Punto de entrada de la app Streamlit
├─ requirements.txt       # Dependencias del proyecto
├─ vehicles_us.csv        # Dataset base (fuente: anuncios de autos usados en EE.UU.)
├─ notebooks/             # Cuadernos de experimentación/EDA
├─ streamlit/             # Recursos auxiliares para la interfaz (si aplica)
└─ .streamlit/            # Configuración de tema/layout de Streamlit (opcional)
```

---

## 🚀 Demo en producción

* **URL**: [https://sprint-7-8nqu.onrender.com](https://sprint-7-8nqu.onrender.com)
  Desplegado en **Render**. Si la app está “wake-sleep”, puede tardar unos segundos en activarse.

---

## 🛠️ Stack técnico

* **Python**
* **Streamlit** (UI)
* **Pandas / NumPy** (manejo de datos)
* (Opcional) **Altair / Plotly / Matplotlib** para visualizaciones, según las dependencias del proyecto.

---

## 📦 Instalación y ejecución local

> Requiere **Python 3.10+**.

```bash
# 1) Clona el repositorio
git clone https://github.com/jaimehdzgt/Sprint_7.git
cd Sprint_7

# 2) (Opcional) Crea y activa un entorno virtual
python -m venv .venv
# Windows
. .venv/Scripts/activate
# macOS / Linux
source .venv/bin/activate

# 3) Instala dependencias
pip install -r requirements.txt

# 4) Ejecuta la aplicación
streamlit run app.py
```

Por defecto, Streamlit abrirá el navegador en `http://localhost:8501`.

---

## 🗂️ Datos

* **Archivo**: `vehicles_us.csv`
* **Descripción**: dataset con anuncios de venta de vehículos en EE.UU. Incluye variables numéricas (p. ej., precio y odómetro) y categóricas (p. ej., tipo de combustible, transmisión, estado del título, etc.).
* **Tamaño y licencia**: ver archivo en el repositorio. Si vas a publicar/derivar, documenta claramente el **origen y la licencia** del dataset.

> Si modificas el nombre o ubicación del archivo, ajusta la ruta correspondiente en `app.py`.

---

## 🧭 Guía rápida de uso (en la app)

1. **Carga/lectura de datos**: la app lee `vehicles_us.csv` incluido en el repo.
2. **Panel lateral (sidebar)**: ajusta filtros (rango de precio/odómetro, selección de categorías) para segmentar los anuncios.
3. **Visualizaciones**: revisa distribuciones y relaciones clave para detectar patrones, outliers o segmentos con mejor relación precio/kilometraje.
4. **Tabla**: inspecciona filas específicas y, si lo deseas, exporta subconjuntos para análisis externo.

---

## 🏗️ Despliegue en Render (resumen)

1. Conecta tu repo a Render.
2. Crea un **Web Service** con:

   * **Runtime**: Python
   * **Build Command**: `pip install -r requirements.txt`
   * **Start Command**: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
3. Añade variables de entorno si tu app las requiere.
4. Despliega y prueba.

> Render puede hibernar servicios gratuitos tras inactividad; la primera visita puede tardar en “despertar”.

---

## 🧪 Notebooks

La carpeta `notebooks/` contiene cuadernos de trabajo (EDA, pruebas, limpieza). Úsalos para experimentar sin afectar la app productiva.

---

## 🗺️ Roadmap sugerido

* [ ] Documentar columnas del dataset y su diccionario de datos.
* [ ] Añadir pruebas de integridad de datos (duplicados, nulos, rangos válidos).
* [ ] Incorporar más visualizaciones (p. ej., precios por fabricante/modelo, dispersión precio‑año, boxplots por condiciones).
* [ ] Agregar opción de **descarga** de datos filtrados (CSV).
* [ ] Incluir **caché** de lectura y preprocesamiento para mejorar rendimiento.
* [ ] Dockerfile para despliegues reproducibles.

---

## 🤝 Contribuciones

¡Sugerencias y PRs son bienvenidos! Abre un **issue** para discutir cambios grandes.

---

## 📄 Licencia

Sin licencia explícita por ahora. Considera agregar una (p. ej., MIT) según tus necesidades.

---

## 📬 Contacto

* Autor: **Jaime Hernández**
* GitHub: [@jaimehdzgt](https://github.com/jaimehdzgt)
* LinkedIn / Correo:  https://www.linkedin.com/in/jaime-hdz/   /  jaime.hdz.gt@gmail.com




#https://sprint-7-8nqu.onrender.com
