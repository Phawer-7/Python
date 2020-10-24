class MyClass:
    def __init__(self):
        self.name = 'Phawer'
        self.name3 = 'Mrfire7'

    def method(self, message):
        # я узнал то что, написанный метод __init__ в классе, работает как глобалная переменная.Только всегда
        # необходимо добавлять префикс self
        print(self.name)
        print(self.name3)

        # как работает формат:
        print(f'{message}')
        print('{0}'.format(message))


MyClass().method('lol')

# в классах глобальные не работают, поэтому необходимо создавать метод __init__ , чуть ниже пример
# использования глобальных переменных. Повторюсь, в классах это не прокатит
name = 'Mrfire7'
name2 = 'Phawer'


def global_var():
    global name, name2
    print(name, name2)


global_var()