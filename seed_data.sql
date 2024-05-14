INSERT INTO Customers
VALUES('C001','Naruto','Uzumaki','naruto@gmail.com','8778000000','Address 1'),
	('C002','Sasuke','Uchiha','sasuke@gmail.com','8778000001','Address 2'),
	('C003','Sakura','Haruno','sakura@gmail.com','8778000002','Address 3'),
	('C004','Hinata','Hyuga','hinata@gmail.com','8778000003','Address 4'),
	('C005','Shikamaru','Nara','shikamaru@gmail.com','8778000004','Address 5'),
	('C006','Zoro','Roronoa','zoro@gmail.com','8778000005','Address 6'),
	('C007','Yoruichi','Shihouin','yoruichi@gmail.com','8778000006','Address 7'),
	('C008','Takumi','Usui','takumi@gmail.com','8778000007','Address 8'),
	('C009','Heewon','Jung','heewon@gmail.com','8778000008','Address 9'),
	('C010','Rudeus','Greyrat','rudeus@gmail.com','8778000009','Address 10');
	
INSERT INTO Products
VALUES('P001','Mouse','Description 1',500,1),
	('P002','Keyboard','Description 2',1000,1),
	('P003','Laptop','Description 3',50000,1),
	('P004','Power bank','Description 4',1000,3),
	('P005','Earphone','Description 5',1000,3),
	('P006','Charger','Description 6',500,3),
	('P007','Smart watch','Description 7',1000,2),
	('P008','Mobile','Description 8',20000,2),
	('P009','Monitor','Description 9',10000,1),
	('P010','Smart TV','Description 10',30000,2);

INSERT INTO Orders
VALUES('OR01','C005','2024-05-12',1500,'Shipped'),
	('OR02','C008','2024-05-16',80000,'Shipped'),
	('OR03','C001','2024-05-12',100000,'Shipped'),
	('OR04','C010','2024-05-16',2000,'Pending'),
	('OR05','C004','2024-04-15',3000,'Pending'),
	('OR06','C001','2024-05-10',50000,'Shipped'),
	('OR07','C008','2024-05-12',5000,'Pending'),
	('OR08','C006','2024-04-03',5000,'Pending'),
	('OR09','C002','2024-05-02',6000,'Shipped'),
	('OR10','C009','2024-05-05',1000,'Shipped');

INSERT INTO OrderDetails
VALUES('OD01','OR01','P001',3),
	('OD02','OR02','P008',4),
	('OD03','OR03','P003',2),
	('OD04','OR04','P001',4),
	('OD05','OR05','P002',3),
	('OD06','OR06','P003',1),
	('OD07','OR07','P007',5),
	('OD08','OR08','P004',5),
	('OD09','OR09','P005',6),
	('OD10','OR10','P006',2);

INSERT INTO Inventory
VALUES('IV01','P001',20,'2024-04-10'),
	('IV02','P002',25,'2024-04-20'),
	('IV03','P003',5,'2024-04-10'),
	('IV04','P004',10,'2024-04-01'),
	('IV05','P005',15,'2024-04-10'),
	('IV06','P006',10,'2024-04-01'),
	('IV07','P007',20,'2024-04-10'),
	('IV08','P008',15,'2024-04-20'),
	('IV09','P009',20,'2024-04-10'),
	('IV10','P010',10,'2024-04-30');