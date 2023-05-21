class Animal:

    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eating...")


class Mammals(Animal):
# i can also do multiple inheritance
    def __init__(self):
        super().__init__()
        self.weight = 6

    def __call__(self):
        pass

    def swim(self):
        print("swimming...")


class Fish:
    def swim(self):
        print("swimming...")


m = Mammals()
print(m.age)
