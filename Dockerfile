FROM python:3.13.3-alpine3.21

RUN addgroup -S appuser && adduser -S appuser -G appuser
RUN apk add --no-cache \
    mariadb-dev \
    gcc \
    musl-dev \
    python3-dev
USER appuser
WORKDIR /app/
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=appuser:appuser . .
EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]