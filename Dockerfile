FROM python:3.11.3-alpine3.18

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY ./requirements.txt /mindfulness/requirements.txt
COPY ./mindfulness /mindfulness
COPY ./scripts /scripts

WORKDIR /mindfulness
EXPOSE 8000

RUN apk update && \
    apk add --no-cache \
        postgresql-dev linux-headers gcc libc-dev && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt && \
    mkdir -p /vol/static && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts/run.sh

ENV PATH="/scripts:/py/bin:$PATH"

CMD ["run.sh"]
