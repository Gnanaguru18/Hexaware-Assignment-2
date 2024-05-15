from Util.DBconn import DBConnection
from abc import ABC, abstractmethod

class InventoryService(DBConnection):
    def GetProduct(self,InventoryID):
        try:
            self.cursor.execute("""
            select * from Products
            where ProductID=(select ProductID from Inventory
                            where InventoryID= ? )""",
            InventoryID
            )
        except Exception as e:
            print(e)
            
    def GetQuantityInStock(self,ProductID):
        try:
            self.cursor.execute("""
            select QuantityInStock from Inventory
            where ProductID= ? """,
            ProductID
            )
        except Exception as e:
            print(e)
    
    def AddToInventory(self,Quantity,ProductID):
        try:
            self.cursor.execute("""
            update Inventory
            set QuantityInStock=QuantityInStock + ?
            where ProductID = ?""",
            (Quantity,ProductID)
            )
            self.conn.commit()
        except Exception as e:
            print(e)

    def RemoveFromInventory(self,Quantity,ProductID):
        try:
            self.cursor.execute("""
            update Inventory
            set QuantityInStock=QuantityInStock - ?
            where ProductID = ?""",
            (Quantity,ProductID)
            )
            self.conn.commit()
        except Exception as e:
            print(e)

    def UpdateStockQuantity(self,Quantity,ProductID):
        try:
            self.cursor.execute("""
            update Inventory
            set QuantityInStock= ?
            where ProductID = ?""",
            (Quantity,ProductID)
            )
            self.conn.commit()
        except Exception as e:
            print(e)
    
    def IsProductAvailable(self,ProductID,Quantity):
        try:
            row_count = self.cursor.execute("""
            select QuantityInStock from Inventory
            where ProductID = ? and QuantityInStock > ? """,
            (ProductID,Quantity)
            ).rowcount
            if row_count == 0:
                print("Not Available")
            else:
                print("Available")
        except Exception as e:
            print(e)
    
    def GetInventoryValue(self,InventoryID):
        try:
            self.cursor.execute("""
            select QuantityInStock*price from Inventory i
            inner join Products p 
            on p.ProductID=i.ProductID
            where InventoryID= ? """,
            (InventoryID)
            )
        except Exception as e:
            print(e)

    def ListLowStockProducts(self,Threshold):
        try:
            self.cursor.execute("""
            select p.ProductID,ProductName from Inventory i
            inner join Products p 
            on p.ProductID=i.ProductID
            where QuantityInStock < ? """,
            Threshold
            )
        except Exception as e:
            print(e)

    def ListOutOfStockProducts(self):
        try:
            self.cursor.execute("""
            select p.ProductID,ProductName from Inventory i
            inner join Products p 
            on p.ProductID=i.ProductID
            where QuantityInStock = 0"""
            )
        except Exception as e:
            print(e)