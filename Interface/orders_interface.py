from abc import ABC, abstractmethod

class IOrdersService(ABC):
    @abstractmethod
    def CalculateTotalAmount(self,OrderID):
        pass

    @abstractmethod
    def GetOrderDetails(self,OrderID):
        pass

    @abstractmethod
    def UpdateOrderStatus(self,OrderID,Status):
        pass

    @abstractmethod
    def CancelOrder(self,OrderID):
        pass