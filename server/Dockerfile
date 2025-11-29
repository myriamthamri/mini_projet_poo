FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app/server/

ENV PYTHONPATH="/app"

EXPOSE 5000

CMD ["python", "-m", "server.server"]