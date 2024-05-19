from Util.DBconn import DBConnection
from Interface import ICustomerService
class CustomerService(DBConnection,ICustomerService):
    def CalculateTotalOrders(self,customer_id):
        try:
            self.cursor.execute("""
            select count(OrderID) from Orders
            where CustomerID= ?
            group by CustomerID""",
            (customer_id)
            )
            product = self.cursor.fetchone()[0]  
            print(f"Total number of orders:{product}")            
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
            print("Customer details updated..........")
        except Exception as e:
            print(e)