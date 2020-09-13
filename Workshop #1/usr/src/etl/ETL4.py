import json
from connections.SourceConnection import SourceConnection
from connections.TargetConnection import TargetConnection
import http.client
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class ETL4:
    sourceConnection: None
    targetConnection: None
    imdbConnection: None
    imdbHeaders: None
    availableEndpoints: {}
    categories: []

    def __init__(self):
        self.sourceConnection = SourceConnection()
        self.targetConnection = TargetConnection()
        
        self.imdbConnection = http.client.HTTPSConnection("imdb8.p.rapidapi.com")
        self.imdbHeaders = {
            'x-rapidapi-host': "imdb8.p.rapidapi.com",
            'x-rapidapi-key': "fee7fa13a7mshd61881af4799557p172871jsndb85a36967f3"
        }

        self.categories = []

        self.availableEndpoints = {
            "Action": "%252Fchart%252Fpopular%252Fgenre%252Faction",
            "Animation": "%252Fchart%252Fpopular%252Fgenre%252Fanimation",
            "Comedy": "%252Fchart%252Fpopular%252Fgenre%252Fcomedy",
            "Documentary": "%252Fchart%252Fpopular%252Fgenre%252Fdocumentary",
            "Drama": "%252Fchart%252Fpopular%252Fgenre%252Fdrama",
            "Family": "%252Fchart%252Fpopular%252Fgenre%252Ffamily",
            "Horror": "%252Fchart%252Fpopular%252Fgenre%252Fhorror",
            "Music": "%252Fchart%252Fpopular%252Fgenre%252Fmusic",
            "Sci-Fi": "%252Fchart%252Fpopular%252Fgenre%252Fsci_fi",
            "Sport": "%252Fchart%252Fpopular%252Fgenre%252Fsport",
        }
    
    def startETL4(self):
        rows_upload: []
        self.loadCategories()

        self.loadTemporaryTable()

        for category in self.categories:
            top5Sakila = self.getTop5PerCategorySakila(category)
            top5IMDb = self.getTop5PerCategoryIMDb(category)

            for i in range(len(top5Sakila)):
                query_insert = ("INSERT INTO top_5_popularity_comparison " +
                    "(sakila_film_title, sakila_film_popularity, sakila_category, imdb_film_title, imdb_film_popularity, imdb_film_category) VALUES (" +
                    "'"+ top5Sakila[i][0] +"', "+
                    ""+ str(top5Sakila[i][1]) +","+
                    "'"+ (top5Sakila[i][2]) +"',"+
                    "'"+ (top5IMDb[i][0]) +"',"+
                    ""+ str(top5IMDb[i][1]) +","+
                    "'"+ (top5IMDb[i][2]) +"'"+
                    ");")

                self.targetConnection.runQuery(query_insert)
                self.targetConnection.commitChanges()
    
    def getPopularMoviesByCategoryIMDb(self, category):
        self.imdbConnection.request(
            "GET", 
            "/title/get-popular-movies-by-genre?genre=" + category, 
            headers=self.imdbHeaders)

        res = self.imdbConnection.getresponse()
        data = res.read()

        movies = json.loads(data.decode("utf-8"))

        return movies

    def getMovieDetailsIMDb(self, name):
        self.imdbConnection.request(
            "GET", 
            "/title/get-details?tconst="+name, 
            headers=self.imdbHeaders)

        res = self.imdbConnection.getresponse()
        data = res.read()

        movie = json.loads(data.decode("utf-8"))

        return movie
    
    def getRatingsPerMovieIMDb(self, name):
        self.imdbConnection.request(
            "GET", 
            "/title/get-ratings?tconst="+name, 
            headers=self.imdbHeaders)

        res = self.imdbConnection.getresponse()
        data = res.read()

        movie = json.loads(data.decode("utf-8"))

        return movie

    def loadCategories(self):
        query_categories = "SELECT name FROM category"

        categories = self.sourceConnection.runQuery(query_categories)
        
        for category in categories:
            self.categories.append(category[0])
    
    def loadTemporaryTable(self):
        query_temporary = """ 
        CREATE TEMPORARY TABLE top_5_popularity_comparison
            (SELECT film.title, film.rental_rate, category.name as category
                FROM film 
                LEFT JOIN film_category ON (film.film_id = film_category.film_id)
                LEFT JOIN category ON (film_category.category_id = category.category_id)
                
                ORDER BY name ASC, rental_rate DESC);
        """

        self.sourceConnection.runQuery(query_temporary)
    
    def getTop5PerCategorySakila(self, category):
        query_top = "SELECT * FROM top_5_popularity_comparison WHERE category = '"+category+"' LIMIT 0, 5;"

        top5 = self.sourceConnection.runQuery(query_top)
        
        return top5
    
    def getTop5PerCategorySakila(self, category):
        query_top = "SELECT * FROM top_5_popularity_comparison WHERE category = '"+category+"' LIMIT 0, 5;"

        top5 = self.sourceConnection.runQuery(query_top)
        
        return top5
    
    def getTop5PerCategoryIMDb(self, category):
        if category in self.availableEndpoints.keys():
            top5IMDb = []
            movies = self.getPopularMoviesByCategoryIMDb(self.availableEndpoints[category])
            
            for i in range(0,5):
                movie_id = movies[i].split("/")

                movie = self.getMovieDetailsIMDb(movie_id[2])
                rating = self.getRatingsPerMovieIMDb(movie_id[2])

                title = movie['title'] if 'title' in rating.keys() else 'NULL'
                rate = (int(rating['rating'])/2) if 'rating' in rating.keys() else 'NULL'

                movie_row = (title, rate, category)    
                
                top5IMDb.append(movie_row)
            
            return top5IMDb
        return [
            ('NULL', 'NULL', category),
            ('NULL', 'NULL', category),
            ('NULL', 'NULL', category),
            ('NULL', 'NULL', category),
            ('NULL', 'NULL', category)
            ]
    
    