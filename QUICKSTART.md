# 🚀 Quick Start Guide

## Setup in 3 Steps

### 1. Get Your OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)

### 2. Add API Key to .env File

Open the `.env` file and replace the placeholder:

```bash
# Before:
OPENAI_API_KEY=your-api-key-here

# After:
OPENAI_API_KEY=sk-your-actual-key-here
```

Save the file.

### 3. Run the Application

```bash
streamlit run learning_assistant.py
```

The app will open in your browser at: http://localhost:8501

## 🎯 Try These Questions

Once the app is running, try asking:

- "What is the ADDIE model and why is it important?"
- "How do adult learners differ from children?"
- "What are best practices for eLearning design?"
- "Explain cognitive load theory"
- "What is the analysis phase in ADDIE?"
- "How should I design assessments for adults?"

## 🔧 Troubleshooting

### "No module named 'X'"
Run: `pip install -r requirements.txt`

### "OpenAI API key not found"
Make sure you edited the `.env` file with your actual API key

### App won't start
1. Make sure you're in the `learning_assistant/` directory
2. Check that Python 3.8+ is installed: `python --version`
3. Try: `streamlit run learning_assistant.py --server.port 8502`

## 📚 Adding Your Own Documents

1. Create `.txt` files with your content
2. Place them in the `knowledge_base/` folder
3. Restart the application

The system will automatically:
- Load your documents
- Create embeddings
- Make them searchable via chat

## 💰 Cost Estimate

- Embedding 3 sample documents: ~$0.001
- Each question/answer: ~$0.01-0.03
- 100 questions ≈ $1-3

Very affordable for personal use!

## 🎨 Customization Ideas

1. **Change the model** (in `learning_assistant.py`):
   ```python
   model_name="gpt-4"  # Better quality, higher cost
   ```

2. **Adjust temperature** for more/less creative answers:
   ```python
   temperature=0.3  # More focused (0.0-1.0)
   ```

3. **Retrieve more sources**:
   ```python
   search_kwargs={"k": 5}  # Return 5 sources instead of 3
   ```

## 📊 What's Happening Under the Hood

1. **Document Loading**: Reads all `.txt` files from `knowledge_base/`
2. **Chunking**: Splits documents into 1000-character chunks
3. **Embedding**: Converts chunks to vector embeddings using OpenAI
4. **Storage**: Stores embeddings in ChromaDB (local vector database)
5. **Query**: Your question is embedded and matched against stored chunks
6. **Retrieval**: Top 3 most relevant chunks are retrieved
7. **Generation**: GPT-3.5 generates answer based on retrieved context
8. **Memory**: Conversation history is maintained for context-aware responses

## 🔒 Privacy & Data

- All processing happens locally except OpenAI API calls
- Your documents stay on your machine (ChromaDB is local)
- Only queries and retrieved context are sent to OpenAI
- Conversation history stays in your browser session

## Next Level Features

Want to add:
- PDF upload functionality
- Multiple knowledge bases
- Export conversations
- Voice input
- Multi-language support
- Admin dashboard

These are all possible extensions! The codebase is designed to be hackable.

---

**Need help?** Check the main `README.md` or the code comments in `learning_assistant.py`
