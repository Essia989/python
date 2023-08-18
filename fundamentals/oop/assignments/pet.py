class Pet:
    def __init__(self,name,type,tricks):
        self.name = name
        self.type = type
        self.tricks =tricks
        self.energy = 40
        self.health = 40

    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.health += 10
        self.energy += 5

    #PLAY()_METHOD_INCREASE_THE_PET_HEALTH_BY_5
    def play(self):
        self.health += 5
        return self

    #NOISE()_PRINT_OUT_THE_PET_SOUND
    def noise(self):
        print("WOOOOF")
        return self

cat = Pet("Nuggets", "cat","hide")
cat.noise()