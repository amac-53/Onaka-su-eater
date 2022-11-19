FROM python:3.10

RUN pip install "fastapi[all]" requests
WORKDIR /backend

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]