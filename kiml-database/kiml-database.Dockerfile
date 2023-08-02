FROM postgres:12.2-alpine

COPY ./kiml-database/init_database.sql /docker-entrypoint-initdb.d