# Sakila ETL Workshop

Welcome!, this is my workshop to get to know how *Extraction*, *Tranformation* and *Load* operations work for business intelligence purposes. In here, we are using the Sakila sample database of MySQL as our data source, you can find more [here](https://dev.mysql.com/doc/sakila/en/).

## Running the data source on Docker

This project has automatized the databases on a Docker instance, you just have to run this command on your local machine:

	docker-compose up -d

Wait for the MySQL instances and databases to finish is initial load and connect to it with any Database Administration Software you want (For example, MySQL Workbench).

To connect to the **source** database, use this values:

	Hostname: localhost or 127.0.0.1
	Port: 33060
	Username: root
	Password: secret

To connect to the **target** database, use this values:

	Hostname: localhost or 127.0.0.1
	Port: 33061
	Username: root
	Password: secret

## (Sakila) source database definition

Here you can find a diagram of the Sakila database with 16 tables between films, actors, customers, staff, stores and rentals of a DVD rental chain store. 

![alt text](./misc/Sakila_database.PNG "Database diagram")

## ETL operations requirements and definitions

1. Contrastar popularidad de las peliculas con bases de datos alternativas (Rotten Tomatoes, IMdb)

2. Relación entre rentabilidad y actor respecto a premiaciones

3. Promedio de dinero perdido por ciudad o país, anualmente

4. Géneros más vistos por ciudad o país, anualmente

5. Géneros más rentables por ciudad, país, anualmente, mensualmente



