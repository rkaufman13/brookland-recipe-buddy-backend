FROM python:3.12.16-bookworm
RUN apt-get update \
    && apt-get install -y libxml2 libffi-dev
WORKDIR /app
COPY requirements.txt ./
COPY app/ ./
COPY .env ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "start.py"]