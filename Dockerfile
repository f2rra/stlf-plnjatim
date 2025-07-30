# Gunakan base image Python yang efisien
FROM python:3.11-slim

# Set working directory di dalam kontainer
WORKDIR /app

# Salin file requirements dan install dependensi
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Salin folder aplikasi dan model ke dalam kontainer
COPY ./app /app
COPY ./model /model

# Ekspos port yang akan digunakan oleh FastAPI
EXPOSE 8000

# Perintah untuk menjalankan aplikasi menggunakan Uvicorn
# Ini akan menjalankan server API saat kontainer dimulai
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
