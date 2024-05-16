from DAO import CustomerService,InventoryService,OrderDetailsService,OrdersService,ProductService
from MyExceptions.customer_exception import validate_email


class MainMenu:
    customer_service=CustomerService()
    product_service=ProductService()
    inventory_service=InventoryService()
    orders_service=OrdersService()
    orderdetails_service=OrderDetailsService()


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
                customer_id=input("Enter Customer ID:")
                self.customer_service.CalculateTotalOrders(customer_id)

            elif choice==2:
                customer_id=input("Enter Customer ID:")
                self.customer_service.GetCustomerDetails(customer_id)

            elif choice==3:          
                customer_id=input("Enter Customer ID:")
                self.customer_service.GetCustomerDetails(customer_id)
                FirstName=input("Enter new FirstName:")
                LastName=input("Enter new LastName:")
                Email=input("Enter new Email:")
                validate_email(Email)
                Phone=input("Enter new Phone:")
                Address=input("Enter new Address:")
                self.customer_service.UpdateCustomerInfo(customer_id,FirstName ,LastName ,Email ,Phone ,Address)

            elif choice==4:
                break
    
    def product_menu(self):
        while True:
            print("""
                Choose 
                1: Get Product Details
                2: Update Product Info
                3. Is Product In Stock
                4. Exit""")
            choice=int(input("Enter choice:"))
            if choice==1:
                ProductID=input("Enter Product ID:")
                self.product_service.GetProductDetails(ProductID)

            elif choice==2:
                ProductID=input("Enter Product ID:")
                self.product_service.GetProductDetails(ProductID)
                ProductName=input("Enter new ProductName:")
                Description=input("Enter new Description:")
                Price=int(input("Enter new Price:"))
                Category=int(input("Enter new Category:"))
                self.product_service.UpdateProductInfo(ProductName ,Description ,Price ,Category)

            elif choice==3:          
                ProductID=input("Enter Product ID:")
                self.product_service.IsProductInStock(ProductID)

            elif choice==4:
                break

    def inventory_menu(self):
        while True:
            print("""
                Choose 
                1: Get Product
                2: Get Quantity In Stock
                3. Add To Inventory
                4. Remove From Inventory
                5. Update Stock Quantity
                6. Is Product Available
                7. Get Inventory Value
                8. List Low Stock Products
                9. List Out Of Stock Products
                10. Exit""")
            choice=int(input("Enter choice:"))
            if choice==1:
                InventoryID=input("Enter Inventory ID:")
                self.inventory_service.GetProduct(InventoryID)
            elif choice==2:
                InventoryID=input("Enter Inventory ID:")
                self.inventory_service.GetQuantityInStock(InventoryID)
            elif choice==3:          
                InventoryID=input("Enter Inventory ID:")
                Quantity=int(input("Enter quantity:"))
                self.inventory_service.AddToInventory(Quantity,InventoryID)
            elif choice==4:
                InventoryID=input("Enter Inventory ID:")
                Quantity=int(input("Enter quantity:"))
                self.inventory_service.RemoveFromInventory(Quantity,InventoryID)
            elif choice==5:   
                InventoryID=input("Enter Inventory ID:")
                Quantity=int(input("Enter quantity:"))       
                self.inventory_service.UpdateStockQuantity(Quantity,InventoryID)
            elif choice==6:
                ProductID=input("Enter Product ID:")
                Quantity=int(input("Enter quantity:")) 
                self.inventory_service.IsProductAvailable(ProductID,Quantity)
            elif choice==7:       
                InventoryID=input("Enter Inventory ID:")   
                self.inventory_service.GetInventoryValue(InventoryID)
            elif choice==8:
                Threshold=int(input("Enter Threshold value:"))
                self.inventory_service.ListLowStockProducts(Threshold)
            elif choice==9:          
                self.inventory_service.ListOutOfStockProducts()
            elif choice==10:
                break

    def orders_menu(self):
        while True:
            print("""
                Choose 
                1: CalculateTotalAmount
                2: GetOrderDetails
                3. UpdateOrderStatus
                4. CancelOrder
                5. Exit""")
            choice=int(input("Enter choice:"))
            if choice==1:
                OrderID=input("Enter Order ID")
                self.orders_service.CalculateTotalAmount(OrderID)
            elif choice==2:
                OrderID=input("Enter Order ID")
                self.orders_service.GetOrderDetails()
            elif choice==3:        
                OrderID=input("Enter Order ID")
                status=input("Enter order status (processing/shipped):")  
                self.orders_service.UpdateOrderStatus(OrderID,status)
            elif choice==4:   
                OrderID=input("Enter Order ID")       
                self.orders_service.CancelOrder(OrderID)
            elif choice==5:
                break

    def orderdetails_menu(self):
        while True:
            print("""
                Choose 
                1: CalculateSubtotal
                2: GetOrderDetailInfo
                3. UpdateQuantity
                4. AddDiscount
                5. Exit""")
            choice=int(input("Enter choice:"))
            if choice==1:
                OrderID=input("Enter Order ID")
                self.orderdetails_service.CalculateSubtotal(OrderID)
            elif choice==2:
                OrderID=input("Enter Order ID")
                self.orderdetails_service.GetOrderDetailInfo(OrderID)
            elif choice==3:          
                OrderID=input("Enter Order ID")
                Quantity=int(input("Enter quantity:"))
                self.orderdetails_service.UpdateQuantity(OrderID,Quantity)
            elif choice==4:          
                OrderID=input("Enter Order ID")
                Discount=int(input("Enter discount %:"))
                self.orderdetails_service.AddDiscount(OrderID,Discount)
            elif choice==5:
                break
    
def main():
     while True:
            print("""
                Choose 
                1: Customer Management
                2: Product Management
                3. Inventory Management
                4. Orders Management
                5. Order details Management
                6. Exit""")
            choice=int(input("Enter choice:"))
            if choice==1:
                main_menu.customer_menu()
            elif choice==2:
                main_menu.product_menu()
            elif choice==3:          
                main_menu.inventory_menu()
            elif choice==4:          
                main_menu.orders_menu()
            elif choice==5:          
                main_menu.orderdetails_menu()
            elif choice==6:
                main_menu.customer_service.close()
                main_menu.product_service.close()
                main_menu.inventory_service.close()
                main_menu.orders_service.close()
                main_menu.orderdetails_service.close()
                break     


if __name__ == "__main__":

    main_menu=MainMenu()
    print("Welcome to Tech Shop")
    main()
      
