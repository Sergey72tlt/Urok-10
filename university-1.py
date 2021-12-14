from datetime import date


class University:
    students_list = []

    def __init__(self, best_ball):
        self.best_ball = best_ball

    def student_score_is_enough(self, new_student):
        if new_student.best_ball < self.best_ball:
            return False
        else:
            return True

    def add_student(self, new_student):
        if not self.student_score_is_enough(new_student):
            print(f'Абитуриенту', new_student, 'не хватило баллов для поступления в наш университет')
        else:
            self.students_list.append(new_student)
            print(f'Абитуриент {new_student} зачислен в наш университет')

    def show_students(self):
        print('Студенты нашего универа:')
        for student in self.students_list:
            print(student)


class People:
    def __init__(self, name: str, surname: str, patronomyc: str, byrth_date: date, phone: str):
        self.surname = surname
        self.name = name
        self.patronomyc = patronomyc
        self.byrth_date = byrth_date
        self.phone = phone


class Student(People):
    def __init__(self, name: str, surname: str, patronomyc: str,
                 byrth_date: date, phone: str, id: int, group_number: int,
                 specialty_code: int, best_ball: int):

        super().__init__(name, surname, patronomyc, byrth_date, phone)
        self.id = id
        self.group_number = group_number
        self.specialty_code = specialty_code
        self.best_ball = best_ball

    def __str__(self):
        return ' '.join((self.name, self.surname))


if __name__ == '__main__':
    school = University(1000)
    student1 = Student('Иван', 'Иванов', 'Иванович', date(1992, 4, 25), '33-52-28', 10, 45, 1000, 1000)
    student2 = Student('Пётр', 'Петров', 'Петрович', date(1989, 7, 2), '33-85-35', 10, 12, 12, 1050)
    student3 = Student('Семен', 'Семенов', 'Семенович', date(1990, 5, 17), '32-01-83', 11, 13, 12, 980)
    student4 = Student('Олег', 'Сидоров', 'Васильевич', date(1952, 9, 1), '22-61-93', 12, 12, 11, 1010)

    school.add_student(student1)
    school.add_student(student2)
    school.add_student(student3)
    school.add_student(student4)

    school.show_students()