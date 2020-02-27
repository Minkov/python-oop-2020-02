class Flower:
    is_happy = False
    current_quantity = 0

    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements

    # def water(self, quantity):
    #     self.is_happy = self.water_requirements <= quantity

    def water(self, quantity):
        self.current_quantity += quantity
        self.is_happy = self.water_requirements <= self.current_quantity

    def status(self):
        result = f'{self.name} is not happy'

        if self.is_happy:
            result = f'{self.name} is happy'

        return result


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
