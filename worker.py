from human import Human
from logger import logger, log_errors

class Worker(Human):
    def __init__(self, name, age, profession):
        super().__init__(name, age)
        self.profession = profession
        self.salary = 0
        logger.info(f"Створено Worker({self.name}, професія {self.profession})")

    @log_errors
    def work(self):
        self.energy -= 30
        self.salary += 80
        logger.info(f"{self.name} працює ({self.profession}). Зарплата {self.salary}, енергія {self.energy}")
        print(f"{self.name} працює як {self.profession} 💼 (+80 зарплати)")
