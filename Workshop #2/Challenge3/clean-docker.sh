docker rm sqlserver2019
docker rmi mcr.microsoft.com/mssql/server
docker volume prune -f