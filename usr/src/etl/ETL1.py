from connections import SourceConnection, TargetConnection

class ETL1:
    sourceConnection: None
    targetConnection: None

    def __init__(self):
        self.sourceConnection = SourceConnection()
        self.targetConnection = TargetConnection()
    
    def startETL1(self):
        self.startTemporalDatabases()
    
    def startTemporalByCity(self):
        query = """
        CREATE TEMPORARY TABLE rents_by_category_city_and_year
        (SELECT COUNT(rental.rental_date) as rental, YEAR(rental.rental_date)as year, category.name as category, city.city as city
            FROM rental 
            LEFT JOIN inventory ON(rental.inventory_id = inventory.inventory_id)
            LEFT JOIN film ON (inventory.film_id = film.film_id)
            LEFT JOIN film_category ON (film.film_id = film_category.film_id)
            LEFT JOIN category ON (film_category.category_id = category.category_id)
            LEFT JOIN customer ON (rental.customer_id = customer.customer_id)
            LEFT JOIN address ON ( customer.address_id = address.address_id )
            LEFT JOIN city ON (address.city_id = city.city_id)
            GROUP BY city, category, year ORDER BY city ASC, year DESC, rental DESC);"""

        self.sourceConnection.runQuery(query)
    
    def startTemporalByCountry(self):
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
    

    def transformAndLoadByCity(self):
        query = """
        SELECT COUNT(*) FROM rents_by_category_city_and_year;"""

        results = self.sourceConnection.runQuery(query)
        row_count = results[0][0]



    def startTemporalDatabases(self):
        self.startTemporalByCity()
        self.startTemporalByCountry()

        self.transformAndLoadByCity()



        