from student import Student
from worker import Worker

student = Student("Олексій", 20)
worker = Worker("Максим", 30, "програміст")

print("=== Симуляція ===\n")

student.study()
worker.work()
student.talk(worker)
worker.rest()

print("\n=== Стани об'єктів ===")
print(f"{student.name} | Знання: {student.knowledge}, Енергія: {student.energy}, Настрій: {student.mood}")
print(f"{worker.name} | Професія: {worker.profession}, Зарплата: {worker.salary}, Енергія: {worker.energy}, Настрій: {worker.mood}")

print("\n=== Дні життя студента ===")
for day in student:
    print(day)
    if student.day == 31: 
        break