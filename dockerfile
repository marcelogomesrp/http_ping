FROM python:3.10-alpine
RUN echo "2"
WORKDIR /app
COPY requirements.txt /app
COPY requirements-dev.txt /app
RUN pip install -r /app/requirements-dev.txt
COPY ./src/. /app/
#CMD ["/usr/local/bin/python", "/app/app.py"]
ENTRYPOINT ["/usr/local/bin/python", "/app/app.py"]

