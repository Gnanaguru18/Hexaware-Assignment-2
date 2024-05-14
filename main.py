import pyodbc

server_name = "TIGGER\\SQLEXPRESS"
database_name = "TechShop"


conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)
print(conn_str)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("Select 1")
print("Database connection is successful")

class CustomerService:
    def CalculateTotalOrder(self,customer_id):
        conn.execute("""
        select count(OrderID) from Orders
        where CustomerID= ?
        group by CustomerID""",
        (customer_id)
        )

    def GetCustomerDetails(self,CustomerID,FirstName ,LastName ,Email ,Phone ,Address):
        conn.execute("""
        insert into Customers values (?,?,?,?,?,?)""",
        (CustomerID,FirstName ,LastName ,Email ,Phone ,Address)
        )
        conn.commit()

    def UpdateCustomerInfo(self,CustomerID,FirstName ,LastName ,Email ,Phone ,Address):
        conn.execute("""
        update Customers
        set FirstName= ? ,LastName= ? ,Email= ? ,Phone= ? ,Address= ?
        where CustomerID=?""",
        (FirstName ,LastName ,Email ,Phone ,Address,CustomerID)
        )
        conn.commit()
    

class ProductService:
    def GetProductDetails(self,ProductID):
        conn.execute("""
        select * from Products
        where ProductID=?""",ProductID
        )
        
    def UpdateProductInfo(self,ProductID ,ProductName ,Description ,Price ,Categor):
        conn.execute("""
        update Products
        set ProductName= ? ,Description= ? ,Price= ? ,Category= ?
		where ProductID=?
        """,
        (ProductName ,Description ,Price ,Categor,ProductID)
        )
        conn.commit()
    
    def IsProductInStock(self,ProductID):
        conn.execute("""
        select QuantityInStock from Inventory
        where ProductID=?
        """,ProductID
        )


class Orders:
    def CalculateTotalAmount(self,OrderID):
        conn.execute("""
        select TotalAmount from Orders
        where OrderID=?
        """,OrderID
        )

    def GetOrderDetails(self,OrderID):
        conn.execute("""
        select ProductID,Quantity from OrderDetails
        where OrderID=?""",OrderID
        )
    
    def UpdateOrderStatus(self,OrderID,Status):
        conn.execute("""
        update Orders
        set Status=?
        where OrderID=?""",
        (Status,OrderID) 
        )
        conn.commit()

    def CancelOrder(self,OrderID):
        conn.execute("""
        declare @a varchar(20)=?;
        update Inventory
        set QuantityInStock=QuantityInStock+(select Quantity from OrderDetails where OrderID= @a )
        delete from OrderDetails
        where OrderID= @a
        delete from Orders
        where OrderID= @a""",OrderID
        )
        conn.commit()


class OrderDetails:
    def CalculateSubtotal(self,OrderID):
        conn.execute("""
        select (quantity*Price) as SubTotal from products p
        inner join OrderDetails o
        on p.ProductID=o.ProductID
        where OrderID= ?""",OrderID
        )
        
    def GetOrderDetailInfo(self,OrderID):
        conn.execute("""
        select CustomerID,OrderDate,quantity,ProductID,TotalAmount,Status from OrderDetails od inner join
        Orders o on
        o.OrderID=od.OrderID
        where OrderID= ? """,OrderID
        )
    
    def UpdateQuantity(self,OrderID,Quantity):
         conn.execute("""
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
        conn.commit()


    def AddDiscount(self,discount,OrderID):
        conn.execute("""
        update Orders
        set TotalAmount=TotalAmount*(1-(?/100))
        where OrderID=?""",
        (discount,OrderID)
        )
        conn.commit()

    
class Inventory:
    def GetProduct(self,InventoryID):
        conn.execute("""
        select * from Products
        where ProductID=(select ProductID from Inventory
                        where InventoryID= ? )""",
        InventoryID
        )
            
    def GetQuantityInStock(self,ProductID):
        conn.execute("""
        select QuantityInStock from Inventory
        where ProductID= ? """,
        ProductID
        )
    
    def AddToInventory(self,Quantity,ProductID):
        conn.execute("""
        update Inventory
        set QuantityInStock=QuantityInStock + ?
        where ProductID = ?""",
        (Quantity,ProductID)
        )
        conn.commit()

    def RemoveFromInventory(self,Quantity,ProductID):
        conn.execute("""
        update Inventory
        set QuantityInStock=QuantityInStock - ?
        where ProductID = ?""",
        (Quantity,ProductID)
        )
        conn.commit()

    def UpdateStockQuantity(self,Quantity,ProductID):
        conn.execute("""
        update Inventory
        set QuantityInStock= ?
        where ProductID = ?""",
        (Quantity,ProductID)
        )
        conn.commit()
    
    def IsProductAvailable(self,ProductID,Quantity):
        row_count = conn.execute("""
        select QuantityInStock from Inventory
        where ProductID = ? and QuantityInStock > ? """,
        (ProductID,Quantity)
        ).rowcount
        if row_count == 0:
            print("Not Available")
        else:
            print("Available")
    
    def GetInventoryValue(self,InventoryID):
        conn.execute("""
        select QuantityInStock*price from Inventory i
        inner join Products p 
        on p.ProductID=i.ProductID
        where InventoryID= ? """,
        (InventoryID)
        )

    def ListLowStockProducts(self,Threshold):
        conn.execute("""
        select p.ProductID,ProductName from Inventory i
        inner join Products p 
        on p.ProductID=i.ProductID
        where QuantityInStock < ? """,
        Threshold
        )

    def ListOutOfStockProducts(self):
        conn.execute("""
        select p.ProductID,ProductName from Inventory i
        inner join Products p 
        on p.ProductID=i.ProductID
        where QuantityInStock = 0"""
        )

class MainMenu:
    customer_service=CustomerService()
    product_service=ProductService()


    def customer_menu(self):
        while True:
            print("""
                Choose 
                1: Calculate Total Orders
                2: Get Customer Details
                3. Update Customer Info
                4. Exit""")
            choice=int(input("Enter choice:"))
            if choice==1:
                self.customer_service.CalculateTotalOrders()
            elif choice==2:
                self.customer_service.GetCustomerDetails()
            elif choice==3:          
                self.customer_service.UpdateCustomerInfo()
            elif choice==5:
                break
    
    def product_menu(self):
        while True:
            print("""
                Choose 
                1: GetProductDetails
                2: UpdateProductInfo
                3. IsProductInStock
                4. Exit""")
            choice=int(input("Enter choice:"))
            if choice==1:
                self.product_service.GetProductDetails()
            elif choice==2:
                self.product_service.UpdateProductInfo()
            elif choice==3:          
                self.product_service.IsProductInStock()
            elif choice==5:
                break


if __name__ == "__main__":


    cursor.close()
    conn.close()
