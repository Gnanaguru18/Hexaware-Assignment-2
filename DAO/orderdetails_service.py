from Util.DBconn import DBConnection
from Interface import IOrderDetailsService
from MyExceptions import InsufficientStockException,IncompleteOrderException
class OrderDetailsService(DBConnection,IOrderDetailsService):

    def CalculateSubtotal(self,OrderID):
        try:
            self.cursor.execute("""
            select ProductID from OrderDetails
            where OrderID = ? """,OrderID
            )
            product=self.cursor.fetchone()[0]
            if not product:
                raise IncompleteOrderException()

            self.cursor.execute("""
            select (quantity*Price) as SubTotal from products p
            inner join OrderDetails o
            on p.ProductID=o.ProductID
            where OrderID= ?""",OrderID
            )
            orders = self.cursor.fetchall()  # Get all data
            for order in orders:
                print(order)  
        except IncompleteOrderException as e:
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
            select QuantityInStock from Inventory
            where ProductID=(select ProductID from OrderDetails
                            where OrderID = ? )""",OrderID
            )
            stock_quantity=self.cursor.fetchone()[0]
            if stock_quantity<Quantity:
                raise InsufficientStockException()

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
        except InsufficientStockException as e:
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
