def task_1() -> None:
    my_int: int = 42
    my_float: float = 3.14
    my_str: str = "Привет, мир!"
    my_list: list = [1, 2, 3, "элемент", True]
    my_bool: bool = True

    print(f"Тип переменной my_int: {type(my_int)}")
    print(f"Тип переменной my_float: {type(my_float)}")
    print(f"Тип переменной my_str: {type(my_str)}")
    print(f"Тип переменной my_list: {type(my_list)}")
    print(f"Тип переменной my_bool: {type(my_bool)}")

task_1()


def task_2() -> None:

    a = [1, 2, 3, 5, 8, 13, 21]

    print("Первые 3 значения списка:", a[:3])


task_2()


def task_3(number: float) -> float:

    return number ** 2

print("Квадрат числа 5:", task_3(5))
print("Квадрат числа 3.5:", task_3(3.5))
