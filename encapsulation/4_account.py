class Account:
    def __init__(self, id, balance, pin):
        self.__id = id
        self.pin = pin
        self.balance = balance

    def __is_correct_pin(self, pin):
        return self.pin == pin

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, value):
        if not value or len(value) < 4:
            raise ValueError
        self.__pin = value

    def get_id(self, pin):
        if not self.__is_correct_pin(pin):
            return 'Wrong pin'

        return self.__id

    def change_pin(self, old_pin, new_pin):
        if not self.__is_correct_pin(old_pin):
            return 'Wrong pin'

        self.pin = new_pin
        return 'Pin changed'

account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
