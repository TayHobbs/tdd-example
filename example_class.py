class Person:

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.name} {self.last_name}'

    def math(self, method, a, b):
        result = 0
        if method == 'add':
            result = a + b
        if method == 'subtract':
            result a -
        return result

