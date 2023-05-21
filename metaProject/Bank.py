from abc import ABC, abstractmethod


class Bank(ABC):
    def basic_info(self)->str:
        print("This is a generic bank")
        return "Generic bank: 0"

    @abstractmethod
    def withdraw(self):
        pass
