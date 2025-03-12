class Human:
    def __init__(self):
        self.eyes = 2
        self.nose = 1

    def speak(self):
        print("I Can Speak")

    def eat(self):
        print("I Can Eat")

class Male(Human):
    def __init__(self, heart):
        super().__init__()
        self.heart = heart

    def work(self):
        print("I Can Work")


man1 = Human()
man1.heart = 1

man2 = Male(1)


man1.speak()
man1.eat()
man2.work()