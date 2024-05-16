class InvalidDataException(Exception):
    def __init__(self):
        super().__init__(f"Invalid data entered")

class IncompleteOrderException(Exception):
    def __init__(self):
        super().__init__(f"Incomplete order")

class InsufficientStockException(Exception):
    def __init__(self):
        super().__init__(F"Insufficient stock available")
