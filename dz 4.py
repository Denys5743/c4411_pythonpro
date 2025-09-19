import random

brand_of_car = {
    "Bmw": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}
}

job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25}
}


class Pet:
    def __init__(self, name="Buddy"):
        self.name = name
        self.happiness = 50

    def play(self):
        print(f"You played with your pet {self.name}!")
        self.happiness += 10
        return 5


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.consumption = brand_list[self.brand]["consumption"]
        self.strength = brand_list[self.brand]["strength"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.strength -= 1
            self.fuel -= self.consumption
            return True
        else:
            print("The car doesn't move")
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


class Human:
    def __init__(self, name="Human", job=None, car=None, home=None):
        self.name = name
        self.job = job
        self.car = car
        self.home = home
        self.gladness = 50
        self.satiety = 50
        self.money = 100
        self.pet = Pet()

    def get_car(self):
        self.car = Auto(brand_of_car)

    def get_home(self):
        self.home = House()

    def get_job(self):
        if self.car.drive():
            self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")

    def shopping(self, manage):
        if not self.car.drive():
            if self.car.fuel < 20:
                self.car.fuel += 100
                self.money -= 100
            return

        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("I bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Horray! Bought delicacies")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self, manage="clean"):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        print(f"\n=== Day {day} of {self.name}'s life ===")
        print(f"Money: {self.money}")
        print(f"Satiety: {self.satiety}")
        print(f"Gladness: {self.gladness}")
        print("--- Home ---")
        print(f"Food: {self.home.food}")
        print(f"Mess: {self.home.mess}")
        print("--- Car ---")
        print(f"Fuel: {self.car.fuel}")
        print(f"Strength: {self.car.strength}")
        print("--- Pet ---")
        print(f"Happiness: {self.pet.happiness}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression")
            return False
        if self.satiety < 0:
            print("Dead from hunger")
            return False
        if self.money < -100:
            print("Bankrupt")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False
        if self.home is None:
            self.get_home()
        if self.car is None:
            self.get_car()
        if self.job is None:
            self.get_job()

        self.days_indexes(day)
        dice = random.randint(1, 6)

        if self.satiety < 20:
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                self.clean_home()
            else:
                self.chill()
        elif self.money <= 0:
            self.work()
        elif self.car.strength < 15:
            self.to_repair()
        elif dice == 1:
            self.chill()
        elif dice == 2:
            self.work()
        elif dice == 3:
            self.clean_home()
        elif dice == 4:
            self.shopping(manage="delicacies")
        elif dice == 5:
            self.gladness += self.pet.play()

        return True


nick = Human(name="Vasya")
for day in range(1, 8):
    if not nick.live(day):
        break
