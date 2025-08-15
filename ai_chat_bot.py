from langchain.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_ollama.llms import OllamaLLM
from langchain.text_splitter import RecursiveCharacterTextSplitter



def main():
    # <--- DOCUMENT LOADING
    loader = TextLoader("data.txt", encoding="utf-8") # Replace with your document
    documents = loader.load()
    # --->

    # <--- DOCUMENT DATA SPLITTING
    data_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, separators='---')
    data_chunks = data_splitter.split_documents(documents)
    # --->

    # <--- CREATE EMBEDDINGS AND STORE DATA CHUNKS IN VECTOR DB
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")
    vector_db = Chroma.from_documents(data_chunks, embeddings)
    # --->

    # <--- LLM AI MODEL INIT
    ollama_llm = OllamaLLM(model="llama3")
    # --->

    # <--- RAG CREATING
    rag_qa_chain = RetrievalQA.from_chain_type(
        llm=ollama_llm,
        chain_type="stuff",
        retriever=vector_db.as_retriever()
    )
    # --->

    # <--- QUERY (PROMPT) CLI SHELL
    print('####################################')
    print('#          EORA AI CHAT BOT        #')
    print('#  Simple AI chat bot for clients  #')
    print('####################################')

    while True:
        query = input("[Вопрос]: ") # Standard query: "Что вы можете сделать для ритейлеров?"
        
        if query == 'exit':
            print("Завершение работы...")
            exit()

        query_context = " Ответьте на руссом языке и приложите ссылки на примеры продуктов EORA"
        query = query+query_context

        llm_response = rag_qa_chain.invoke({"query": query})
        print("[Ответ]:", llm_response["result"], sep='\n')
    # --->


if __name__ == "__main__":
    main()