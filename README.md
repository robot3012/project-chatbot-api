# Chatbot API

Este proyecto es una API de chatbot construida con FastAPI y TensorFlow. El chatbot está diseñado para responder preguntas sobre seguros utilizando un modelo de aprendizaje automático.

## Estructura del Proyecto

- **`main.py`**: Define la API con FastAPI.
- **`model.py`**: Contiene funciones para cargar y preprocesar el modelo y el tokenizador.
- **`data.py`**: Funciones para cargar y dividir datos.
- **`requirements.txt`**: Lista de dependencias del proyecto.
- **`Dockerfile`**: Define el entorno de Docker para el proyecto.
- **`datos.txt`**: Archivo de datos de entrenamiento (preguntas y respuestas).

## Instalación

Para instalar y configurar el proyecto localmente:

1. **Clona el repositorio:**

  ```bash
   git clone <URL-del-repositorio>
   cd <nombre-del-repositorio>
  ```

2. **Crea un entorno virtual (opcional pero recomendado):**

  ```bash
  python -m venv venv
  source venv/bin/activate  # En Windows usa: venv\Scripts\activate
  ```
3. **Instala las dependencias:**

  ```bash
  pip install -r requirements.txt
  ```
4. **Entrena el modelo (si es necesario):**

Asegúrate de tener el archivo datos.txt en la raíz del proyecto. Luego ejecuta el script de entrenamiento (ajusta el nombre del archivo si es diferente):

  ```bash
  python trainer.py
  ```
## Uso

1. **Inicia el servidor FastAPI:**

  ```bash
  uvicorn main:app --host 0.0.0.0 --port 8000
  ```
Si estás en un entorno de desarrollo y deseas que el servidor se reinicie automáticamente con los cambios en el código, puedes usar --reload:

  ```bash
  uvicorn main:app --host 0.0.0.0 --port 8000 --reload
  ```
2. **Accede a la API:**
   
Abre tu navegador web y visita http://localhost:8000/docs para ver la documentación interactiva de la API generada por FastAPI. Aquí podrás probar el endpoint /consultar/.

## Despliegue con Docker

1. **Construye la imagen Docker:**

  ```bash
  docker build -t chatbot-api .
  ```
2. **Ejecuta el contenedor Docker:**

Para el desarrollo con recarga automática, usa:

  ```bash
  docker run -p 8000:8000 -v "$(pwd)":/app chatbot-api uvicorn main:app --host 0.0.0.0 --port 8000 --reload
  ```
Para producción (sin recarga automática), usa:

  ```bash
  docker run -p 8000:8000 chatbot-api
  ```
