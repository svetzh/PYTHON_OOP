<<<<<<< HEAD
from project.elf import Elf
from project.hero import Hero

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
=======
from project.elf import Elf
from project.hero import Hero

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
>>>>>>> 276765b8e88ecb03013f4fe22c25ddcd3699ae0d
print(elf.level)