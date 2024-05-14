
##################################
#          hero.py               #
##################################
class Hero:
    def __init__(self, name: str, weapon: str) -> None:
        self.name = name
        self.weapon = weapon

    def attack(self) -> None:
        print(f"{self.name} is attacking with a {self.weapon}")

    def __str__(self) -> str:
        return f"{self.name} is a(n) {self.__class__.__name__} and is equiped with a {self.weapon}"


##################################
#          archer.py             #
##################################
class Archer(Hero):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Bow")


##################################
#          knight.py             #
##################################
class Knight(Hero):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Sword")

    def defend(self) -> None:
        print(f"{self.name} is defending with a Shield")


##################################
#          wizzard.py            #
##################################
class Wizzard(Hero):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Staff")

    def cast_spell(self, spell: str) -> None:
        print(f"{self.name} is casting {spell}")

    def attack(self) -> None:
        self.cast_spell("Fireball")


mike = Hero("Mike", "Spear")
# print(mike)
# mike.attack()

joe = Archer("Joe")
# print(joe)
# joe.attack()

jake = Knight("Jake")
# print(jake)
# jake.attack()
# jake.defend()

tina = Wizzard("Tina")
# print(tina)
# tina.cast_spell("Defensive Ward")
# tina.attack()

heroes = [mike, joe, jake, tina]
for hero in heroes:
    hero.attack()
