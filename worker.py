from human import Human

class Worker(Human):
    def __init__(self, name, age, profession):
        super().__init__(name, age)
        self.profession = profession
        self.salary = 0

    def work(self):
        self.energy -= 30
        self.salary += 80
        print(f"{self.name} працює як {self.profession} 💼 (+80 зарплати)")
