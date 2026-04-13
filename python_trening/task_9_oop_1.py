from task_9_checks import Checks


class Button(Checks):
    def __init__(self, loc, text=""):

        super().__init__(loc)
        self.text = text

    def click(self):

        print(f"Клик по кнопке с локатором: {self.loc}")



class InputField(Checks):
    def __init__(self, loc, placeholder=""):

        super().__init__(loc)
        self.placeholder = placeholder

    def input_text(self, text):

        print(f"Ввод текста '{text}' в поле с локатором: {self.loc}")


class Link(Checks):
    def __init__(self, loc, href=""):

        super().__init__(loc)
        self.href = href

    def open(self):

        print(f"Открытие ссылки с локатором: {self.loc}")


class Image(Checks):
    def __init__(self, loc, alt=""):

        super().__init__(loc)
        self.alt = alt

    def display(self):

        print(f"Отображение изображения с локатором: {self.loc}")



button = Button("//button[@id='submit']", "Отправить")
input_field = InputField("//input[@name='username']", "Введите имя пользователя")
link = Link("//a[@href='/about']", "/about")
image = Image("//img[@alt='logo']", "Логотип компании")


print("Результаты вызова метода check_text():")
print(f"Кнопка: {button.check_text()}")
print(f"Поле ввода: {input_field.check_text()}")
print(f"Ссылка: {link.check_text()}")
print(f"Изображение: {image.check_text()}")
