from ClassPerson import Person


class Teacher(Person):
    def __init__(self, last_name, first_name, middle_name, birth_date, faculty, position, academic_degree, salary,
                 courses):
        super().__init__(last_name, first_name, middle_name, birth_date)
        self.faculty = faculty
        self.position = position
        self.academic_degree = academic_degree
        self.salary = salary
        self.courses = courses
