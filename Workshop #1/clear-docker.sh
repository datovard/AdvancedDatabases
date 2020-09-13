docker stop workshop1_etl-runner_1 workshop1_mysql-target_1 workshop1_mysql-source_1
docker rm workshop1_etl-runner_1 workshop1_mysql-target_1 workshop1_mysql-source_1
docker volume prune -f
docker image rm workshop1_etl-runner workshop1_mysql-target workshop1_mysql-source