class Being:
    def __init__(self, name):
        self.name = name
        self.energy = 100

    def rest(self):
        self.energy += 30
        print(f"{self.name} відпочиває 😴 (+30 енергії)")
