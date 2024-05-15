from Util.DBconn import DBConnection
from abc import ABC, abstractmethod


class ProductService(DBConnection):
    def GetProductDetails(self,ProductID):
        try:
            self.cursor.execute("""
            select * from Products
            where ProductID=?""",ProductID
            )
        except Exception as e:
            print(e)
            
    def UpdateProductInfo(self,ProductID ,ProductName ,Description ,Price ,Categor):
        try:
            self.cursor.execute("""
            update Products
            set ProductName= ? ,Description= ? ,Price= ? ,Category= ?
            where ProductID=?
            """,
            (ProductName ,Description ,Price ,Categor,ProductID)
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
        except Exception as e:
            print(e)

