class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"hello {self.name}   ")

    def walk(self):
        print(f"{self.name} is walking")

    def __str__(self):
        return f"{self.name}"

human1 = Human("esther")
human2 = Human("torin")
human1.walk()
human1.greet()
human2.greet()

print(human1.name)
print(human1)