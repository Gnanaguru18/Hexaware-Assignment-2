from Util.DBconn import DBConnection
from abc import ABC, abstractmethod

class OrderDetailsService(DBConnection):

    def CalculateSubtotal(self,OrderID):
        try:
            self.cursor.execute("""
            select (quantity*Price) as SubTotal from products p
            inner join OrderDetails o
            on p.ProductID=o.ProductID
            where OrderID= ?""",OrderID
            )
        except Exception as e:
            print(e)
        
    def GetOrderDetailInfo(self,OrderID):
        try:
            self.cursor.execute("""
            select CustomerID,OrderDate,quantity,ProductID,TotalAmount,Status from OrderDetails od inner join
            Orders o on
            o.OrderID=od.OrderID
            where OrderID= ? """,OrderID
            )
        except Exception as e:
            print(e)
    
    def UpdateQuantity(self,OrderID,Quantity):
        try:
            self.cursor.execute("""
            update OrderDetails
            set Quantity=?
            where OrderID=?

            update Orders
            set TotalAmount=(select quantity*Price from OrderDetails o inner join 
                            Products p on
                            o.ProductID=p.ProductID
                            where OrderID=?) """,
            (Quantity,OrderID,OrderID)
            )
            self.conn.commit()
        except Exception as e:
            print(e)


    def AddDiscount(self,discount,OrderID):
        try:
            self.cursor.execute("""
            update Orders
            set TotalAmount=TotalAmount*(1-(?/100))
            where OrderID=?""",
            (discount,OrderID)
            )
            self.conn.commit()
        except Exception as e:
            print(e)
