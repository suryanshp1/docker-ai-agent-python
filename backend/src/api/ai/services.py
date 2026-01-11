from .llms import get_openai_llm
from .schemas import EmailMessage


def generate_email_messages(query: str) -> EmailMessage:
    llm_base = get_openai_llm()
    llm = llm_base.with_structured_output(EmailMessage)

    messages = [
        {"role": "system", "content": "You are a helpful assistant for research and composeing plaintext emails. Do not use markdown or html in the response use plain text only."},
        {"role": "human", "content": f"{query}. Do not use markdown or html in the response use plain text only."},
    ]

    return llm.invoke(messages)