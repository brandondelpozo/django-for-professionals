# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONBUFFERED 1

# Set work directory
WORKDIR /djangoforprofessionals

# Install dependencies
COPY Pipfile Pipfile.lock /djangoforprofessionals/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /djangoforprofessionals/