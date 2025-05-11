# Stage 1: init
FROM python:3.11

# Copy local context to `/app` inside container (see .dockerignore)
WORKDIR /app
COPY . .

# Crear el entorno virtual que será copiado al contenedor final
ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3.11 -m venv $VIRTUAL_ENV

# Instalar dependencias
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: build
CMD reflex run --env prod --backend-only