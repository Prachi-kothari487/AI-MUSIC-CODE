FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY AI-music-recommender-main/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir "fastapi>=0.100.0" "uvicorn[standard]>=0.23.0"

COPY AI-music-recommender-main/ ./AI-music-recommender-main/
COPY inference.py ./inference.py

EXPOSE 8000

CMD ["uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "8000", "--no-access-log"]
