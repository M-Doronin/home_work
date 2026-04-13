#task_1
class Rectangle:
    def __init__(self, width, height):

        self.width = width
        self.height = height

    def area(self):

        return self.width * self.height

    def perimeter(self):

        return 2 * (self.width + self.height)



rect1 = Rectangle(5, 3)
rect2 = Rectangle(10, 4)
rect3 = Rectangle(7, 7)


print("Прямоугольник 1:")
print(f"Ширина: {rect1.width}, Высота: {rect1.height}")
print(f"Площадь: {rect1.area()}")
print(f"Периметр: {rect1.perimeter()}")
print()

print("Прямоугольник 2:")
print(f"Ширина: {rect2.width}, Высота: {rect2.height}")
print(f"Площадь: {rect2.area()}")
print(f"Периметр: {rect2.perimeter()}")
print()

print("Прямоугольник 3:")
print(f"Ширина: {rect3.width}, Высота: {rect3.height}")
print(f"Площадь: {rect3.area()}")
print(f"Периметр: {rect3.perimeter()}")



#task_2
class Math:
    def __init__(self, a, b):

        self.a = a
        self.b = b

    def addition(self):

        result = self.a + self.b
        print(f"Сложение: {self.a} + {self.b} = {result}")


    def multiplication(self):

        result = self.a * self.b
        print(f"Умножение: {self.a} × {self.b} = {result}")

    def division(self):
        
        if self.b == 0:
            print("Ошибка: деление на ноль невозможно")
        else:
            result = self.a / self.b
            print(f"Деление: {self.a} ÷ {self.b} = {result}")

    def subtraction(self):

        result = self.a - self.b
        print(f"Вычитание: {self.a} - {self.b} = {result}")




print("Пример 1: числа 10 и 5")
math1 = Math(10, 5)
math1.addition()
math1.multiplication()
math1.division()
math1.subtraction()

print("\nПример 2: числа 8 и 3")
math2 = Math(8, 3)
math2.addition()
math2.multiplication()
math2.division()
math2.subtraction()

print("\nПример 3: числа 15 и 0 (проверка деления на ноль)")
math3 = Math(15, 0)
math3.addition()
math3.multiplication()
math3.division()
math3.subtraction()



#task_3
class SidebarButton:
    def __init__(self, text, button_type="Кнопка", locator=""):
        self.text = text
        self.type = button_type
        self.locator = locator

    def click(self):
        return f"Клик по кнопке {self.text}"

    def get_text(self):
        return self.text


buttons = [
    SidebarButton("Text Box"),
    SidebarButton("Check Box"),
    SidebarButton("Radio Button"),
    SidebarButton("Web Tables"),
    SidebarButton("Buttons"),
    SidebarButton("Links"),
    SidebarButton("Broken Links - Images"),
    SidebarButton("Upload and Download"),
    SidebarButton("Dynamic Properties")
]


print("Тексты всех кнопок сайдбара:")
for button in buttons:
    print(button.get_text())


print("\nРезультаты кликов по кнопкам:")
for button in buttons:
    print(button.click())
