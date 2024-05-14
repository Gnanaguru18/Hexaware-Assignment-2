CREATE DATABASE TechShop
USE TechShop

CREATE TABLE Customers(
CustomerID VARCHAR(20),
FirstName VARCHAR(50),
LastName VARCHAR(50),
Email VARCHAR(255),
Phone VARCHAR(10),
Address VARCHAR(255),
PRIMARY KEY (CustomerID)
);

CREATE TABLE Products(
ProductID VARCHAR(20),
ProductName VARCHAR(50),
Description VARCHAR(255),
Price INT,
Category INT,
PRIMARY KEY (ProductID)
);

CREATE TABLE Orders(
OrderID VARCHAR(20),
CustomerID VARCHAR(20),
OrderDate DATE,
TotalAmount INT,
Status VARCHAR(10),
PRIMARY KEY (OrderID),
FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE OrderDetails(
OrderDetailID VARCHAR(20),
OrderID VARCHAR(20),
ProductID VARCHAR(20),
Quantity INT,
PRIMARY KEY (OrderDetailID),
FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

CREATE TABLE Inventory(
InventoryID VARCHAR(20),
ProductID VARCHAR(20),
QuantityInStock INT,
LastStockUpdate DATE,
PRIMARY KEY (InventoryID),
FOREIGN KEY (ProductID) REFERENCES ProductS(ProductID)
);