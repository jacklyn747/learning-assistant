import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_classic.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Learning Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional UI
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stChatMessage {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .source-box {
        background-color: #e8f4f8;
        border-left: 4px solid #2196F3;
        padding: 10px;
        margin: 10px 0;
        border-radius: 5px;
        font-size: 0.9em;
    }
    h1 {
        color: #1e3a8a;
    }
    .stButton>button {
        background-color: #2196F3;
        color: white;
        border-radius: 5px;
        padding: 10px 24px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1976D2;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_resource
def initialize_rag_system():
    """Initialize the RAG system with document loading and vector store creation"""
    
    # Check if OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        st.error("⚠️ OpenAI API key not found! Please add it to your .env file.")
        st.stop()
    
    # Load documents from knowledge_base folder
    try:
        loader = DirectoryLoader(
            'knowledge_base/',
            glob="**/*.txt",
            loader_cls=TextLoader,
            loader_kwargs={'encoding': 'utf-8'}
        )
        documents = loader.load()
        
        if not documents:
            st.warning("⚠️ No documents found in knowledge_base folder!")
            return None
        
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_documents(documents)
        
        # Create embeddings and vector store
        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory="./chroma_db"
        )
        
        # Initialize ChatOpenAI
        llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.7,
            max_tokens=500
        )
        
        # Create custom prompt template
        prompt_template = """You are an expert instructional design and eLearning assistant. 
Use the following context to answer the question. If you don't know the answer based on the context, 
say so honestly. Always be specific and provide practical insights.

Context: {context}

Question: {question}

Answer:"""

        PROMPT = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )
        
        # Initialize conversation memory
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"
        )
        
        # Create conversational retrieval chain
        qa_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
            memory=memory,
            return_source_documents=True,
            combine_docs_chain_kwargs={"prompt": PROMPT}
        )
        
        return qa_chain, len(documents)
    
    except Exception as e:
        st.error(f"❌ Error initializing RAG system: {str(e)}")
        return None

def format_sources(source_documents):
    """Format source documents for display"""
    sources = []
    for i, doc in enumerate(source_documents, 1):
        source_file = os.path.basename(doc.metadata.get('source', 'Unknown'))
        sources.append(f"**Source {i}:** {source_file}")
    return sources

# Main app
def main():
    # Header
    st.title("🎓 AI-Powered Learning Assistant")
    st.markdown("*Your intelligent companion for instructional design and eLearning knowledge*")
    
    # Sidebar
    with st.sidebar:
        st.header("📚 System Info")
        
        # Initialize the RAG system
        with st.spinner("🔄 Loading knowledge base..."):
            result = initialize_rag_system()
        
        if result:
            qa_chain, doc_count = result
            st.success(f"✅ Loaded {doc_count} documents")
            st.info("💡 Ask me anything about instructional design, learning theories, or eLearning best practices!")
        else:
            st.error("❌ Failed to initialize system")
            qa_chain = None
        
        st.markdown("---")
        
        # Clear conversation button
        if st.button("🗑️ Clear Conversation"):
            st.session_state.messages = []
            if qa_chain:
                qa_chain.memory.clear()
            st.rerun()
        
        st.markdown("---")
        st.markdown("### 🛠️ Tech Stack")
        st.markdown("""
        - **LLM:** GPT-3.5-turbo
        - **Framework:** LangChain
        - **Vector DB:** ChromaDB
        - **UI:** Streamlit
        """)
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if "sources" in message:
                with st.expander("📄 View Sources"):
                    for source in message["sources"]:
                        st.markdown(f"<div class='source-box'>{source}</div>", unsafe_allow_html=True)
    
    # Chat input
    if prompt := st.chat_input("Ask me anything about instructional design..."):
        if not qa_chain:
            st.error("⚠️ System not initialized. Please check your setup.")
            return
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("🤔 Thinking..."):
                try:
                    response = qa_chain({"question": prompt})
                    answer = response['answer']
                    source_docs = response['source_documents']
                    
                    # Display answer
                    st.markdown(answer)
                    
                    # Display sources
                    if source_docs:
                        sources = format_sources(source_docs)
                        with st.expander("📄 View Sources"):
                            for source in sources:
                                st.markdown(f"<div class='source-box'>{source}</div>", unsafe_allow_html=True)
                        
                        # Add to chat history with sources
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": answer,
                            "sources": sources
                        })
                    else:
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": answer
                        })
                
                except Exception as e:
                    error_msg = f"❌ Error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": error_msg
                    })

if __name__ == "__main__":
    main()
