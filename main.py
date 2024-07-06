from typing import Any
from dotenv import load_dotenv
from langchain import hub
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from agents.python_agent import python_agent
from agents.tavily_agent import tavily_agent
import streamlit as st
from streamlit_chat import message

from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain_community.callbacks.streamlit import (
    StreamlitCallbackHandler,
)
from langchain_community.chat_message_histories import (
    StreamlitChatMessageHistory,
)

load_dotenv()
history = StreamlitChatMessageHistory(key="chat_history")

if len(history.messages) == 0:
    history.add_ai_message("Hi, I'm Tina. How can I help you?")
st_callback = StreamlitCallbackHandler(st.container())

def main():
    print("Start...")
    st.title("💬 Multi-Agent Chatbot")
    base_prompt = hub.pull("langchain-ai/react-agent-template")
    
    view_messages = st.expander("View the message contents in session state")
    for msg in history.messages:
        st.chat_message(msg.type).write(msg.content)
    
    def tavily_agent_executer_wrapper(original_prompt: str) -> dict[str, Any]:
        return tavily_agent_executer.invoke({"input": original_prompt, "chat_history": history.messages})
    
    def python_agent_executer_wrapper(original_prompt: str) -> dict[str, Any]:
        return python_agent_executer.invoke({"input": original_prompt, "chat_history": history.messages})
    
    python_agent_executer = python_agent()
    tavily_agent_executer = tavily_agent()
    
    tools = [
        Tool(
            name="Python Agent",
            func=python_agent_executer_wrapper,
            description="""useful when you need to transform natural language to python and execute the python code,
                          returning the results of the code execution
                          DOES NOT ACCEPT CODE AS INPUT""",
        ),
        Tool(
            name="Tavily Agent",
            func=tavily_agent_executer_wrapper,
            description="""useful when you need to answer general knowledge questions,
                        which you can't answer by yourself, you can use this tool to seach on web to get the accurate
                        result """,
        ),
    ]

    prompt = base_prompt.partial(instructions="Your name is Tina and You are a helpful agent with access to several tools, including Python agent and Tavily Agent . For questions about Programming, You should use the Python agent tool. For general knowledge questions, You should use the Tavily Agent tool.")
    grand_agent = create_react_agent(
        prompt=prompt,
        llm=ChatOpenAI(temperature=0, model="gpt-4-turbo"),
        tools=tools,
    )
    grand_agent_executor = AgentExecutor(agent=grand_agent, tools=tools, verbose=True)
    
    if prompt := st.chat_input():
        st.chat_message("user").write(prompt)
        st_callback = StreamlitCallbackHandler(st.container())
        response = grand_agent_executor.invoke(
            {
                "input": prompt,
                "chat_history": history.messages
            },
            {"callbacks": [st_callback]}
        )
        history.add_user_message(prompt)
        history.add_ai_message(response["output"])
        st.chat_message("ai").write(response["output"])


if __name__ == "__main__":
    main()
