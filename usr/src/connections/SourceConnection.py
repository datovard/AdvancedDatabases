class SourceConnection:
    hostname = 'mysql-source'
    database='sakila'
    username='root'
    password='secret'
    connection=None

    def startConnection(self):
        try:
            connection = mysql.connector.connect(host='mysql-source',
                                                database='sakila',
                                                user='root',
                                                password='secret'
                                                )
            if connection.is_connected():
                db_Info = connection.get_server_info()

        except Error as e:
            print("Error while connecting to MySQL", e)
    
    def closeConnection(self):
        if (connection.is_connected()):
            cursor.close()
            connection.close()
