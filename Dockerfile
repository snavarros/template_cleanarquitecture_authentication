FROM python:3.13-alpine

# Crear entorno virtual
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Instalar dependencias del sistema usando apk (en lugar de apt-get)
RUN apk update && apk add --no-cache \
    build-base \
    libpq \
    libffi-dev \
    postgresql-dev \
    gcc \
    musl-dev \
    && pip install --no-cache-dir --upgrade pip

# Copiar solo requirements para cacheo
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Crear carpeta de trabajo (el código se montará con volumen)
WORKDIR /app

COPY . .

# Comando de inicio
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]