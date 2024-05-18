from abc import ABC, abstractmethod

class IProductService(ABC):
    @abstractmethod
    def GetProductDetails(self,ProductID):
        pass

    @abstractmethod
    def UpdateProductInfo(self,ProductID ,ProductName ,Description ,Price ,Category):
        pass

    @abstractmethod
    def IsProductInStock(self,ProductID):
        pass