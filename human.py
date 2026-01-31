from being import Being
from logger import logger

class Human(Being):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        self.mood = 70
        logger.info(f"Створено Human({self.name}, {self.age})")

    def talk(self, other):
        self.mood += 5
        other.mood += 5
        logger.info(f"{self.name} говорить з {other.name} (+5 настрою)")
        print(f"{self.name} поспілкувався з {other.name} 🗣️ (+5 настрою обом)")
