# Thayer Yang
# 13 MAY 2025
# Inheritance

class Human:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def think(self):
        print("The human is thinking deeply.")

    def communicate(self):
        print("The human is communicating clearly.")

class AI(Human):
    def __init__(self, name, age, occupation, intelligence_level):
        self.intelligence_level = intelligence_level
        super().__init__(name, age, occupation)

    def think(self):
        print("The A`perform_task()` online.")

    def communicate(self):
        print("The AI is communicating digitally with its human.")

    def learn(self):
        print("The AI is learning and improving its capabilities.")

    def analyze(self):
        print("The AI is analyzing its tasks")

class Robot(Human):
    def __init__(self,name, age, occupation, model, condition):
        super().__init__(name,age,occupation)

        self.model = model
        self.condition = condition

    def think(self):
        print(f"{self.name} is awaiting a task")

    def communicate(self):
        print(f"{self.name} is beeping various frequencies")

    def perform_task(self):
        print(f"{self.name} is performing the given task")

my_ai = AI("Athena", 5, "Virtual Assistant", 9.8)
print(my_ai.name)
print(my_ai.age)
print(my_ai.occupation)
print(my_ai.intelligence_level)
my_ai.think()
my_ai.communicate()
my_ai.learn()

ai1 = AI("RICK", 44, "PICKLE", 11.2)
ai1.analyze()

robo = Robot("TyRob", 12, "Lever Handler", "SB Mini", "Factory New")

robo.perform_task()