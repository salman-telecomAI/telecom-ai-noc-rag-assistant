from fastapi import HTTPException

MAX_QUESTION_LENGTH = 1000


def validate_question(question: str) -> str:

    if question is None:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    question = question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    if len(question) > MAX_QUESTION_LENGTH:
        raise HTTPException(
            status_code=400,
            detail="Question exceeds maximum length."
        )

    return question