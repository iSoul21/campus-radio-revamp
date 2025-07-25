FROM python:3.11-slim

WORKDIR /app

COPY server/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY server/ ./

EXPOSE 8080

ENV FLASK_APP=app.py

CMD ["python", "app.py"]