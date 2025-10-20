# 📰 News Research Assistant

A powerful AI-powered tool that answers news questions using Retrieval-Augmented Generation (RAG). This application scrapes content from provided URLs, indexes it in a vector database, and uses an LLM to generate accurate answers based on the retrieved information.

![News Research Assistant](https://github.com/Vraj-Data-Scientist/real-estate-assistant-using-RAG/blob/main/image.png?raw=true)

## ✨ Features

- 🔗 **Flexible URL Input**: Use predefined URLs or add your own custom sources
- 🤖 **AI-Powered Answers**: Leverages Groq's LLM (Llama 3.3 70B) for intelligent responses
- 📚 **Vector Database**: Uses ChromaDB with HuggingFace embeddings for efficient retrieval
- 🎯 **Source Attribution**: Provides sources for generated answers
- 🚀 **User-Friendly Interface**: Built with Streamlit for an intuitive experience

## 🛠️ Technologies Used

- **Streamlit**: Web application framework
- **LangChain**: Framework for LLM applications
- **Groq API**: Fast LLM inference (Llama 3.3 70B)
- **ChromaDB**: Vector database for semantic search
- **HuggingFace Embeddings**: Sentence transformers for text embeddings
- **Unstructured**: URL content extraction

## 📋 Prerequisites

- Python 3.8 or higher
- Groq API key (get it from [Groq Console](https://console.groq.com/))

## 🚀 Installation

1. **Clone the repository**
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your-groq-api-key-here
```

## 🎯 Usage

1. **Start the application**
```bash
streamlit run main.py
```

2. **Access the app**
   - Open your browser and go to `http://localhost:8501`

3. **How to use**
   - Select predefined URLs from the sidebar or add custom URLs
   - Click "🔄 Process URLs" to index the content
   - Ask questions in the text input field
   - Get AI-generated answers with source citations!

## 📝 Example Questions

- "What's the current 30-year mortgage rate?"
- "What factors affect mortgage rates?"
- "What are the latest trends in the news?"
- "What was the mortgage rate on March 20, 2025?"

## 🎨 Project Structure

```
.
├── main.py              # Streamlit frontend application
├── rag.py              # RAG backend (URL processing, embeddings, LLM)
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not tracked by git)
├── .gitignore         # Git ignore file
└── resources/         # Vector database storage (auto-generated)
    └── vectorstore/   # ChromaDB persistence directory
```

## ⚙️ Configuration

### Model Settings (in `rag.py`)
- **LLM Model**: `llama-3.3-70b-versatile`
- **Temperature**: `0.9`
- **Max Tokens**: `500`
- **Embedding Model**: `sentence-transformers/all-MiniLM-L6-v2`
- **Chunk Size**: `1000`

### Predefined URLs (in `main.py`)
- Mortgage News Daily: https://www.mortgagenewsdaily.com/mortgage-rates
- Bankrate Mortgages: https://www.bankrate.com/mortgages/

## 🔒 Security Notes

- Never commit your `.env` file or API keys to Git
- The `.gitignore` file is configured to exclude sensitive files
- Keep your Groq API key secure and private

## ⚠️ Limitations

- Works best with text-rich, publicly accessible websites
- May struggle with:
  - Content behind login walls
  - Information in images or complex tables
  - Sites that block automated access (like CNBC)
  - Dynamic content that requires JavaScript

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with [LangChain](https://www.langchain.com/)
- Powered by [Groq](https://groq.com/)
- UI built with [Streamlit](https://streamlit.io/)

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Happy News Research! 📰**
