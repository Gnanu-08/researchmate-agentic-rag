# Viva Questions and Answers

1. What is RAG?
RAG retrieves relevant external knowledge and supplies it to an LLM before generation.

2. Why use RAG?
It reduces dependence on the model's parametric knowledge and grounds answers in a controlled knowledge base.

3. What makes this project agentic?
The system has a planner, retrieval tool, evidence evaluator, and iterative retrieval decision instead of a single fixed generation call.

4. Why ChromaDB?
It provides a simple local vector store suitable for document retrieval prototypes.

5. Why Sentence Transformers?
They provide local embeddings without requiring an embedding API.

6. Why provider abstraction?
It prevents agent code from being tied to one LLM vendor.

7. How do you switch to Ollama?
Set LLM_PROVIDER=ollama and configure the Ollama model.

8. How do you switch to OpenAI?
Set LLM_PROVIDER=openai and provide OPENAI_API_KEY.

9. What is chunking?
Breaking documents into smaller passages so retrieval can find focused evidence.

10. What happens if evidence is insufficient?
The controller performs a refined retrieval attempt before generating the answer.

11. How are hallucinations reduced?
The generator is instructed to use only retrieved evidence and explicitly say when evidence is insufficient.

12. What is the main limitation?
The quality of retrieval and generation depends on the knowledge base, embedding model, and selected LLM.
