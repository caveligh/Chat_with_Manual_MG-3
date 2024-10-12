# pip install langchain chromadb pypdf streamlit openai

import os
import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Configura tu clave de API de OpenAI
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
if OPENAI_API_KEY is None:
    OPENAI_API_KEY = 'tu_clave_de_api_de_openai'  # Reemplaza con tu clave real

def actualizar_embeddings():
    ruta_pdf = "MG3.pdf"
    loader = PyPDFLoader(ruta_pdf)
    docs = loader.load()
    # Dividir el texto en fragmentos manejables
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    chunked_documents = text_splitter.split_documents(docs)
    # Crear la base de datos vectorial y persistirla
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectordb = Chroma.from_documents(
        chunked_documents, 
        embeddings,
        persist_directory="./chroma_db"
    )
    vectordb.persist()
    return vectordb

st.title("Mesa de ayuda del MG3")
st.write("Este agente responde preguntas relacionadas con el MG3.")

# Inicializar variables en session_state si no existen
if 'vectordb' not in st.session_state:
    st.session_state['vectordb'] = None
if 'retriever' not in st.session_state:
    st.session_state['retriever'] = None
if 'embeddings_updated' not in st.session_state:
    st.session_state['embeddings_updated'] = False

# Verificar si la base de datos existe y cargarla si es así
if not st.session_state['embeddings_updated'] and os.path.exists("./chroma_db"):
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectordb = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    st.session_state['vectordb'] = vectordb
    st.session_state['retriever'] = vectordb.as_retriever(search_kwargs={"k": 5})
    st.session_state['embeddings_updated'] = True
    st.success("Embeddings cargados desde el almacenamiento.")

# Botón para actualizar embeddings
if not st.session_state['embeddings_updated']:
    if st.button("Actualizar Embeddings"):
        with st.spinner('Actualizando embeddings...'):
            vectordb = actualizar_embeddings()
            st.session_state['vectordb'] = vectordb
            st.session_state['retriever'] = vectordb.as_retriever(search_kwargs={"k": 5})
            st.session_state['embeddings_updated'] = True
            st.success("Embeddings actualizados correctamente.")
else:
    st.write("Los embeddings están actualizados y listos para usar.")

# Definir el modelo de lenguaje
llm = ChatOpenAI(model_name="gpt-3.5-turbo", max_tokens=1024, openai_api_key=OPENAI_API_KEY)

# Crear el prompt template
prompt_template = '''
Eres un agente de ayuda inteligente especializado en el manual del usuario del MG3.
Responde las preguntas de los usuarios basándote estrictamente en la información proporcionada.
No hagas suposiciones ni proporciones información que no esté incluida en los documentos.

Pregunta: {question}
=========
{context}
=========
Respuesta en Español:
'''

prompt = PromptTemplate(
    input_variables=["question", "context"],
    template=prompt_template
)

# Mostrar el campo de texto para la pregunta
pregunta = st.text_area("Haz tu pregunta sobre el manual")

# Botón para enviar la pregunta
if st.button("Enviar"):
    if pregunta:
        if st.session_state['retriever'] is not None:
            # Crear el chain de QA con recuperación
            qa_chain = RetrievalQA.from_chain_type(
                llm=llm, 
                chain_type="stuff", 
                retriever=st.session_state['retriever'], 
                chain_type_kwargs={"prompt": prompt}
            )
            with st.spinner('Generando respuesta...'):
                respuesta = qa_chain.run(pregunta)
            st.write(respuesta)
        else:
            st.warning("Los embeddings no están actualizados. Por favor, haz clic en 'Actualizar Embeddings' y espera a que se complete el proceso.")
    else:
        st.write("Por favor, ingresa una pregunta antes de enviar.")
