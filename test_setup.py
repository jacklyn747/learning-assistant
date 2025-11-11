#!/usr/bin/env python3
"""
Test script to validate the RAG Learning Assistant setup
This verifies all components work without requiring an API key
"""

import os
import sys
from pathlib import Path

def test_imports():
    """Test that all required packages are installed"""
    print("🔍 Testing package imports...")
    
    try:
        import streamlit
        print("  ✅ Streamlit imported successfully")
    except ImportError as e:
        print(f"  ❌ Streamlit import failed: {e}")
        return False
    
    try:
        from langchain_community.document_loaders import DirectoryLoader, TextLoader
        from langchain_text_splitters import RecursiveCharacterTextSplitter
        from langchain_openai import OpenAIEmbeddings, ChatOpenAI
        from langchain_community.vectorstores import Chroma
        from langchain_classic.chains import ConversationalRetrievalChain
        from langchain_classic.memory import ConversationBufferMemory
        from langchain_core.prompts import PromptTemplate
        print("  ✅ LangChain components imported successfully")
    except ImportError as e:
        print(f"  ❌ LangChain import failed: {e}")
        return False
    
    try:
        import chromadb
        print("  ✅ ChromaDB imported successfully")
    except ImportError as e:
        print(f"  ❌ ChromaDB import failed: {e}")
        return False
    
    try:
        import tiktoken
        print("  ✅ Tiktoken imported successfully")
    except ImportError as e:
        print(f"  ❌ Tiktoken import failed: {e}")
        return False
    
    try:
        from dotenv import load_dotenv
        print("  ✅ python-dotenv imported successfully")
    except ImportError as e:
        print(f"  ❌ python-dotenv import failed: {e}")
        return False
    
    return True

def test_file_structure():
    """Test that all required files exist"""
    print("\n📁 Testing file structure...")
    
    required_files = [
        'learning_assistant.py',
        'requirements.txt',
        '.env',
        'README.md',
        'knowledge_base/addie_model.txt',
        'knowledge_base/adult_learning_principles.txt',
        'knowledge_base/elearning_best_practices.txt'
    ]
    
    all_exist = True
    for file_path in required_files:
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            print(f"  ✅ {file_path} ({size:,} bytes)")
        else:
            print(f"  ❌ {file_path} NOT FOUND")
            all_exist = False
    
    return all_exist

def test_knowledge_base():
    """Test that knowledge base documents can be loaded"""
    print("\n📚 Testing knowledge base loading...")
    
    try:
        from langchain_community.document_loaders import DirectoryLoader, TextLoader
        from langchain_text_splitters import RecursiveCharacterTextSplitter
        
        # Load documents
        loader = DirectoryLoader(
            'knowledge_base/',
            glob="**/*.txt",
            loader_cls=TextLoader,
            loader_kwargs={'encoding': 'utf-8'}
        )
        documents = loader.load()
        print(f"  ✅ Loaded {len(documents)} documents")
        
        # Split into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = text_splitter.split_documents(documents)
        print(f"  ✅ Split into {len(chunks)} chunks")
        
        # Show sample content
        if chunks:
            sample = chunks[0].page_content[:200]
            print(f"\n  📄 Sample chunk preview:")
            print(f"     {sample}...")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error loading documents: {e}")
        return False

def test_env_file():
    """Test .env file configuration"""
    print("\n🔑 Testing .env configuration...")
    
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        api_key = os.getenv('OPENAI_API_KEY')
        
        if not api_key:
            print("  ⚠️  OPENAI_API_KEY not set in .env")
            print("     Add your API key to .env to use the chatbot")
            return False
        elif api_key == 'your-api-key-here':
            print("  ⚠️  OPENAI_API_KEY is still placeholder value")
            print("     Replace with your actual OpenAI API key")
            return False
        elif api_key.startswith('sk-'):
            print("  ✅ OPENAI_API_KEY is configured (starts with sk-)")
            return True
        else:
            print("  ⚠️  OPENAI_API_KEY format looks incorrect")
            print("     OpenAI keys should start with 'sk-'")
            return False
            
    except Exception as e:
        print(f"  ❌ Error checking .env: {e}")
        return False

def test_streamlit_syntax():
    """Test that the main app file has valid Python syntax"""
    print("\n🐍 Testing Python syntax...")
    
    try:
        import py_compile
        py_compile.compile('learning_assistant.py', doraise=True)
        print("  ✅ learning_assistant.py has valid syntax")
        return True
    except Exception as e:
        print(f"  ❌ Syntax error in learning_assistant.py: {e}")
        return False

def main():
    """Run all tests"""
    print("="*60)
    print("🧪 RAG Learning Assistant - Setup Validation")
    print("="*60)
    
    results = {
        'imports': test_imports(),
        'files': test_file_structure(),
        'knowledge_base': test_knowledge_base(),
        'env': test_env_file(),
        'syntax': test_streamlit_syntax()
    }
    
    print("\n" + "="*60)
    print("📊 TEST RESULTS SUMMARY")
    print("="*60)
    
    passed = sum(results.values())
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name.replace('_', ' ').title()}")
    
    print("="*60)
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Your setup is ready.")
        print("\n📝 Next steps:")
        print("   1. Add your OpenAI API key to .env file")
        print("   2. Run: streamlit run learning_assistant.py")
        print("   3. Open browser at http://localhost:8501")
    elif results['env'] == False and passed == total - 1:
        print("\n⚠️  Almost ready! Just need to add your API key.")
        print("\n📝 Next steps:")
        print("   1. Edit .env and add: OPENAI_API_KEY=sk-your-key-here")
        print("   2. Run: streamlit run learning_assistant.py")
    else:
        print("\n❌ Some tests failed. Please fix the issues above.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
