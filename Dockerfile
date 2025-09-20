FROM python:3.12-slim

RUN pip install streamlit pandas pyarrow

COPY ./main.py /app/main.py

WORKDIR /app

ENTRYPOINT ["streamlit", "run", "main.py"]