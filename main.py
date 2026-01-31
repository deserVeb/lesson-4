from student import Student
from worker import Worker
from logger import logger

student = Student("Олексій", 20)
worker = Worker("Максим", 30, "програміст")

logger.info("=== Симуляція розпочата ===")

student.study()
worker.work()
student.talk(worker)
worker.rest()

print("\n=== Дні життя студента ===")
for day in student:
    print(day)
    if student.day == 7:  # тиждень (можеш поставити 365)
        break

logger.info("=== Симуляція завершена ===")
