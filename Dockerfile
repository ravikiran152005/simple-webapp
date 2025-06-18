FROM python:3.10-slim

# Install MySQL client dependencies
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev gcc \
    && apt-get clean

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["python", "app.py"]