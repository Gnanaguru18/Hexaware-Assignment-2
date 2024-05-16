from Util.DBconn import DBConnection
from abc import ABC, abstractmethod

class ICustomerService(ABC):
    @abstractmethod
    def CalculateTotalOrders(self,customer_id):
        pass

    @abstractmethod
    def GetCustomerDetails(self,CustomerID):
        pass

    @abstractmethod
    def UpdateCustomerInfo(self,CustomerID,FirstName ,LastName ,Email ,Phone ,Address):
        pass
class CustomerService(DBConnection,ICustomerService):
    def CalculateTotalOrders(self,customer_id):
        try:
            self.cursor.execute("""
            select count(OrderID) from Orders
            where CustomerID= ?
            group by CustomerID""",
            (customer_id)
            )
            products = self.cursor.fetchall()  
            for product in products:
                print(product)            
        except Exception as e:
            print(e)

    def GetCustomerDetails(self,CustomerID):
        try:
            self.cursor.execute("""
            select * from Customers
            where CustomerID= ?  """,
            CustomerID
            )
            products = self.cursor.fetchall()  
            for product in products:
                print(product)
        except Exception as e:
            print(e)

    def UpdateCustomerInfo(self,CustomerID,FirstName ,LastName ,Email ,Phone ,Address):
        try:
            self.cursor.execute("""
            update Customers
            set FirstName= ? ,LastName= ? ,Email= ? ,Phone= ? ,Address= ?
            where CustomerID=?""",
            (FirstName ,LastName ,Email ,Phone ,Address,CustomerID)
            )
            self.conn.commit()
        except Exception as e:
            print(e)