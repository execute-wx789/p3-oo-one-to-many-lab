class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []
    def __init__(self,name,pet_type,owner=None):
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception
        self.owner = owner
        self.name = name
        Pet.all.append(self)


class Owner(Pet):
    def __init__(self,name):
        self.name = name
    def pets(self):
        returnList = []
        for pet in Pet.all:
            if pet.owner == self:
                returnList.append(pet)
        return returnList
    def add_pet(self, pet):
        pet.owner = self
    def get_sorted_pets(self):
        returnList = []
        for pet in Pet.all:
            if pet.owner == self:
                returnList.append(pet)
        def sortKey(e):
            return e.name
        returnList.sort(key=sortKey)
        return returnList