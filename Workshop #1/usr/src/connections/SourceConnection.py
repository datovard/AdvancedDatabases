import mysql.connector

class SourceConnection:
    hostname = 'mysql-source'
    database='sakila'
    username='root'
    password='secret'
    connection=None

    def __init__(self):
        self.startConnection()
    
    def __del__(self):
        self.closeConnection()

    def startConnection(self):
        self.connection = mysql.connector.connect(
                                            host=self.hostname,
                                            database=self.database,
                                            user=self.username,
                                            password=self.password
                                            )
        if self.connection.is_connected():
            db_Info = self.connection.get_server_info()
    
    def closeConnection(self):
        if (self.connection.is_connected()):
            self.connection.close()

    def runQuery(self, query):
        cursor = self.connection.cursor()

        cursor.execute(query)

        if cursor.rowcount <= 0:
            result = cursor.fetchall()
        else:
            result = None

        cursor.close()

        return result