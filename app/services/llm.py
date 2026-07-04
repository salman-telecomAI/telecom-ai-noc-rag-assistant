def generate_answer(question: str, context: str):
    """
    Placeholder Azure OpenAI response.
    """

    return {
        "question": question,
        "context": context,
        "answer": "Azure OpenAI placeholder response."
    }


if __name__ == "__main__":
    result = generate_answer(
        "What is LOS Alarm?",
        "LOS Alarm indicates Loss of Signal."
    )

    print(result)