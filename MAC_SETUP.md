# 🍎 Mac Setup Instructions

## The .env file IS in the ZIP, but Mac sometimes hides it during extraction.

## SOLUTION 1: Use Terminal (Easiest)

1. **Open Terminal** (Applications → Utilities → Terminal)

2. **Navigate to where you extracted the folder:**
   ```bash
   cd ~/Downloads/learning_assistant
   ```
   (Or wherever you put it)

3. **List ALL files including hidden ones:**
   ```bash
   ls -la
   ```

4. **You should see `.env` in the list**

5. **If you see it, show the contents:**
   ```bash
   cat .env
   ```

6. **Edit it with nano:**
   ```bash
   nano .env
   ```
   - Replace `your-api-key-here` with your actual OpenAI key
   - Press `Control + X` to exit
   - Press `Y` to save
   - Press `Enter` to confirm

---

## SOLUTION 2: Show Hidden Files in Finder

1. Open Finder
2. Navigate to your `learning_assistant` folder
3. Press: **Command + Shift + . (period)**
4. Hidden files (starting with `.`) will now be visible
5. You'll see `.env` appear
6. Double-click to open it (it'll open in TextEdit)
7. Replace `your-api-key-here` with your actual key
8. Save

---

## SOLUTION 3: Create it from the template

If the `.env` file REALLY isn't there:

1. **In Finder, find the file called `env_template.txt`** (it's visible)
2. **Duplicate it** (Right-click → Duplicate)
3. **Rename the duplicate from `env_template.txt` to `.env`**
   - Just `.env` - nothing else
4. **Open it** (double-click, opens in TextEdit)
5. **Replace `your-api-key-here` with your actual OpenAI API key**
6. **Save it**

---

## Verify It Worked

In Terminal:
```bash
cd ~/Downloads/learning_assistant
cat .env
```

You should see:
```
OPENAI_API_KEY=sk-proj-yourkeyhere
```

---

## Then Install & Run

```bash
# Install dependencies
pip3 install -r requirements.txt

# Run the app
streamlit run learning_assistant.py
```

Browser opens to http://localhost:8501

Done! 🎉
