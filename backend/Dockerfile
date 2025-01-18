FROM python:3.11.8

WORKDIR /backend

COPY src/ ./src
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE ${BACKEND_CONTAINER_PORT}

CMD ["python", "-m", "src.app"]
