FROM python:3.9.13-slim

RUN python3 -m venv /opt/venv

CMD ["mkdir", "/app/backend/"]

WORKDIR /app/backend

COPY backend .

RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r /app/backend/requirements.txt && \
    chmod +x /app/backend/entrypoint.sh

CMD ["/app/backend/entrypoint.sh"]