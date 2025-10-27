FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Instalar dependencias del proyecto
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar el código
COPY . /app

# Exponer puertos que usa la aplicación (app:8000, green_app:8001)
EXPOSE 8000 8001

# Por defecto arrancamos la aplicación principal; docker-compose puede sobreescribir el comando para otros servicios
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
