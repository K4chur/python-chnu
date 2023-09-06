from ClassPerson import Person
from ClassTeacher import Teacher
import datetime

teacher1 = Teacher("Ivanov", "Ivan", "Ivanovich", datetime.date(1980, 5, 15), "Engineering", "Associate Professor", "Ph.D.", 50000, 3)
teacher2 = Teacher("Petrov", "Petr", "Petrovich", datetime.date(1975, 8, 22), "Science", "Professor", "Doctor of Science", 60000, 2)
teacher3 = Teacher("Sidorov", "Sergey", "Sergeevich", datetime.date(1990, 3, 10), "Engineering", "Assistant Professor", "M.Sc.", 45000, 4)

teachers = [teacher1, teacher2, teacher3]

faculty_name = "Engineering"
course_teachers = [teacher for teacher in teachers if teacher.faculty == faculty_name]
total_courses = sum(teacher.courses for teacher in course_teachers)
average_age = sum(teacher.calculate_age() for teacher in course_teachers) / len(course_teachers)

print(f"Total courses on the '{faculty_name}' faculty: {total_courses}")
print(f"Average age of teachers on the '{faculty_name}' faculty: {average_age:.1f} years")