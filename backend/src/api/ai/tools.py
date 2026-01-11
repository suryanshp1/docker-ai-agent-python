from langchain_core.tools import tool
from api.emailer.sender import send_mail
from api.emailer.inbox_reader import read_inbox
from api.ai.services import generate_email_messages

@tool
def send_mail(subject: str, content: str) -> str:
    """
    Send me an email with the given subject and content.

    Args:
        subject: The subject of the email
        content: The content of the email

    Returns:
        str: A message indicating whether the email was sent successfully or not
    """
    try:
        send_mail(subject, content)
        return "Email Sent Successfully"
    except Exception as e:
        return f"Email Not Sent | Error: {str(e)}"


@tool
def get_unread_emails(hours_ago: int = 48) -> str:
    """
    Get my unread emails from the inbox.

    Args:
        hours_ago: Number of hours to look back from now

    Returns:
        List of my unread emails seperated by ---
    """
    try:
        emails = read_inbox(hours_ago=hours_ago, verbose=False)
        cleaned = []
        for email in emails:
            data = email.copy()
            if "html_body" in data:
                data.pop("html_body")
            msg = ""
            for k, v in data.items():
                msg += f"{k}:\t{v}\n"
            cleaned.append(msg)
        return "---\n".join(cleaned)[:500]
    except Exception as e:
        return f"Error: {str(e)}"

@tool
def research_email(query: str) -> str:
    """
    Research the given query and return the result.

    Args:
        query: The query to research

    Returns:
        str: The result of the research
    """
    try:
        return generate_email_messages(query)
    except Exception as e:
        return f"Error: {str(e)}"