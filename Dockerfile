FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y upgrade \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt-get install -y \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash libms

RUN mkdir -p /app

COPY requirements.txt entrypoint.sh /app/

COPY . /app/

WORKDIR /app

RUN chown -R libms:libms /app \
    && chmod +x /app/entrypoint.sh

USER libms 

RUN pip3 install -r requirements.txt

ENV ENVIRONMENT=dev

CMD ["/app/entrypoint.sh"]
