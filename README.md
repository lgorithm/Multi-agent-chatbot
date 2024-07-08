# Multi-Agent Chatbot

**Multi-Agent Chatbot** is a sophisticated chatbot application that leverages multiple agents to handle different types of queries. It integrates with LangChain, OpenAI, and various tools to deliver accurate and helpful responses. This application is built using Streamlit and is deployed on Google Kubernetes Engine with continuous integration using GitHub Actions. Monitoring is facilitated through Langsmith.

## Features

- **Python Agent**: Executes Python code to answer programming-related questions.
- **Tavily Agent**: Uses web search to answer general knowledge questions.
- **Streamlit Interface**: Interactive UI for querying and viewing responses.
- **Multi-Agent Integration**: Utilizes different agents for specialized tasks.
- **CI/CD**: Automatically deploy updates to Google Kubernetes Engine on code push.
- **Monitoring**: Integrated with Langsmith for monitoring LLM application.

## Prerequisites

- Python 3.10+
- Poetry (for dependency management)
- Streamlit
- LangChain
- Pinecone (with API key)
- OpenAI API key

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/lgorithm/Multi-agent-chatbot.git
    cd Multi-agent-chatbot
    ```

2. **Install dependencies**:
    ```sh
    poetry install
    ```

3. **Set up environment variables**:
    Create a `.env` file in the project root and add your API keys and other necessary environment variables:
    ```env
    OPENAI_API_KEY=
    TAVILY_API_KEY=
    LANGCHAIN_API_KEY=
    LANGCHAIN_PROJECT=
    LANGCHAIN_TRACING_V2=
    ```

4. **Run the application locally**:
    ```sh
    streamlit run main.py
    ```

## Docker

To run the application using Docker:

1. **Build the Docker image**:
    ```sh
    docker build -t multi-agent-chatbot:latest .
    ```

2. **Run the Docker container**:
    ```sh
    docker run -p 8501:8501 --env-file .env multi-agent-chatbot:latest
    ```

## Deployment

This project uses GitHub Actions for continuous deployment. On pushing code to the `develop` branch, the application is automatically built and deployed to Google Kubernetes Engine.

### Google Kubernetes Engine Deployment

1. **Ensure you have a GKE cluster running**.
2. **Set up GitHub Actions**:
   - Configure secrets in your GitHub repository for GKE credentials and other necessary environment variables.

## Monitoring

Langsmith is integrated for monitoring the performance and usage of the LLM application.

