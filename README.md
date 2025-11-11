# 🎓 AI-Powered Learning Assistant

An intelligent chatbot powered by RAG (Retrieval-Augmented Generation) that answers questions about instructional design, eLearning, and learning theories using a custom knowledge base.

## 🚀 Features

- **Smart Q&A**: Ask questions and get accurate answers from your knowledge base
- **Source Citations**: See exactly where information comes from
- **Conversation Memory**: Context-aware responses that remember your chat history
- **Professional UI**: Clean, modern Streamlit interface
- **Custom Knowledge Base**: Easily add your own documents to expand the bot's knowledge

## 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit**: Web UI framework
- **LangChain**: RAG orchestration
- **OpenAI GPT-3.5-turbo**: Language model
- **ChromaDB**: Vector database for embeddings
- **OpenAI Embeddings**: Document vectorization

## 📦 Installation

### 1. Clone or Download the Project

Save all files in a folder called `learning_assistant/`

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up OpenAI API Key

Edit the `.env` file and add your OpenAI API key:

```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

Get your API key from: https://platform.openai.com/api-keys

### 4. Add Knowledge Base Documents

The `knowledge_base/` folder contains sample documents about:
- ADDIE Model (instructional design framework)
- Adult Learning Principles (andragogy)
- eLearning Best Practices

To add your own documents:
1. Create `.txt` files with your content
2. Place them in the `knowledge_base/` folder
3. Restart the application to load new documents

## 🎯 Usage

### Start the Application

```bash
streamlit run learning_assistant.py
```

The app will open in your browser at `http://localhost:8501`

### Using the Chatbot

1. **Wait for initialization**: The system loads documents and creates embeddings on startup
2. **Ask questions**: Type your question in the chat input
3. **View sources**: Expand the "View Sources" section to see where answers came from
4. **Clear conversation**: Use the sidebar button to start a fresh conversation

### Example Questions

- "What is the ADDIE model?"
- "How do adult learners differ from children?"
- "What are best practices for eLearning design?"
- "Explain the analysis phase of ADDIE"
- "What is cognitive load theory?"
- "How should I design assessments for eLearning?"

## 📁 Project Structure

```
learning_assistant/
│
├── learning_assistant.py       # Main Streamlit application
├── requirements.txt             # Python dependencies
├── .env                         # OpenAI API key configuration
├── README.md                    # This file
│
├── knowledge_base/              # Your custom documents
│   ├── addie_model.txt
│   ├── adult_learning_principles.txt
│   └── elearning_best_practices.txt
│
└── chroma_db/                   # Vector database (auto-created)
```

## 🔧 Configuration

### Adjusting Model Parameters

In `learning_assistant.py`, you can modify:

```python
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",  # or "gpt-4" for better quality
    temperature=0.7,              # 0.0-1.0 (lower = more focused)
    max_tokens=500                # Response length limit
)
```

### Changing Retrieval Settings

Adjust the number of source documents retrieved:

```python
retriever=vectorstore.as_retriever(search_kwargs={"k": 3})  # Change k value
```

### Customizing Chunk Size

Modify document splitting parameters:

```python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,      # Increase for longer chunks
    chunk_overlap=200     # Overlap between chunks
)
```

## 🐛 Troubleshooting

### "OpenAI API key not found"
- Check that your `.env` file exists
- Verify your API key is correct
- Make sure the key starts with `sk-`

### "No documents found in knowledge_base folder"
- Ensure `.txt` files are in the `knowledge_base/` folder
- Check file permissions

### Slow responses
- GPT-3.5-turbo is fast, but embedding creation on first run takes time
- Subsequent queries are faster
- Consider reducing chunk_size or k value

### Import errors
- Run `pip install -r requirements.txt` again
- Check Python version (3.8+ required)

## 💡 Extending the Knowledge Base

### Supported Document Formats
Currently supports `.txt` files. To add other formats:

```python
# For PDF files
from langchain.document_loaders import PyPDFLoader

# For Word documents
from langchain.document_loaders import Docx2txtLoader

# For Markdown
from langchain.document_loaders import UnstructuredMarkdownLoader
```

### Best Practices for Knowledge Base Content
- Use clear, structured text
- Include headings and sections
- Keep files focused on specific topics
- Aim for 1000-5000 words per document
- Use consistent terminology

## 🔐 Security Notes

- Never commit your `.env` file with real API keys to version control
- Add `.env` to `.gitignore`
- Keep your OpenAI API key private
- Monitor your OpenAI usage at platform.openai.com

## 📊 Costs

OpenAI API costs (as of 2024):
- **GPT-3.5-turbo**: ~$0.002 per 1K tokens
- **Embeddings**: ~$0.0001 per 1K tokens

Typical costs per query:
- Embedding cost: negligible
- Query cost: ~$0.01-0.05 depending on length

## 🚀 Next Steps

Ideas to enhance this project:
- Add support for PDF, DOCX, and Markdown files
- Implement user authentication
- Add file upload feature for dynamic knowledge base updates
- Create API endpoints for integration
- Add conversation export/import
- Implement multi-language support
- Add semantic search features
- Create admin dashboard for analytics

## 📝 License

This project is open source and available for educational and commercial use.

## 🙏 Credits

Built with:
- [LangChain](https://langchain.com/)
- [Streamlit](https://streamlit.io/)
- [OpenAI](https://openai.com/)
- [ChromaDB](https://www.trychroma.com/)

---

**Need help?** Check the troubleshooting section or review the inline code comments in `learning_assistant.py`
