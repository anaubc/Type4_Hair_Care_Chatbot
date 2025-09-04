import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

CHROMA_PATH = "chroma"

embeddings = OpenAIEmbeddings(openai_api_key=API_KEY)
db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)

def db_search(question, db, k=3, threshold=0.7):
    results = db.similarity_search_with_relevance_scores(question, k)
    if len(results) == 0 or results[0][1] < threshold:
        return None
    return [doc for doc, score in results if score >= threshold]

if __name__ == '__main__':
    print("\nHi! I am your Type 4 Hair Care Assistant. Ask me anything (or 'quit' to exit): ")
    model = ChatOpenAI(openai_api_key=API_KEY)

    while True:
        query = input("You: ")
        if query.lower() in ['quit', 'exit']:
            break

        docs = db_search(query, db)

        if docs is None:
            print("🤔 Sorry, I couldn't find the answer to your question in my sources.")
        else:
            context = "\n\n".join([doc.page_content for doc in docs])
            prompt = f"Based on the following articles:\n{context}\n\nAnswer the question: {query}"
            response = model.predict(prompt)
            sources = [doc.metadata.get("source", None) for doc in docs]
            print(f"Assistant: {response}\nSources: {sources}")