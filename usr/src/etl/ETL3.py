from connections.SourceConnection import SourceConnection
from connections.TargetConnection import TargetConnection

class ETL3:
    sourceConnection: None
    targetConnection: None

    def __init__(self):
        self.sourceConnection = SourceConnection()
        self.targetConnection = TargetConnection()
    
    def startETL3(self):
        self.startTransformationsAndLoads()
    
    def startTransformationsAndLoads(self):
        query_count = "SELECT COUNT(*) FROM rental WHERE return_date IS NULL;"
        
        count = self.sourceConnection.runQuery(query_count)
        row_count = count[0][0]
        rounds = int(row_count/1000) + 1

        for i in range(0, rounds):
            query_costs = """
            SELECT COUNT(rental.rental_id) as total_copies_lost, film.title, SUM(payment.amount) as total_rental_lost, SUM(film.replacement_cost) as total_replacement_cost
                FROM rental 
                LEFT JOIN inventory ON(rental.inventory_id = inventory.inventory_id)
                LEFT JOIN film ON(inventory.film_id = film.film_id)
                LEFT JOIN payment ON(rental.rental_id = payment.payment_id)
                WHERE return_date IS NULL
                GROUP BY film.title, film.special_features ORDER BY total_copies_lost DESC, total_replacement_cost DESC;"""
            
            costs = self.sourceConnection.runQuery(query_costs)

            for cost in costs:
                query_insert = "INSERT INTO money_lost_on_rentals (total_copies_lost, title, total_rental_lost, total_replacement_cost) VALUES "
                query_insert += "(" + str(cost[0]) + ", '" + cost[1] + "', " + str(cost[2]) + ", " + str(cost[3]) + ")"

                self.targetConnection.runQuery(query_insert)

                self.targetConnection.commitChanges()


    
    