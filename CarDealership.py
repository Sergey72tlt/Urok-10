class CarDealership:
    def __init__(self, salon_name):
        """
        car_dict - будет хранить словарик машин, вида
        {
            машина: [количество_в_наличии, количество_проданных],
        }
        :param salon_name: неазвание салона оп рподаже тачек
        """
        self.car_dict = {}
        self.name = salon_name

    def add_car(self, new_car, amount):
        """
        Метод для добавление новых тачек в салон
        :param new_car: новая тачка
        :param amount: количество на добавление
        """
        amount_available, amount_sold = self.car_dict.get(new_car, [0, 0])
        print("\nВ салоне тачек типа {} было в наличии: {}, было уже продано: {}".format(new_car, amount_available,
                                                                                       amount_sold))
        print(f"Добавлено: {amount}\n")
        self.car_dict.update({new_car: [amount_available + amount, amount_sold]})

    def sell_car(self, car, amount):
        """
        Метод для продажи тачек из салона
        :param car: тачка на продажу
        :param amount: количество тачек на продажу
        :return: возвращает True, если успешная продажа или False, если продать не получилось
        """
        # проверка что тачек в салоне достаточно для продажи
        amount_available, amount_sold = self.car_dict.get(car, [0, 0])
        if amount_available >= amount:
            # тачек достаточно
            self.car_dict.update({car: [amount_available - amount, amount_sold + amount]})
            print(f"\nУспешная продажа тачки {car}")
            print(f"Продано {amount_sold + amount}")
            print(f"Осталось в наличии {amount_available - amount}\n")
            return True
        else:
            # тачек в салоне не достаточно для продажи
            print(f"\nТачек типа {car} в салоне недостаточно для продажи")
            print(f"Было запрошено {amount}")
            print(f"Сейчас в наличии {amount_available}\n")
            return False

    def show_cars(self):
        """
        Показывает все тачки из нашего салона
        """
        print(f'\nТачки в нашем салоне \"{self.name}\": ')
        if not self.car_dict:
            print("Пока что у нас пусто, ожидаем поставку в ближайшем времени\n")
        else:
            for car, amounts in self.car_dict.items():
                print(f"{car}: в наличии {amounts[0]}, продано {amounts[1]}")
            print("\n")


class Car:
    def __init__(self, unique_id: int, car_model: str, manufacturer_country: str, year_of_issue: int,
                 engine_capacity: int, price: int):
        self.unique_id = unique_id
        self.car_model = car_model
        self.manufacturer_country = manufacturer_country
        self.year_of_issue = year_of_issue
        self.engine_capacity = engine_capacity
        self.price = price


class Lorry(Car):
    def __init__(self, unique_id: int, car_model: str, manufacturer_country: str, year_of_issue: int,
                 engine_capacity: int, price: int, weight_restriction_of_carriage: int):
        super().__init__(unique_id, car_model, manufacturer_country, year_of_issue,
                         engine_capacity, price)
        self.weight_restriction_of_carriage = weight_restriction_of_carriage

    def __str__(self):
        return self.car_model


if __name__ == '__main__':
    car_showroom = CarDealership("Тачка на прокачку")
    car1 = Lorry(123, 'Mazda', 'Japan', 2021, 130, 2500000, 2500)
    car2 = Lorry(157, 'Toyota', 'Japan', 2021, 120, 3500000, 2450)
    car3 = Lorry(963, 'Lexus', 'Japan', 2021, 150, 8000000, 2750)

    car_showroom.show_cars()

    car_showroom.add_car(car1, 20)
    car_showroom.add_car(car2, 10)
    car_showroom.add_car(car3, 15)

    car_showroom.show_cars()

    car_showroom.sell_car(car1, 10)
    car_showroom.sell_car(car1, 5)
    car_showroom.sell_car(car2, 10)
    car_showroom.sell_car(car2, 5)
    car_showroom.sell_car(car3, 5)

    car_showroom.show_cars()