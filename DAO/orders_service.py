from Util.DBconn import DBConnection
from Interface import IOrdersService

class OrdersService(DBConnection,IOrdersService):
    def CalculateTotalAmount(self,OrderID):
        try:
            self.cursor.execute("""
            select TotalAmount from Orders
            where OrderID=?
            """,OrderID
            )
            orders = self.cursor.fetchall()  # Get all data
            for order in orders:
                print(order)            
        except Exception as e:
            print(e)

    def GetOrderDetails(self,OrderID):
        try:
            self.cursor.execute("""
            select ProductID,Quantity from OrderDetails
            where OrderID=?""",OrderID
            )
            orders = self.cursor.fetchall()  # Get all data
            for order in orders:
                print(order)
        except Exception as e:
            print(e)

    def UpdateOrderStatus(self,OrderID,Status):
        try:
            self.cursor.execute("""
            update Orders
            set Status=?
            where OrderID=?""",
            (Status,OrderID) 
            )
            self.conn.commit()
            print("Updated Status......")
        except Exception as e:
            print(e)

    def CancelOrder(self,OrderID):
        try:
            self.cursor.execute("""
            declare @a varchar(20)=?;
            update Inventory
            set QuantityInStock=QuantityInStock+(select Quantity from OrderDetails where OrderID= @a )
            delete from OrderDetails
            where OrderID= @a
            delete from Orders
            where OrderID= @a""",OrderID
            )
            self.conn.commit()
            print("Order Cancelled successfully....")
        except Exception as e:
            print(e)