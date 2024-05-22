
def my_prompt():
    prompt_template = """
    Use the following pieces of infoormation to answer the user and if you do not know the answer to user's query, jut say you do not know, please do not make up the answer.

    Context: {context}
    Question: {question}

    Only return helpful answer nothing else.
    Helpful answer:
    """
    return prompt_template