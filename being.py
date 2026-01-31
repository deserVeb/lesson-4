from logger import logger

class Being:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        logger.info(f"Створено Being({self.name})")

    def rest(self):
        self.energy += 30
        logger.info(f"{self.name} відпочиває (+30 енергії). Енергія: {self.energy}")
        print(f"{self.name} відпочиває 😴 (+30 енергії)")
