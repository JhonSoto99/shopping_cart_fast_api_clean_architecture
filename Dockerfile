# Especifica versión de python para el contenedor.
FROM python:3.12

# Espacio de trabajo dentro del contenedor.
WORKDIR /app

# Copear el archivo de requemimientos de local al entorno.
COPY requirements.txt /app/requirements.txt

# Instalar dependencias dentro del entorno
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copear código base
COPY . /app

# Exponer el puerto 80.
EXPOSE 80

CMD ["uvicorn", "app.drivers.rest.main:app", "--reload", "--host", "0.0.0.0", "--port" , "80"]