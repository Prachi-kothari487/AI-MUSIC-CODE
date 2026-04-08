FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY AI-music-recommender-main/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir "openai>=1.0.0" "requests>=2.28.0" \
    && pip install --no-cache-dir "fastapi>=0.100.0" "uvicorn[standard]>=0.23.0"

COPY AI-music-recommender-main/ ./AI-music-recommender-main/
COPY inference.py ./inference.py

EXPOSE 7860

CMD ["python", "inference.py"]
