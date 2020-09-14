# Workshop #2: Multiple Data Warehouse Challenges

Welcome!, this is a workshop based on the design and creation of data warehouses, take a look on each of the challenges

## Challenge #1

Consultar el modelo E/R de la bases de datos Sakila de MySQL, y diseñar una
bodega de datos, siguiendo la metodología Kimball. Identificar los hechos,
granularidad, dimensiones, jerarquías de las dimensiones, y medidas. Identificar
dimensiones: junk, des-generadas, y que cambian lentamente. Identificar relaciones
muchos a muchos entre la Tabla de hechos y dimensiones para darles solución.

Having the Sakila database and its E/R model, design a data warehouse following the Kimball mehodology or Bottom-up data warehouse approach.

Identify: 
1. Facts
2. Granularity
3. Dimensions
	- Hierarchy of those dimensions
	- Junk
	- De-generated
	- Slow changing
4. Metrics. 

Additionally, identify many-to-many relations between facts and dimension tables to provide a solution.

## Challenge #2

A web business company records the data of each visit on the web (weblog file). A clickstream is every event that occurs on every web page on the company's servers. The clickstream contains a number of data such as the page, session, the referrer, etc. 

Your task is to identify the necessary transformation tasks, and model a data warehouse to generate statistics to connect this information to the web sales. It is recommend reviewing weblog files and [Google Analytics](https://analytics.google.com/analytics/web/provision/#/provision) and other [visualization tools](https://www.weblogexpert.com/sample/index.htm) to see the impact that the analysis of web information would have.

## Challenge #3

Go to [The Code Project](https://www.codeproject.com/Articles/652108/Create-First-Data-WareHouse) where you can find an example on how to create a data warehouse:

Before we start the challenge, all the needed files as the SQL script file for the database creation and the SQL script to run the resulting queries, even a format to run a Docker instance with SQL Server installed is provided on the folder **/Challenge3** of this workshop.

Your tasks are:
1. Follow the tutorial and create the data warehouse on any DBMS you want (Recommended: MySQL or PosgreSQL)
2. Run this queries:
	1. Total sales of each of the products per month during 2013:
	
	Resulting query

	```sql
	SELECT SUM(SalesTotalCost) as SalesTotalCostMonthly, MonthName 
		from FactProductSales 
		LEFT JOIN DimDate ON(FactProductSales.SalesDateKey = DimDate.DateKey) 
		WHERE DimDate.Year = 2013 
		GROUP BY DimDate.Year, DimDate.Month, DimDate.MonthName;
	```

	And some results:

	![alt text](./Challenge3/misc/Query-1.PNG "Sakila diagram")

	2. The best seller for each of the products during 2013:

	Resulting query

	```sql
	SELECT DISTINCT t1.TotalCost, t1.ProductName, t2.SalesPersonName  FROM 
		( SELECT MAX(SalesTotalCost) as TotalCost, ProductName FROM FactProductSales
			LEFT JOIN DimProduct ON (FactProductSales.ProductID = DimProduct.ProductKey)
			GROUP BY ProductName) as t1 

		INNER JOIN

		( SELECT SalesTotalCost, SalesPersonName FROM FactProductSales 
			LEFT JOIN DimSalesPerson ON (FactProductSales.SalesPersonID = DimSalesPerson.SalesPersonID)) as t2
		
		ON (t2.SalesTotalCost = t1.TotalCost)
		ORDER BY ProductName;
	```

	And some results:

	![alt text](./Challenge3/misc/Query-2.PNG "Query 2 result")

	3. Quantity of each product sold per month during 2013, in order of highest to lowest:

	Resulting query

	```sql
	SELECT SUM(Quantity) as TotalQuantity, ProductName, MonthName FROM 
		FactProductSales
		INNER JOIN DimDate ON (FactProductSales.SalesDateKey = DimDate.DateKey)
		INNER JOIN DimProduct ON (FactProductSales.ProductID = DimProduct.ProductKey)
		WHERE DimDate.Year = 2013
		GROUP BY MonthName, ProductName
		ORDER BY MonthName ASC, TotalQuantity DESC, ProductName;
	```

	And some results:

	![alt text](./Challenge3/misc/Query-3.PNG "Query 3 result")

	4. Quantity of each product sold per day (name of days) during 2013, in order of highest to lowest:

	Resulting query

	```sql
	SELECT SUM(Quantity) as TotalQuantity, ProductName, DayName FROM 
		FactProductSales
		INNER JOIN DimDate ON (FactProductSales.SalesDateKey = DimDate.DateKey)
		INNER JOIN DimProduct ON (FactProductSales.ProductID = DimProduct.ProductKey)
		WHERE DimDate.Year = 2013
		GROUP BY DayOfWeekUK, DayName, ProductName
		ORDER BY DayOfWeekUK ASC, TotalQuantity DESC, ProductName;
	```

	And some results:

	![alt text](./Challenge3/misc/Query-4.PNG "Query 4 result")

	5. The most sold product in April of the last three years:

	Resulting query

	```sql
	SELECT TOP 1 WITH TIES TotalQuantity, ProductName FROM
		(SELECT SUM(Quantity) as TotalQuantity, ProductName FROM 
			FactProductSales
			INNER JOIN DimProduct ON (FactProductSales.ProductID = DimProduct.ProductKey)
			INNER JOIN DimDate ON (FactProductSales.SalesDateKey = DimDate.DateKey)
			WHERE MonthName = 'January' AND
			Year BETWEEN (YEAR(GETDATE())-2) AND YEAR(GETDATE())
			GROUP BY ProductName 
		) as t1 
		ORDER BY TotalQuantity DESC;
	```

	And some results:

	![alt text](./Challenge3/misc/Query-5.PNG "Query 5 result")

	6. Amount of a product sold for years in a specific city. (select the product and the city):

	Resulting query

	```sql
	SELECT SUM(Quantity) TotalQuantity, ProductName, City, Year FROM 
		FactProductSales
		INNER JOIN DimProduct ON (FactProductSales.ProductID = DimProduct.ProductKey)
		INNER JOIN DimStores ON (FactProductSales.StoreID = DimStores.StoreID)
		INNER JOIN DimDate ON (FactProductSales.SalesDateKey = DimDate.DateKey)
		WHERE ProductName = 'Nirma Soap' AND City = 'Ahmedabad'
		GROUP BY ProductName, City, Year
		ORDER BY Year DESC, TotalQuantity DESC;
	```

	And some results:

	![alt text](./Challenge3/misc/Query-6.PNG "Query 6 result")

### How to run the Docker instance and the files for Challenge 3

As I mentioned previously, you can run an SQL Server on a Docker instance with the configuration that I already set for you. First, you must set a terminal or CMD on the **Challenge3** folder of this workshop (*/advanceddatabases/Workshop\ #2/Challenge3*) and run this command:

	docker-compose up -d

Once you have the instance running, you can connect with your preferred DBMS Manager (I recommend using SQL Server Management Studio) to the instance running in your Docker. Use this credentials to connect:

![alt text](./Challenge3/misc/SQL-Server-connection.PNG "Connection to SQL Server")}

Remember that the password is: *PasswordO1.* with the ending point. Also, you can change it if you want in the */Challenge3/docker-compose.yml* file.

To run the database scripts, you have to check the files on */Challenge3/config/db/* folder, there are two files:

	challenge-3-schema.sql: This script creates all the tables of the data warehouse
	challenge-3-queries.sql: This another one holds the queries for each of the tasks of this challenge