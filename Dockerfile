FROM python:3.9-slim

WORKDIR /app

# TODO: copy files
COPY ...

RUN pip install --upgrade pip

#TODO: install dependencies
RUN pip install --no-cache-dir ...

EXPOSE 8000

#TODO: add missed parameters to the CMD 
CMD ["...", "...", "--host", "0.0.0.0", "--port", "8000"]