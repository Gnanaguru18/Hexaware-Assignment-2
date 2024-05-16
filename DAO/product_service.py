from Util.DBconn import DBConnection
from abc import ABC, abstractmethod


class ProductService(DBConnection):
    def GetProductDetails(self,ProductID):
        try:
            self.cursor.execute("""
            select * from Products
            where ProductID=?""",ProductID
            )
            products = self.cursor.fetchall()  # Get all data
            for product in products:
                print(product)
        except Exception as e:
            print(e)
            
    def UpdateProductInfo(self,ProductID ,ProductName ,Description ,Price ,Category):
        try:
            self.cursor.execute("""
            update Products
            set ProductName= ? ,Description= ? ,Price= ? ,Category= ?
            where ProductID=?
            """,
            (ProductName ,Description ,Price ,Category,ProductID)
            )
            self.conn.commit()
        except Exception as e:
            print(e)
    
    def IsProductInStock(self,ProductID):
        try:    
            self.cursor.execute("""
            select QuantityInStock from Inventory
            where ProductID=?
            """,ProductID
            )
            product = self.cursor.fetchall()
            quantity=[i for i in product] 
            if quantity[0] == 0:
                print("Not available")
            else:
                print("Available")
        except Exception as e:
            print(e)

