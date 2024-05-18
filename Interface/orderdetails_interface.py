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