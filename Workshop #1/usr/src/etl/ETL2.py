from connections.SourceConnection import SourceConnection
from connections.TargetConnection import TargetConnection

class ETL2:
    sourceConnection: None
    targetConnection: None

    def __init__(self):
        self.sourceConnection = SourceConnection()
        self.targetConnection = TargetConnection()
    
    def startETL2(self):
        self.startTemporalDatabases()
        self.startTransformationsAndLoads()
    
    def startTemporalDatabases(self):
        query = """
        CREATE TEMPORARY TABLE rents_by_category_country_and_year
        (SELECT COUNT(rental.rental_date) as rental, YEAR(rental.rental_date)as year, category.name as category, country.country as country
            FROM rental 
            LEFT JOIN inventory ON(rental.inventory_id = inventory.inventory_id)
            LEFT JOIN film ON (inventory.film_id = film.film_id)
            LEFT JOIN film_category ON (film.film_id = film_category.film_id)
            LEFT JOIN category ON (film_category.category_id = category.category_id)
            LEFT JOIN customer ON (rental.customer_id = customer.customer_id)
            LEFT JOIN address ON ( customer.address_id = address.address_id )
            LEFT JOIN city ON (address.city_id = city.city_id)
            LEFT JOIN country ON (city.country_id = country.country_id)
            GROUP BY country, category, year ORDER BY country ASC, year DESC, rental DESC);"""

        self.sourceConnection.runQuery(query)

    def startTransformationsAndLoads(self):
        query = "SELECT COUNT(*) FROM rents_by_category_country_and_year;"

        results = self.sourceConnection.runQuery(query)
        row_count = results[0][0]
        rounds = int(row_count/1000) + 1

        for i in range(0, rounds):
            query = "SELECT MAX(rental) as rental, country, year FROM rents_by_category_country_and_year GROUP BY year, country ORDER BY country ASC, year DESC"
            query += " LIMIT " + str(i * 1000) + ", 1000"

            results = self.sourceConnection.runQuery(query)
            
            for j in results:
                query_category = "SELECT category FROM rents_by_category_country_and_year WHERE year = " + str(j[2]) + " AND country = '" + j[1] + "' AND rental = "+ str(j[0]) +";"
                
                categories = self.sourceConnection.runQuery(query_category)

                for category in categories:
                    query_insert = "INSERT INTO rents_by_category_country_and_year (rental, year, category, country) VALUES ("+str(j[0])+", "+str(j[2])+", '"+category[0]+"', '"+j[1]+"' )"

                    self.targetConnection.runQuery(query_insert)
                    self.targetConnection.commitChanges()