from being import Being

class Human(Being):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        self.mood = 70

    def talk(self, other):
        self.mood += 5
        other.mood += 5
        print(f"{self.name} поспілкувався з {other.name} 🗣️ (+5 настрою обом)")
