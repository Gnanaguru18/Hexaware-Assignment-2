class IncompleteOrderException(Exception):
    def __init__(self):
        super().__init__(f"Incomplete order")

class InsufficientStockException(Exception):
    def __init__(self):
        super().__init__(f"Insufficient stock available")

class DBConnectionException(Exception):
    def __init__(self):
        super().__init__("DB connection failed..")