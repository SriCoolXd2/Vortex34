FROM python:3.10.8-slim
WORKDIR /app
RUN apt-get update && apt-get install -y git
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
CMD ["python", "-m", "Vortex"]
