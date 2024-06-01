class warrior:
    def __init__(self, name, health=int, energy=100):
        self.name = name
        self.health = health 
        self.energy = energy

    def attack(self, target, damage = 1):
        target.health -= damage
        self.energy -= damage
        print(f"{self.name} attacking {damage} damage to {target.name}")
        if target.is_attacked(warrior_name=self.name):
            self.health -= target.damage

    def needhealing(self, target, needhp = 1):
        target.usedheal -= needhp
        print(f"{self.name} need healing")
        if target.is_needhealing(warrior_name=self.name):
            self.health += target.healing

    def show_info(self):
        print(f"{self.name} health: {self.health}")
        print(f"{self.name} energy: {self.energy}")


class healer:
    def __init__(self, name, health=int, energy=100, usedheal=10):
        self.name = name
        self.health = health
        self.usedheal = usedheal
        self.usedheal_init = self.usedheal
        self.energy = energy
        self.healing = 5
    
    def is_needhealing(self, warrior_name):
        print(f"{self.name} heal {self.healing} hp to {warrior_name}")
        return self.usedheal < self.usedheal_init

    def show_info(self):
        print(f"{self.name} health: {self.health}")


class monster:
    def __init__(self, name, health=int):
        self.name = name
        self.health = health
        self.health_init = self.health
        self.damage = 30

    def is_attacked(self, warrior_name):
        print(f"{self.name} attack {self.damage} damage to {warrior_name}")
        return self.health < self.health_init

    def show_info(self):
        print(f"{self.name} health: {self.health}")

hero1 = warrior(name="Arthur", health=100)
hero2 = healer(name="Estes", health=80)
maou = monster(name="Anos", health=500)

hero1.attack(target=maou, damage=80)

if hero1.health < 80:
    hero1.needhealing(target=hero2, needhp=1)

hero1.show_info()
hero2.show_info()
maou.show_info()