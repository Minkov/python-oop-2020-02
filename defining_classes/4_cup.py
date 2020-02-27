class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        # check all invalid cases
        if self.quantity + milliliters <= self.size:
            return

        self.quantity += milliliters

    def status(self):
        return self.size - self.quantity
