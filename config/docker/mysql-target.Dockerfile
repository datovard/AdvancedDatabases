FROM mysql:8.0.19

# Add the content of the sql-scripts/ directory to your image
# All scripts in docker-entrypoint-initdb.d/ are automatically
# executed during container startup
COPY ./config/db/target-schema.sql /docker-entrypoint-initdb.d/