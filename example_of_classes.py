class Dragons:
    def __init__(self, name, place):
        self.name = name
        self.place = place
    def info(self):
        print(f'the dragon is {self.name}, lives in {self.place} area')

class Ancient_dragons(Dragons):
    def __init__(self, name, place, specialty):
        super().__init__(name,place)
        self.specialty=specialty
    def info(self):
        print(f'the dragon is {self.name}, lives in {self.place} area, specialty: {self.specialty}')
