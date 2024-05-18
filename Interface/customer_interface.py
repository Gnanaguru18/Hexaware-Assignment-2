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