# Build the Frontend
FROM node:latest AS uibuilder

WORKDIR /uibuild

COPY ./frontend /uibuild

RUN yarn install
RUN yarn run build

# Dockerfile for WordWall
FROM python:3.12

WORKDIR /server

COPY ./requirements.txt /server/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

COPY ./wordwall /server

# Copy React Files
COPY --from=uibuilder /wordwall /server

CMD ["uvicorn", "wordwall.main:app", "--host", "0.0.0.0", "--port", "80", "--forwarded-allow-ips", "'*'"]
