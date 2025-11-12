import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate

load_dotenv()

st.set_page_config(
    page_title="AI Learning Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.main { background-color: #f5f7fa; }
h1 { color: #000000; }
p { color: #262730; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def initialize_rag_system():
    if not os.getenv("OPENAI_API_KEY"):
        st.error("OpenAI API key not found!")
        st.stop()
    
    try:
        loader = DirectoryLoader('knowledge_base/', glob="**/*.txt", loader_cls=TextLoader, loader_kwargs={'encoding': 'utf-8'})
        documents = loader.load()
        
        if not documents:
            st.warning("No documents found!")
            return None
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_documents(documents)
        
        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory="./chroma_db")
        
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, max_tokens=500)
        
        prompt_template = """You are an expert instructional design assistant. Use the context to answer the question.

Context: {context}

Question: {question}

Answer:"""
        
        PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True, output_key="answer")
        
        qa_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
            memory=memory,
            return_source_documents=True,
            combine_docs_chain_kwargs={"prompt": PROMPT}
        )
        
        return qa_chain, len(documents)
    
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

def format_sources(source_documents):
    sources = []
    for i, doc in enumerate(source_documents, 1):
        source_file = os.path.basename(doc.metadata.get('source', 'Unknown'))
        sources.append(f"**Source {i}:** {source_file}")
    return sources

def main():
    st.title("🎓 AI-Powered Learning Assistant")
    st.markdown("*Your intelligent companion for instructional design knowledge*")
    
    with st.sidebar:
        st.header("📚 System Info")
        with st.spinner("Loading..."):
            result = initialize_rag_system()
        
        if result:
            qa_chain, doc_count = result
            st.success(f"Loaded {doc_count} documents")
        else:
            st.error("Failed to initialize")
            qa_chain = None
        
        st.markdown("---")
        if st.button("Clear Conversation"):
            st.session_state.messages = []
            if qa_chain:
                qa_chain.memory.clear()
            st.rerun()
        
        st.markdown("---")
        st.markdown("### Tech Stack")
        st.markdown("- LLM: GPT-3.5-turbo\n- Framework: LangChain\n- Vector DB: ChromaDB")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if "sources" in message:
                with st.expander("View Sources"):
                    for source in message["sources"]:
                        st.markdown(source)
    
    if prompt := st.chat_input("Ask about instructional design..."):
        if not qa_chain:
            st.error("System not initialized")
            return
        
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = qa_chain({"question": prompt})
                    answer = response['answer']
                    source_docs = response['source_documents']
                    
                    st.markdown(answer)
                    
                    if source_docs:
                        sources = format_sources(source_docs)
                        with st.expander("View Sources"):
                            for source in sources:
                                st.markdown(source)
                        st.session_state.messages.append({"role": "assistant", "content": answer, "sources": sources})
                    else:
                        st.session_state.messages.append({"role": "assistant", "content": answer})
                
                except Exception as e:
                    error_msg = f"Error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})

if __name__ == "__main__":
    main()
