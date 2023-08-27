from dog import Dog

class Vida(Dog):
    """A simple Dog class"""

    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print(f"Food {self.name} Food!")

    def other_bark(self):
        print(f"{self.name} Bark!")