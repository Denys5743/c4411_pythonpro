class Pet:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        self.energy = 50
        self.happiness = 50
        self.hungry = 50
        self.alive = True

    def sleep(self):
        print(f"{self.name} спить")
        self.energy += 10
        self.hungry += 5

    def eat(self):
        print(f"{self.name} їсть")
        self.hungry -= 15
        self.energy += 5

    def play(self):
        print(f"{self.name} грається")
        self.happiness += 10
        self.energy -= 5
        self.hungry += 5

    def walk(self):
        if self.kind == "dog":
            print(f"{self.name} гуляє")
            self.happiness += 15
            self.energy -= 10
        else:
            print(f"{self.name} не хоче гуляти")

    def is_alive(self):
        if self.energy <= 0 or self.hungry >= 100 or self.happiness <= 0:
            print(f"{self.name} більше не з нами")
            self.alive = False

    def end_of_day(self):
        print(f"Енергія: {self.energy}")
        print(f"Щастя: {self.happiness}")
        print(f"Голод: {self.hungry}")
        print("-" * 20)

    def live(self, day):
        print(f"День {day}")
        action = random.choice(["sleep", "eat", "play", "walk"])
        getattr(self, action)()
        self.end_of_day()
        self.is_alive()

pet = Pet("Мурчик", "cat")

for day in range(1, 31):
    if not pet.alive:
        break
    pet.live(day)