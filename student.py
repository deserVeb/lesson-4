from human import Human

class Student(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.knowledge = 40

    def study(self):
        if self.energy >= 20:
            self.energy -= 20
            self.knowledge += 15
            print(f"{self.name} навчається 📚 (+15 знань)")
        else:
            print(f"{self.name} занадто втомлений для навчання 😵")
