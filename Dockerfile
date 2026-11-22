FROM python:3.12.16-bookworm
RUN apt-get update \
    && apt-get install -y libxml2 libffi-dev
WORKDIR /app
COPY requirements.txt ./
COPY app/ ./

ENV ADMIN_EMAIL $ADMIN_EMAIL
ENV GITHUB_API_KEY $GITHUB_API_KEY

RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "start.py"]