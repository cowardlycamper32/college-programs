from random import randint
import os
from platform import system

def clearScreen():
    plat = system()
    if plat == "Windows":
        os.system("cls")
    else:
        os.system("clear")



class Attacks:
    def __init__(self, name, dmg, heals = False):
        self.dmg = dmg
        self.name = name
        self.heals = heals
        if heals:
            self.dmg = -self.dmg

class Fighter:
    def __init__(self, name, health, attacks):
        self.name = name
        self.health = health
        self.attacks = attacks
    def attack(self, num, target):
        chance = randint(0,3)
        if chance:
            print(self.name, "used",self.attacks[num-1].name)
            if self.attacks[num-1].heals:
                self.health -= self.attacks[num-1].dmg
            else:
                target.health -= self.attacks[num-1].dmg
        else:
            print(self.name, "failed to use", self.attacks[num - 1].name)
    def chooseAttack(self, cpu=False):
        if cpu:
            choice = randint(0, len(self.attacks)-1)
            return choice
            clearScreen()
        else:
            for i in range(len(self.attacks)):
                print(str(i+1) + ". " + self.attacks[i].name + " " + str(self.attacks[i].dmg) + " Damage")
            while True:
                try:
                    choice = int(input("Enter the attack:\n"))
                    if choice > len(self.attacks) or choice < 1:
                        raise IndexError
                    break
                except (ValueError, TypeError):
                    print("nah ah")
                except IndexError:
                    print("nah ah ah")
            clearScreen()
            return choice



def winCond(thanos, ironman):
    if ironman.health <= 0:
        print("Thanos wins")
        return True
    elif thanos.health <= 0:
        print("Ironman wins")
        return True

def battle(thanos, ironman, cpu):
    win = False
    while not win:
        if win:
            return
        item = thanos.chooseAttack()
        thanos.attack(item, ironman)
        print(thanos.name + " HP: " + str(thanos.health) + "\n" + ironman.name + " HP: " + str(ironman.health) + "\n")
        win = winCond(thanos, ironman)
        if win:
            return
        if cpu:
            item = ironman.chooseAttack(True)
            ironman.attack(item, thanos)
        else:
            item = ironman.chooseAttack()
            ironman.attack(item, thanos)
        print(thanos.name + " HP: " + str(thanos.health) + "\n" + ironman.name + " HP: " + str(ironman.health) + "\n")
        win = winCond(thanos, ironman)


thanos = Fighter("Thanos", 200, [Attacks("Heal", 50, True), Attacks("Punch", 50)])
ironman = Fighter("Ironman", 100, [Attacks("Heal", 5, True), Attacks("Lazer", 5)])

while True:
    try:
        cpu = int(input("[1] 2 Player\n[2] CPU")) - 1
        if cpu > 2 or cpu < 0:
            raise IndexError
        break
    except (ValueError, TypeError):
        print("nah ah")
    except IndexError:
        print("nah ah ah")

battle(thanos, ironman, cpu)
print("Exiting...")