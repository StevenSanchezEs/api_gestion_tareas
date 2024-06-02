# Usa una imagen base oficial de Python 3.12
FROM python:3.12-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt a la imagen
COPY requirements.txt /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación a la imagen
COPY . /app/

# Expone el puerto en el que correrá la aplicación
EXPOSE 5000

# Comando para correr la aplicación con honcho
CMD ["honcho", "start"]