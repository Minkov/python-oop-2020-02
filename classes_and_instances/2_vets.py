class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        self.animals.append(animal_name)

    def unregister_animal(self, animal_name):
        if animal_name not in self.animals:
            return f'{animal_name} not in the clinic'

        self.animals.remove(animal_name)
        Vet.animals.remove(animal_name)

        return f'{animal_name} unregistered successfully'

    def info(self):
        animals_count = len(self.animals)
        space_left_in_clinic = Vet.space - len(Vet.animals)
        return f'{self.name} has {animals_count} animals. {space_left_in_clinic} space left in clinic'

class VetClinic:
    def __init__(self):
        self.vets = []
        self.space = 5
        self.total_animals = []

    def add_vet(self, name):
        self.vets.append(Vet(name))

    def register_animal_to_vet(self, vet_name, animal_name):
        if len(self.total_animals) == self.space:
            return 'Not enough space'
        vet = list(filter(lambda v: v.name == vet_name, self.vets))[0]
        self.total_animals.append(animal_name)
        vet.register_animal(animal_name)
        return f'{animal_name} registered in the clinic'

peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
