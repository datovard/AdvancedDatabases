FROM mcr.microsoft.com/mssql/server:2019-CU5-ubuntu-16.04

COPY ./config/db/challenge-3-schema.sql .

RUN sqlcmd -i challenge-3-schema.sql