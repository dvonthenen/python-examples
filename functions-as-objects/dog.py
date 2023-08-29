from typing import Any


class Dog:
    """A simple Dog class"""

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} Bark!")

    def speak_name(self, name="Doggo"):
        print(f"Bark {name} Bark!")

    def __call__(self):
        self.bark()