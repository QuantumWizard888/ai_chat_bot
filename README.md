# AI chat bot for clients

## Simple AI chat bot for clients with CLI

AI chat bot for clients who want to know more about EORA company. It uses RAG (Retrieval Augmented Generation) technique and provides very ascetic CLI fo user to send queries and to get bot replies.

It uses:

* **LLM server**: Ollama
* **LLM models and embeddings**: llama3, mmxbai-embed-large
* **LLM framework**: Langchain
* **Vector DB**: ChromaDB

### Installation

1. Create virtual environment and activate it:
```
# Linux
python3 -m venv .venv
. .venv/bin/activate

# Windows
python3 -m venv .venv
.venv\Scripts\activate.bat
```
**NOTE**: If you want to make some changes to program code - make it while virtual environment is activated. Don't forget to exit virtual environment after you finish your work:
```
# Freeze additional libs requirements
pip freeze > requirements.txt

# Exit VENV on Linux
deactivate

# Exit VENV on Windows
.venv\Scripts\deactivate.bat
```

2. Install all required modules using:
```
pip install -r requirements
```

3. Install Ollama and pull required models using commands:
```
ollama pull llama3
ollama pull mxbai-embed-large
```

4. Run the AI bot:
```
python3 ai_chat_bot.py
```

### How to use?

Enter this query:
```
Что вы можете сделать для ритейлеров?
```
And hit ENTER.

If you'd like to exit the conversation just enter:
```
exit
```
And hit enter.

### FAQ

* Q: What you've tried to implement?
* A: I've tried to make simple AI bot with simple CLI which utilizes RAG with additional context.
* Q: What's working? And what's not?
* A: I guess succedeed in general RAG appoach, but the program still lacks internal solutions for flexible query context tuning.
* Q: What you think is your solution quality?
* A: Not as good as I want, but it gets things done.
* Q: What you'd like to add to yourr solution if you'd have more time?
* A:
    - Make an API which is used inside a web application
    - Make this application asynchronous
    - Add images (from company's portfolio) to the reply
    - Optimize for faster response generation

