FROM python:3.10
COPY . /sun_api_data_two
WORKDIR /sun_api_data_two

ENV DB_HOST=${DB_HOST}
ENV MYSQL_USER=${MYSQL_USER}
ENV MYSQL_DB_NAME=${MYSQL_DB_NAME}
ENV MYSQL_PASSWORD=${MYSQL_PASSWORD}
ENV MYSQL_PORT=${MYSQL_PORT}
ENV API_TOKEN=${API_TOKEN}

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
