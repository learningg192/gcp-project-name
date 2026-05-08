FROM python:3.10

WORKDIR /app

# copy backend
COPY backend/ /app/backend/

# copy frontend
COPY frontend/ /app/frontend/

RUN pip install --no-cache-dir -r /app/backend/requirements.txt

EXPOSE 80

CMD ["python", "/app/backend/app.py"]