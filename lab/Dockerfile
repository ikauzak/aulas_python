FROM python:3.7.2-alpine3.8 as source
FROM source as builder
COPY requirements/requirements.prod /tmp/
RUN pip install --upgrade --install-option="--prefix=/app" -r /tmp/requirements.prod


FROM source
COPY --from=builder /app /app
COPY app/* /app/app.py
WORKDIR /app
RUN chmod 777 app.py
CMD ["python3", "app.py"]
