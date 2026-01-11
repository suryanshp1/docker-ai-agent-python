from langgraph.prebuilt import create_react_agent
from api.ai.llms import get_openai_llm
from .tools import send_mail, get_unread_emails, research_email
from langgraph_supervisor import create_supervisor


EMAIL_TOOLS_LIST = [
    send_mail,
    get_unread_emails
]

def get_email_agent():
    
    agent = create_react_agent(
        model=get_openai_llm(),
        tools=EMAIL_TOOLS_LIST,
        prompt="you are a helpful assistant for managing my email inbox for generating, sending and reading emails.",
        name="email_agent"
    )

    return agent

def get_research_agent():
    
    agent = create_react_agent(
        model=get_openai_llm(),
        tools=[research_email],
        prompt="you are a helpful research assistant for preparing emails.",
        name="email_research_agent"
    )

    return agent

# supe = get_supervisor()
# supe.invoke({"messages" : [{"role": "user", "content": "find how to create a website and send me an email about that"}]})
def get_supervisor():
    model = get_openai_llm()
    supervisor = create_supervisor(
        agents=[get_email_agent(), get_research_agent()],
        model=model,
        prompt="you manage a email inbox manager agent and research agent. Assign tasks to them and monitor their progress."
    ).compile()

    return supervisor