from Inheritance_exer_03_Monsters.elf import Elf
from Inheritance_exer_03_Monsters.hero import Hero

hero = Hero('H', 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf('E', 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)