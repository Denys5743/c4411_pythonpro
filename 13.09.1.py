import random
brand_of_car = {
    "Bmw": {"fuel":100, "strenhth":100,
            "сonsuprion": 6},
    "Lada": {"fuel":50, "strenhth":40,
            "сonsuprion": 10},
    "Volvo": {"fuel":70, "strenhth":150,
            "сonsuprion": 8},
    "Ferrari": {"fuel":80, "strenhth":120,
            "сonsuprion": 14}
}
job_list = {
    "Java developer": {"salary":50, "gadness_less":10}
    "Python developer": {"salary":40, "gadness_less":3}
    "C++ developer": {"salary":45, "gadness_less":25}


}
class Human:
    def __init__(self, name="Human",job=None,car=None,home=None):
        self.name = name
        self.job = job
        self.car = car
        self.home = home
        self.gladness = 50
        self.satiety = 50
        self.money = 100
    def get_car(self):
        self.car = auto(brand_of_car)
    def get_home(self):
        self.home = House()
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_remove()
            return
        self.job = job(job_list)
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
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                return
        self.money += self.job.salary
        self.gladness += self.job.gadness_less
        self.satiety -= 4
    def shopping(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
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
            print("Horray")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
    def clean_home(self, manage):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strenhth += 100
        self.money -= 50


    def days_indexes(self, day):
        print(f"today the {day}of{self.name} life")
        print(f"money -{self.money}")
        print(f"satiety -{self.satiety}")
        print(f"gladness -{self.gladness}")
        print("home")
        print(f"food - {self.home.food}")
        print(f"mess - {self.home.mess}")
        print("car")
        print(f"fuel - {self.car.fuel}")
        print(f"strenhth - {self.car.strenhth}")

    def is_alive(self):
        if self.gladness < 0:
            print("depression")
            return False
        if self.satiety < 0:
            print("dead")
            return False
        if self.money <- 0:
            print("bankrupt")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"{self.car.brand}")
            if self.job is None:
                self.get_job()
                print(f"{self.job.job}")
            self.days_indexes(day)
            dice = random.randint(1,4)
            if self.satiety < 20:
                self.eat()
            elif self.gladness < 20:
                if self.home.mess > 15:
                    self.clean_home()
                else:
                    self.chill()
            elif self.money > 0:
                self.work()
            elif self.car.strenhth < 15:
                self.to_repair()
            elif dice == 1:
                self.chill()
            elif dice == 2:
                self.work()
            elif dice == 3:
                self.clean_home()
            elif dice == 4:
                self.shopping(manage="delicacies")



class  auto:
    def __init__(self,brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.consumprion = brand_list[self.brand]["consumprion"]
        self.strength = brand_list[self.brand]["strength"]

    def driver(self):
        if self.strength > 0 and self.fuel > self.consumprion:
            self.strength -= 1
            self.fuel -= self.consumprion
            return True
        else:
            print("The car not move")
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

nick = Human(name="Vasya")
for day in range(1,8):
    if nick.live() == False:
        break


