FROM python:3.11-slim

# Set some global variables to be used across the Dockerfile
ARG WORKDIR="/www"
ARG APPNAME="app"

# Set the working directory to a secure non-root location
WORKDIR /home/${APPNAME}${WORKDIR}

# Configure Python to not buffer "stdout" or create .pyc files
ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install and configure poetry to manage the dependencies
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY ./pyproject.toml ./poetry.lock* /home/${APPNAME}${WORKDIR}/

# Install the runtime dependencies using poetry
RUN bash -c "poetry install --no-root;"

# Copy the source code to the container
COPY . .

# Expose the port used by the application so that its accessible outside the container
EXPOSE 8000
