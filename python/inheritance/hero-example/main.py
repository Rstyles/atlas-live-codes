#!/usr/bin/python3
from hero import Hero
from archer import Archer
from knight import Knight
from wizzard import Wizzard

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
