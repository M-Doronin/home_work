from car import Car


my_car = Car("красный", "седан", 2020)


print(f"Начальные характеристики: цвет — {my_car.color}, тип — {my_car.type}, год — {my_car.year}")
print()


my_car.start_engine()
my_car.stop_engine()
print()


my_car.set_year(2023)
my_car.set_type("внедорожник")
my_car.set_color("синий")
print()


print(f"Обновлённые характеристики: цвет — {my_car.color}, тип — {my_car.type}, год — {my_car.year}")
