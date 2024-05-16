#!/usr/bin/python3

from archer import Archer
from hero import Hero
from knight import Knight
from wizzard import Wizzard


joe = Hero("Joe", "Spear")
# print(joe)
# joe.attack()

mike = Archer("Mike")
# print(mike)
# mike.attack()

jake = Knight("Jake")
# print(jake)
# jake.attack()
# jake.defend()

tina = Wizzard("Tina")
# print(tina)
# tina.cast_spell("Magic Missile")
# tina.attack()

heroes = [joe, mike, jake, tina]
for hero in heroes:
    hero.attack()