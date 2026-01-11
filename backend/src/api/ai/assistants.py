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
        {"role": "system", "content": f"You are a helpful assistant that can send and read emails. You have access to tools: {list(EMAIL_TOOLS.keys())}. ALWAYS use the tools when the user asks to perform an action or get information. Do not answer from your own knowledge if a tool can provide the answer. If the user asks to send an email but does not provide a specific subject or content, YOU MUST GENERATE appropriate and professional content based on the user's intent. Do not ask for clarification unless the request is completely ambiguous."},
        {"role": "human", "content": f"{query}."},
    ]

    response = llm.invoke(messages)
    messages.append({"role": "assistant", "content": response.content})

    if hasattr(response, "tool_calls") and response.tool_calls:
        for tool_call in response.tool_calls:
            tool_name = tool_call.get("name")
            tool_func = EMAIL_TOOLS.get(tool_name)
            tool_args = tool_call.get("args")
            if not tool_func:
                continue
            tool_result = tool_func.invoke(tool_args)
            messages.append({"role": "tool", "content": tool_result, "tool_call_id": tool_call.get("id")})
        final_response = llm.invoke(messages)
        return final_response
    
    return response