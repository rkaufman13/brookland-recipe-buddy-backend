FROM python:3.12-slim
RUN apt-get update \
    && apt-get install -y libxml2 libffi-dev
WORKDIR /app
COPY requirements.txt ./
COPY start.py ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "start.py"]