**Chat With Docs**

Este proyecto es una aplicación interactiva desarrollada en Streamlit que permite a los usuarios hacer preguntas sobre el manual del usuario del MG3 y obtener respuestas precisas basadas únicamente en el contenido del manual. Utiliza LangChain, OpenAI GPT-3.5-turbo y ChromaDB para proporcionar respuestas informadas y reducir las alucinaciones.

**Características**

- **Interfaz de Usuario Interactiva**: Utiliza Streamlit para proporcionar una interfaz sencilla y fácil de usar.
- **Procesamiento de Documentos**: Carga y procesa el manual del MG3 en formato PDF.
- **Vectorización y Recuperación**: Utiliza ChromaDB y embeddings de OpenAI para indexar y recuperar información relevante del manual.
- **Modelo de Lenguaje Avanzado**: Emplea el modelo GPT-3.5-turbo de OpenAI para generar respuestas basadas en el contexto proporcionado.
- **Reducción de Alucinaciones**: Mediante el uso de prompts específicos y cadenas de recuperación, se garantiza que las respuestas se basen estrictamente en el contenido del manual.

**Requisitos Previos**

- Python 3.7 o superior
- Cuenta de OpenAI con una clave de API válida
- Paquetes de Python listados en requirements.txt o instalados como se indica a continuación

**Instalación**

**Clonar el Repositorio**

git clone <https://github.com/tu_usuario/mesa-de-ayuda-mg3.git>

cd mesa-de-ayuda-mg3

**Crear un Entorno Virtual (Opcional pero Recomendado)**

python -m venv venv

\# En Windows

venv\\Scripts\\activate

\# En Unix o MacOS

source venv/bin/activate

**Instalar las Dependencias**

pip install --upgrade pip

pip install langchain chromadb pypdf streamlit openai

**Configuración**

**Clave de API de OpenAI**

Necesitas una clave de API de OpenAI para utilizar el modelo GPT-3.5-turbo. Puedes obtenerla en [OpenAI API Keys](https://platform.openai.com/account/api-keys).

Existen dos formas de configurar la clave de API:

1. **Variable de Entorno**: Establece una variable de entorno llamada OPENAI_API_KEY con tu clave.
    - En Windows:

set OPENAI_API_KEY=tu_clave_de_api_de_openai

- - En Unix o MacOS:

export OPENAI_API_KEY=tu_clave_de_api_de_openai

1. **En el Código**: Edita el archivo chat_with_docs.py y reemplaza 'tu_clave_de_api_de_openai' con tu clave real.

python

Copiar código

OPENAI_API_KEY = 'tu_clave_de_api_de_openai' # Reemplaza con tu clave real

**Archivo PDF del Manual**

Asegúrate de que el archivo MG3.pdf (el manual del MG3) está en el mismo directorio que el script chat_with_docs.py. Si el archivo tiene otro nombre o está en otra ubicación, modifica la ruta en la función actualizar_embeddings():

def actualizar_embeddings():

ruta_pdf = "ruta/a/tu/MG3.pdf"

\# ...

**Uso**

**Ejecutar la Aplicación**

Inicia la aplicación de Streamlit ejecutando el siguiente comando en el directorio del proyecto:

streamlit run chat_with_docs.py

**Interactuar con la Aplicación**

1. **Actualizar Embeddings (si es necesario)**: Si es la primera vez que ejecutas la aplicación o si el contenido del manual ha cambiado, haz clic en el botón **"Actualizar Embeddings"**. Este proceso puede tomar algunos minutos.
2. **Hacer Preguntas**: Escribe tu pregunta sobre el manual del MG3 en el campo de texto proporcionado.
3. **Enviar la Pregunta**: Haz clic en el botón **"Enviar"**. La aplicación procesará tu pregunta y generará una respuesta basada en el contenido del manual.

**Estructura del Proyecto**

- **chat_with_docs.py**: Script principal que ejecuta la aplicación de Streamlit.
- **MG3.pdf**: Archivo PDF del manual del MG3 (debes proporcionar este archivo).
- **./chroma_db**: Directorio donde se almacenan los embeddings y la base de datos vectorial (se genera después de actualizar embeddings).

**Tecnologías Utilizadas**

- **Streamlit**: Biblioteca para crear aplicaciones web interactivas en Python.
- **LangChain**: Marco de trabajo para construir aplicaciones de lenguaje natural con modelos de lenguaje grandes.
- **OpenAI GPT-3.5-turbo**: Modelo de lenguaje avanzado para generación de texto.
- **ChromaDB**: Base de datos vectorial para almacenar y recuperar embeddings.
- **PyPDFLoader**: Herramienta para cargar y procesar documentos PDF.

**Personalización**

- **Cambiar el Modelo de Lenguaje**: Puedes ajustar el modelo utilizado en ChatOpenAI modificando el parámetro model_name.

llm = ChatOpenAI(model_name="gpt-3.5-turbo", ...)

- **Ajustar el Prompt**: El prompt utilizado para generar respuestas se puede modificar en el prompt_template.

prompt_template = '''

Eres un agente de ayuda inteligente especializado en el manual del usuario del MG3.

...

'''

- **Cambiar el Documento de Referencia**: Si deseas utilizar otro documento, reemplaza el archivo PDF y actualiza la ruta en actualizar_embeddings().

**Solución de Problemas**

- **Error de Clave de API**: Asegúrate de que la clave de API de OpenAI es correcta y está configurada adecuadamente.
- **Problemas con Paquetes**: Verifica que todos los paquetes están instalados y actualizados. Puedes reinstalarlos utilizando:

pip install --upgrade langchain chromadb pypdf streamlit openai

- **Archivo PDF no Encontrado**: Confirma que el archivo PDF está en la ubicación correcta y que la ruta es correcta en el código.
- **Tiempo de Respuesta Lento**: La generación de embeddings y respuestas puede tomar tiempo. Ten paciencia y espera a que el proceso finalice.

**Contribuciones**

Si deseas contribuir a este proyecto, puedes:

- Reportar problemas y errores
- Proponer mejoras y nuevas características
- Enviar pull requests con cambios y correcciones

**Licencia**

Este proyecto se distribuye bajo la Licencia MIT.