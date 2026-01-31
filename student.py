from human import Human
from logger import logger, log_errors

class Student(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.knowledge = 40
        self.day = 0
        logger.info(f"Створено Student({self.name})")

    @log_errors
    def study(self):
        if self.energy >= 20:
            self.energy -= 20
            self.knowledge += 15
            logger.info(f"{self.name} навчається. Знання {self.knowledge}, енергія {self.energy}")
            print(f"{self.name} навчається 📚 (+15 знань)")
        else:
            logger.warning(f"{self.name} занадто втомлений")
            print(f"{self.name} занадто втомлений для навчання 😵")

    # --- Симуляція днів ---
    def __iter__(self):
        return self

    def __next__(self):
        self.day += 1

        if self.energy >= 30:
            self.study()
            action = "вчився 📚"
        else:
            self.rest()
            action = "відпочивав 😴"

        logger.info(f"День {self.day}: {action}")
        return f"День {self.day}: {self.name} {action}. Енергія {self.energy}, Знання {self.knowledge}"
