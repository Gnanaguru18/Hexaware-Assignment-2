from Util.DBconn import DBConnection
from abc import ABC, abstractmethod

class IOrderDetailsService(ABC):
    @abstractmethod
    def CalculateSubtotal(self,OrderID):
        pass

    @abstractmethod
    def GetOrderDetailInfo(self,OrderID):
        pass

    @abstractmethod
    def UpdateQuantity(self,OrderID,Quantity):
        pass

    @abstractmethod
    def AddDiscount(self,OrderID,discount):
        pass
class OrderDetailsService(DBConnection,IOrderDetailsService):

    def CalculateSubtotal(self,OrderID):
        try:
            self.cursor.execute("""
            select (quantity*Price) as SubTotal from products p
            inner join OrderDetails o
            on p.ProductID=o.ProductID
            where OrderID= ?""",OrderID
            )
            orders = self.cursor.fetchall()  # Get all data
            for order in orders:
                print(order)  
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
            orders = self.cursor.fetchall()  # Get all data
            for order in orders:
                print(order)  
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
            print("Quantity updated.........")
        except Exception as e:
            print(e)


    def AddDiscount(self,OrderID,discount):
        try:
            self.cursor.execute("""
            update Orders
            set TotalAmount-=TotalAmount*(1-(?/100))
            where OrderID=?""",
            (discount,OrderID)
            )
            self.conn.commit()
            print("Discount applied.........")
        except Exception as e:
            print(e)
