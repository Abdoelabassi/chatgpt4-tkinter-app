FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y libx11-6 libxext-dev libxrender-dev libxinerama-dev libxi-dev libxrandr-dev libxcursor-dev libxtst-dev tk-dev && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip && \
	pip install --no-cache-dir openai customtkinter

CMD ["python", "chatgpt.py"]
