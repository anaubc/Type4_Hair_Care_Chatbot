# Type 4 Hair Care Chatbot
My summer 2025 internship with the **ChatMFC** team at Manulife truly sparked this project. I enjoyed gaining hands-on experience with chat automation and retrieval techniques. Since I take great pride in my hair and routine and have spent many hours watching videos and reading about **Type 4 hair care**, I felt inspired to combine these two passions into one exciting project.

The result is a **retrieval-augmented chatbot** that specializes in answering questions about Type 4 natural hair. It uses:
- **LangChain** for orchestration
- **ChromaDB** for storing and retrieving embedded documents
- **OpenAI API** for generating natural language responses

I looked for articles related to this topic online and converted them to Markdown files. They are preprocessed, chunked, and stored in a persistent Chroma database. At query time, the chatbot retrieves the most relevant passages, applies a relevance score filter to reduce hallucinations, and generates a conversational response. 

This project is still in progress! I plan to enhance the accuracy and add more hair care resources. 

Here are a few videos that helped me create this project:
- [RAG + Langchain](https://www.youtube.com/watch?v=tcqEUSNCn8I)
- [Python GPT Chatbot](https://www.youtube.com/watch?v=q5HiD5PNuck)
