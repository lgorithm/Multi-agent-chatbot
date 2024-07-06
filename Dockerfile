FROM python:3.10
WORKDIR  /app
COPY pyproject.toml main.py /app/
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
COPY /agents /app/agents
EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD [ "main.py", "--server.port=8501", "--server.address=0.0.0.0"]