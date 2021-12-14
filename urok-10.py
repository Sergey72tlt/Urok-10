from datetime import date

class Enterprise:
    _emploees = []

    def __init__(self, capital: int):
        self.capital = capital

    @property
    def emploees(self):
        return self._emploees

    def _get_other_capital(self):
        other_capital = self.capital
        for emploee in self.emploees:
            other_capital -= emploee.salary

        return other_capital


    def add_emploee(self, new_emploee):
        other_capital = self._get_other_capital()
        if new_emploee.salary > other_capital:
            # error_msg = 'У нас нет денег ему на зарплату'.format(new_emploee)
            # raise ValueError(error_msg)
            print(f'У нас нет денег на зарплату', new_emploee)
        else:
            print(f' {new_emploee} принят на работу')
            self._emploees.append(new_emploee)


class People:
    def __init__(self, name: str, surname: str, patronomyc: str, byrth_date: date, phone: str):
        self.name = name
        self.surname = surname
        self.patronomyc = patronomyc
        self.byrth_date = byrth_date
        self.phone = phone


class Emploee(People):
    def __init__(self, name: str, surname: str, patronomyc: str,
                 byrth_date: date, phone: str, id: int, dep_code: int, salary: float):
        super().__init__(name, surname, patronomyc, byrth_date, phone)
        self.id = id
        self.dep_code = dep_code
        self.salary = salary

    def __str__(self):
        return ' '.join((self.name, self.surname))


if __name__=='__main__':
    zavod = Enterprise(10000)
    emploee1 = Emploee('Иван', 'Иванов', 'Иванович', date(1992, 4, 25), '33-52-28', 10, 45, 2000)
    emploee2 = Emploee('Пётр', 'Петров', 'Петрович', date(1989, 7, 2), '33-85-35', 10, 12, 2500)
    emploee3 = Emploee('Семен', 'Семенов', 'Семенович', date(1990, 5, 17), '32-01-83', 10, 12, 5000)
    emploee4 = Emploee('Олег', 'Сидоров', 'Васильевич', date(1952, 9, 1), '22-61-93', 10, 11, 7000)

    zavod.add_emploee(emploee1)
    zavod.add_emploee(emploee2)
    zavod.add_emploee(emploee3)
    zavod.add_emploee(emploee4)
