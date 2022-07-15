from abc import ABC, abstractmethod
from dataclasses import dataclass
from msilib.schema import Class
from select import select
from tkinter.messagebox import NO


class FlyBehavior(ABC):
    """Fly interfaces."""
    @abstractmethod
    def fly():
        raise NotImplemented

class FlyWithWing(FlyBehavior):
    def fly():
        print("Implementing duck flying")

class FlyNoWay(FlyBehavior):
    def fly():
        print("Can not implement flying")


class QuackBehavior(ABC):
    """Quack interface."""
    @abstractmethod
    def quack():
        raise NotImplemented

class Quack(QuackBehavior):
    def quack():
        print("Implementing duck quack")

class Squeak(QuackBehavior):
    def quack():
        print("rubber duckies squeak")

class MuteQuack(QuackBehavior):
    def quack():
        print("Can not quack")

class Duck:
    """The duck supper class"""
    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior) -> None:
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def fly(self):
        self.fly_behavior.fly()

    def quack(self):
        self.quack_behavior.quack()

    def swim(self):
        print("Swim implementing")

    def display(self):
        pass


class MallardDuck(Duck):
    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior) -> None:
        super().__init__(fly_behavior, quack_behavior)

    def display(self):
        print("Look like a MallardDuck")

class RubberDuck(Duck):
    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior) -> None:
        super().__init__(fly_behavior, quack_behavior)

    def display(self):
        print("Look like a RubberDuck")

class DecoyDuck(Duck):
    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior) -> None:
        super().__init__(fly_behavior, quack_behavior)

    def display(self):
        print("Look like a DecoyDuck")


def main() -> None:
    mallard_duck = MallardDuck(FlyWithWing, Quack)
    mallard_duck.display()
    mallard_duck.fly()
    mallard_duck.quack()
    print('*'*80)
    rubber_duck = RubberDuck(FlyNoWay, Squeak)
    rubber_duck.display()
    rubber_duck.fly()
    rubber_duck.quack()
    print('*'*80)
    decoy_duck = RubberDuck(FlyNoWay, MuteQuack)
    decoy_duck.display()
    decoy_duck.fly()
    decoy_duck.quack()

if __name__ == "__main__":
    main()