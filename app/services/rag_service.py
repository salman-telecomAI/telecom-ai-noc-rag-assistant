from fastapi import HTTPException

from app.rag.search import search_documents
from app.services.llm import ask_llm
from app.utils.logger import logger


def generate_answer(question: str, top_k: int = 3):

    try:

        if not question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty.")

        logger.info(f"Question received: {question}")

        documents = search_documents(question, top_k)

        if not documents:
            logger.warning("No relevant telecom documents found.")

            return {
                "question": question,
                "answer": "No relevant telecom information found.",
                "context": [],
            }

        logger.info(f"{len(documents)} document(s) retrieved.")

        context = "\n\n".join(documents)

        prompt = f"""
You are a Senior DWDM/NOC Engineer.

Answer ONLY using the context below.

Context:
{context}

Question:
{question}

Answer:
"""

        logger.info("Sending request to OpenRouter...")

        answer = ask_llm(prompt)

        logger.info("Answer generated successfully.")

        return {"question": question, "answer": answer, "context": documents}

    except HTTPException:
        raise

    except Exception as e:

        logger.exception("Unexpected application error.")

        raise HTTPException(status_code=500, detail=str(e))
