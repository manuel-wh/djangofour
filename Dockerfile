# Usar una imagen base oficial de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requerimientos
COPY Pipfile Pipfile.lock /app/

# Instalar pipenv y las dependencias del proyecto
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

# Copiar el resto del código del proyecto
COPY . /app/

# Exponer el puerto que usará el servidor de desarrollo
EXPOSE 8000

# Comando para ejecutar el servidor de desarrollo
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]