# Cuchara App

Cuchara App es una aplicación web desarrollada en **Django** que permite a las empresas registrar sus restaurantes y subir sus menús. Estos menús se almacenan en **Azure Blob Storage**, se indexan con **Azure AI Search**, y los usuarios pueden buscar restaurantes cercanos a su ubicación usando **Leaflet** y palabras clave relacionadas con los platillos. Además, la aplicación genera descripciones de los menús utilizando **OpenAI**.

## Características principales
- **Registro de empresas**: Los restaurantes pueden registrarse y subir sus menús en formato PDF o imagen.
- **Almacenamiento en Azure Blob Storage**: Los menús se almacenan en un contenedor de Azure.
- **Indexación con Azure AI Search**: Se extrae información de los menús para facilitar la búsqueda por palabras clave.
- **Búsqueda de restaurantes**: Los usuarios pueden buscar restaurantes cercanos en un mapa interactivo de **Leaflet**.
- **Descripciones automáticas**: Se genera una descripción del menú usando **OpenAI**.

## Requisitos
Asegúrate de tener los siguientes servicios configurados antes de ejecutar la aplicación:

- Python 3.8+
- Django
- Azure Blob Storage
- Azure AI Search
- OpenAI API

## Instalación
1. **Clonar el repositorio:**
   ```sh
   git clone https://github.com/tuusuario/cuchara-app.git
   cd cuchara-app
   ```

2. **Crear un entorno virtual y activarlo:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configurar las variables de entorno:**
   Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

   ```ini
   BLOB_CONTAINER=<tu_blob_container>
   BLOB_CLIENT=<tu_blob_client>
   BLOB_KEY=<tu_blob_key>

   SEARCH_ENDPOINT=<tu_search_endpoint>
   SEARCH_INDEX_NAME=<tu_search_index_name>
   SEARCH_API_KEY=<tu_search_api_key>

   OPENAI_ENDPOINT=<tu_openai_endpoint>
   OPENAI_API_KEY=<tu_openai_api_key>
   OPENAI_DEPLOYMENT=<tu_openai_deployment>
   OPENAI_API_VERSION=<tu_openai_api_version>
   ```

5. **Ejecutar migraciones:**
   ```sh
   python manage.py migrate
   ```

6. **Ejecutar el servidor:**
   ```sh
   python manage.py runserver
   ```

## Uso
- Las empresas pueden registrarse y subir sus menús en la plataforma.
- Los usuarios pueden buscar restaurantes por nombre de platillo y ver los resultados en un mapa interactivo.
- Se puede hacer clic en cada restaurante para ver más detalles sobre su menú y ubicación.

## Tecnologías utilizadas
- **Backend:** Django
- **Base de datos:** SQLite
- **Almacenamiento:** Azure Blob Storage
- **Búsqueda:** Azure AI Search
- **Mapas:** Leaflet
- **IA:** OpenAI gpt-4o-mini

