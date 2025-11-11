# 🚀 START HERE - Step-by-Step Instructions

## STEP 1: Download the Project

**Click this link to download everything:**
👉 **You need to download from the file browser on this interface**

The ZIP file is called: `learning_assistant_rag.zip` (24KB)

It contains all 12 files you need.

---

## STEP 2: Unzip the File

After downloading:
- **Windows**: Right-click → "Extract All"
- **Mac**: Double-click the ZIP file
- **Linux**: `unzip learning_assistant_rag.zip`

You'll get a folder called `learning_assistant/` with these files:

```
learning_assistant/
├── learning_assistant.py          ← Main app
├── requirements.txt               ← Dependencies
├── .env                          ← 🔑 API KEY GOES HERE
├── README.md                      ← Documentation
├── QUICKSTART.md                  ← Quick guide
├── test_setup.py                  ← Test script
└── knowledge_base/
    ├── addie_model.txt
    ├── adult_learning_principles.txt
    └── elearning_best_practices.txt
```

---

## STEP 3: Get Your OpenAI API Key

1. Go to: **https://platform.openai.com/api-keys**
2. Sign in (or create a free account)
3. Click **"Create new secret key"**
4. Give it a name like "Learning Assistant"
5. **Copy the key** (it looks like: `sk-proj-abc123...`)
   - ⚠️ Save it now! You can't see it again after you close the window

---

## STEP 4: Add Your API Key

**Find the `.env` file** in the `learning_assistant/` folder you just unzipped.

### On Windows:
- You might not see `.env` at first (hidden file)
- Open File Explorer → View tab → Check "File name extensions" and "Hidden items"
- Or just open the folder in VS Code or Notepad++

### On Mac/Linux:
- `.env` files are hidden by default
- Press `Cmd+Shift+.` (Mac) to show hidden files
- Or use: `ls -la` in Terminal to see it

### Edit the `.env` file:

**BEFORE (what it says now):**
```
OPENAI_API_KEY=your-api-key-here
```

**AFTER (with your actual key):**
```
OPENAI_API_KEY=sk-proj-abc123your-actual-key-here
```

**⚠️ Important:**
- Replace the ENTIRE phrase `your-api-key-here` with your actual key
- No quotes, no spaces
- Keep `OPENAI_API_KEY=` at the start
- Your key starts with `sk-` or `sk-proj-`

**Save the file** after editing.

---

## STEP 5: Install Dependencies

Open a terminal/command prompt in the `learning_assistant/` folder:

**Windows (Command Prompt or PowerShell):**
```bash
cd path\to\learning_assistant
pip install -r requirements.txt
```

**Mac/Linux (Terminal):**
```bash
cd /path/to/learning_assistant
pip install -r requirements.txt
```

This installs:
- Streamlit (UI)
- LangChain (RAG system)
- OpenAI SDK
- ChromaDB (vector database)

Takes about 1-2 minutes.

---

## STEP 6: Run the App

In the same terminal, run:

```bash
streamlit run learning_assistant.py
```

You should see:
```
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

**Your browser should open automatically** to http://localhost:8501

If not, manually open a browser and go to: **http://localhost:8501**

---

## STEP 7: Test It!

Once the app loads, you'll see:
- A chat interface
- A sidebar showing "✅ Loaded 3 documents"

**Ask a question like:**
- "What is the ADDIE model?"
- "How do adult learners differ from children?"
- "What are eLearning best practices?"

The bot will:
1. Search the knowledge base
2. Retrieve relevant chunks
3. Generate an answer with GPT-3.5
4. Show you the source documents

**Click "View Sources"** to see where the answer came from.

---

## ✅ YOU'RE DONE!

If you see the chat interface and can ask questions, **you're live**.

---

## 🐛 Troubleshooting

### "OpenAI API key not found"
- Check that you edited the `.env` file
- Make sure you saved the file after editing
- Verify your key starts with `sk-`
- Try restarting the app

### "No module named 'X'"
- Run: `pip install -r requirements.txt` again
- Make sure you're in the right folder

### "No documents found"
- Check that `knowledge_base/` folder exists
- Verify the 3 `.txt` files are inside it

### Can't see the `.env` file
- **Windows**: File Explorer → View → Show hidden files
- **Mac**: Finder → Press `Cmd+Shift+.`
- Or open the entire folder in VS Code to see all files

### Port already in use
- Try: `streamlit run learning_assistant.py --server.port 8502`
- Then go to: http://localhost:8502

---

## 💰 Costs

- **Setup**: ~$0.001 (creates embeddings once)
- **Each question**: ~$0.01-0.03
- **100 questions**: ~$1-3

Very affordable!

---

## 📚 Next Steps

Once it's working:
1. Read `QUICKSTART.md` for tips
2. Check `README.md` for advanced features
3. Add your own documents to `knowledge_base/`
4. Customize the UI in `learning_assistant.py`

---

## 🆘 Still Stuck?

**Common Issues:**

**Issue**: "I can't find the .env file"
**Solution**: It's hidden. Use VS Code or enable hidden files in your file browser.

**Issue**: "My API key isn't working"
**Solution**: 
- Go back to platform.openai.com
- Make sure your account has billing set up
- Check you copied the entire key (they're long!)
- Try creating a new key

**Issue**: "pip command not found"
**Solution**: 
- Install Python 3.8+ from python.org
- Make sure to check "Add Python to PATH" during installation
- Try `python -m pip install -r requirements.txt` instead

**Issue**: "It's running but responses are slow"
**Solution**: First query is always slower (creating embeddings). Subsequent queries are fast.

---

## 🎉 That's It!

You now have a working RAG chatbot. The hard part (building it) is done. You just need to:
1. Download the ZIP
2. Edit `.env` with your API key
3. Run `pip install -r requirements.txt`
4. Run `streamlit run learning_assistant.py`

**4 steps. That's it.**
