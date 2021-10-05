# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBUTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /djangoforprofessionals

# Install dependencies
COPY Pipfile Pipfile.lock /djangoforprofessionals/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /djangoforprofessionals