class Worker:
    def __init__(self):
        self.job = "Developer"
    def work(self):
        return f"Working as {self.job}"

class Athlete:
    def __init__(self):
        self.sport = "Football"
    def train(self):
        return f"Training in {self.sport}"

class Gamer:
    def __init__(self):
        self.game = "Minecraft"
    def play(self):
        return f"Playing {self.game}"

class SuperHuman(Worker, Athlete, Gamer):
    def __init__(self):
        Worker.__init__(self)
        Athlete.__init__(self)
        Gamer.__init__(self)

sh = SuperHuman()
print(sh.work())
print(sh.train())
print(sh.play())
