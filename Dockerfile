# This Dockerfile is used to deploy a simple single-container Reflex app instance.
FROM python:3.11

WORKDIR /app
COPY . .

ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3.11 -m venv $VIRTUAL_ENV

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD reflex run --env prod --backend-only

# FROM ubuntu:latest
LABEL authors="Miriam Durán"

# ENTRYPOINT ["top", "-b"]

# ?Lanzar 'docker build -t reflex-web:latest .' tras crear el DockerFile para crear la imagen
# ?Se runea inicialmente con 'docker run -p 8000:8000 --name app reflex-web:latest' para crear el contenedor, sólo exponemos el puerto del back