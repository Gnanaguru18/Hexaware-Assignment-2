

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
