from human import Human

class Student(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.knowledge = 40
        self.day = 0  # лічильник днів життя

    # робимо студента ітерованим
    def __iter__(self):
        return self

    def __next__(self):
        self.day += 1

        # логіка нового дня
        if self.energy >= 30:
            self.study()
            action = "вчився 📚"
        else:
            self.rest()
            action = "відпочивав 😴"

        return f"День {self.day}: {self.name} {action}. Енергія: {self.energy}, Знання: {self.knowledge}"

    def study(self):
        if self.energy >= 20:
            self.energy -= 20
            self.knowledge += 15
            print(f"{self.name} навчається 📚 (+15 знань)")
        else:
            print(f"{self.name} занадто втомлений для навчання 😵")
