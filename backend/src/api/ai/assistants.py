from .llms import get_openai_llm
from .tools import send_mail, get_unread_emails


EMAIL_TOOLS = {
    "send_mail": send_mail,
    "get_unread_emails": get_unread_emails
}


def email_assistant(query: str):
    llm_base = get_openai_llm()
    llm = llm_base.bind_tools(list(EMAIL_TOOLS.values()))

    messages = [
        {"role": "system", "content": f"You are a helpful assistant that can send and read emails. You have access to tools: {list(EMAIL_TOOLS.keys())}. ALWAYS use the tools when the user asks to perform an action or get information. Do not answer from your own knowledge if a tool can provide the answer."},
        {"role": "human", "content": f"{query}."},
    ]

    return llm.invoke(messages)