import datetime


class Person:
    def __init__(self, last_name, first_name, middle_name, birth_date):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.birth_date = birth_date

    def calculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birth_date.year - (
                    (today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
