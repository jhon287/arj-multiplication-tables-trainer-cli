FROM python:3-alpine

WORKDIR /app

COPY src/* /app/

ENTRYPOINT [ "python", "main.py" ]

CMD [ "--help" ]
