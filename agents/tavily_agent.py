from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain import hub
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)

def tavily_agent():
    instructions = """You are an assistant."""
    base_prompt = hub.pull("langchain-ai/react-agent-template")
    prompt = base_prompt.partial(instructions=instructions)
    llm = ChatOpenAI(temperature=0)
    tools = [TavilySearchResults()]
    agent = create_react_agent(llm, tools, prompt)
    
    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
    )