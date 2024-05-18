from abc import ABC, abstractmethod

class IInventoryService(ABC):
    @abstractmethod
    def GetProduct(self,InventoryID):
        pass

    @abstractmethod
    def GetQuantityInStock(self,ProductID):
        pass

    @abstractmethod
    def AddToInventory(self,Quantity,InventoryID):
        pass

    @abstractmethod
    def RemoveFromInventory(self,Quantity,InventoryID):
        pass

    @abstractmethod
    def UpdateStockQuantity(self,Quantity,InventoryID):
        pass

    @abstractmethod
    def IsProductAvailable(self,ProductID,Quantity):
        pass

    @abstractmethod
    def GetInventoryValue(self,InventoryID):
        pass

    @abstractmethod
    def ListLowStockProducts(self,Threshold):
        pass

    @abstractmethod
    def ListOutOfStockProducts(self):
        pass