-- Total sales of each of the products per month during 2013

SELECT SUM(SalesTotalCost) as SalesTotalCostMonthly, MonthName 
	from FactProductSales 
	LEFT JOIN DimDate ON(FactProductSales.SalesDateKey = DimDate.DateKey) 
	WHERE DimDate.Year = 2013 
	GROUP BY DimDate.Year, DimDate.Month, DimDate.MonthName;
/*
-- The best seller for each of the products during 2013

SELECT MAX(SalesTotalCost) as TotalCost, ProductName FROM FactProductSales
	LEFT JOIN DimProduct ON (FactProductSales.ProductID = DimProduct.ProductKey)
	GROUP BY ProductName;

SELECT SalesTotalCost, SalesPersonName FROM FactProductSales 
	LEFT JOIN DimSalesPerson ON (FactProductSales.SalesPersonID = DimSalesPerson.SalesPersonID)
	ORDER BY SalesTotalCost DESC;

SELECT DISTINCT t1.TotalCost, t1.ProductName, t2.SalesPersonName  FROM 
	( SELECT MAX(SalesTotalCost) as TotalCost, ProductName FROM FactProductSales
	LEFT JOIN DimProduct ON (FactProductSales.ProductID = DimProduct.ProductKey)
	GROUP BY ProductName) as t1 

	INNER JOIN

	(SELECT SalesTotalCost, SalesPersonName FROM FactProductSales 
	LEFT JOIN DimSalesPerson ON (FactProductSales.SalesPersonID = DimSalesPerson.SalesPersonID)) as t2
	ON (t2.SalesTotalCost = t1.TotalCost)
	ORDER BY ProductName;

-- Quantity of each product sold per month during 2013, in order of highest to lowest

SELECT Quantity, ProductName, MonthName FROM 
	FactProductSales
	INNER JOIN DimDate ON (FactProductSales.SalesDateKey = DimDate.DateKey)
	INNER JOIN DimProduct ON (FactProductSales.ProductID = DimProduct.ProductKey)
	WHERE DimDate.Year = 2013
	ORDER BY MonthName ASC, Quantity DESC, ProductName;

SELECT SUM(Quantity) as TotalQuantity, ProductName, MonthName FROM 
	FactProductSales
	INNER JOIN DimDate ON (FactProductSales.SalesDateKey = DimDate.DateKey)
	INNER JOIN DimProduct ON (FactProductSales.ProductID = DimProduct.ProductKey)
	WHERE DimDate.Year = 2013
	GROUP BY MonthName, ProductName
	ORDER BY MonthName ASC, TotalQuantity DESC, ProductName;

-- Quantity of each product sold per day (name of days) during 2013, in order of highest to lowest

SELECT Quantity, ProductName, DayName FROM 
	FactProductSales
	INNER JOIN DimDate ON (FactProductSales.SalesDateKey = DimDate.DateKey)
	INNER JOIN DimProduct ON (FactProductSales.ProductID = DimProduct.ProductKey)
	WHERE DimDate.Year = 2013
	ORDER BY DayOfWeekUK ASC, Quantity DESC, ProductName;

SELECT SUM(Quantity) as TotalQuantity, ProductName, DayName FROM 
	FactProductSales
	INNER JOIN DimDate ON (FactProductSales.SalesDateKey = DimDate.DateKey)
	INNER JOIN DimProduct ON (FactProductSales.ProductID = DimProduct.ProductKey)
	WHERE DimDate.Year = 2013
	GROUP BY DayOfWeekUK, DayName, ProductName
	ORDER BY DayOfWeekUK ASC, TotalQuantity DESC, ProductName;

-- The most sold product in April of the last three years

SELECT TOP 1 WITH TIES TotalQuantity, ProductName FROM
(SELECT SUM(Quantity) as TotalQuantity, ProductName FROM 
	FactProductSales
	INNER JOIN DimProduct ON (FactProductSales.ProductID = DimProduct.ProductKey)
	INNER JOIN DimDate ON (FactProductSales.SalesDateKey = DimDate.DateKey)
	WHERE MonthName = 'January' AND
	-- Year BETWEEN (YEAR(GETDATE())-2) AND YEAR(GETDATE())
	Year BETWEEN 2011 AND 2013
	GROUP BY ProductName 
	) as t1 
	ORDER BY TotalQuantity DESC;

-- Amount of a product sold for years in a specific city. (select the product and the city).

SELECT SUM(Quantity) TotalQuantity, ProductName, City, Year FROM 
	FactProductSales
	INNER JOIN DimProduct ON (FactProductSales.ProductID = DimProduct.ProductKey)
	INNER JOIN DimStores ON (FactProductSales.StoreID = DimStores.StoreID)
	INNER JOIN DimDate ON (FactProductSales.SalesDateKey = DimDate.DateKey)
	WHERE ProductName = 'Nirma Soap' AND City = 'Ahmedabad'
	GROUP BY ProductName, City, Year
	ORDER BY Year DESC, TotalQuantity DESC;*/