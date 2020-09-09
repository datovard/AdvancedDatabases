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

## How to run the ETL's

The ETL's are written in Python code, to execute it you have to run this command

	docker-compose -f .\docker-compose-etl.yml up

Remember to wait for the database instances to be up first, just give them a minute.

## (Sakila) source database definition

Here you can find a diagram of the Sakila database with 16 tables between films, actors, customers, staff, stores and rentals of a DVD rental chain store. 

![alt text](./misc/Sakila_database.PNG "Database diagram")

## ETL operations definitions

1. We want to know which category of movies most viewed in each city anually and
   We want to know which category of movies most viewed in each country anually

2. We want to know which film is getting the most unreturned rentals, the total cost of replacement of those copies and how much it was lost on those rentals

3. We want to know the top five most popular movies per category and contrast it with an external movie database

4. ?

## ETL description table

|        | Extraction sources                                                                                                                                                                                                 | Transformations made on the data                                                                                                                                                                                           | Loaded fields                                                                                                                                                                                                                     |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ETL #1 | - Sakila Database tables used :<br/>     * rental<br/>     * inventory<br/>     * film<br/>     * film_category<br/>     * category<br/>     * customer<br/>     * address<br/>     * city<br/>     * country<br/> | - Calculating count of rentals as total of rentals<br/> - Extraction of maximum of total of rentals<br/>                                                                                                                   | - rents_by_category_city_and_year:<br/>     * rental<br/>     * year<br/>     * category<br/>     * city<br/> - rents_by_category_country_and_year:<br/>     * rental<br/>     * year<br/>     * category<br/>     * country<br/> |
| ETL #2 | - Sakila Database tables used:<br/>     * rental<br/>     * inventory<br/>     * film<br/>     * payment<br/>                                                                                                      | - Calculating count of rentals as total of rentals<br/> - Aggregation of payment per rental to calculate the total rental lost<br/> - Aggregation of cost of replacement per copy to calculate total replacement cost<br/> | - money_lost_on_rentals:<br/>     * total_copies_lost<br/>     * title<br/>     * total_rental_lost<br/>     * total_replacement_lost<br/>                                                                                        |
| ETL #3 | - Sakila Database tables used:<br/>     * film<br/>     * film_category<br/>     * category<br/>                                                                                                                   | - Aggregation of data between Sakila database and IMDb Open API                                                                                                                                                            | - top_5_popularity_comparison<br/>     * sakila_film_title<br/>     * sakila_film_popularity<br/>     * sakila_category<br/>     * imdb_film_title<br/>     * imdb_film_popularity<br/>     * imdb_film_category<br/>             |