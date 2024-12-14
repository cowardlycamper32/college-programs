import random as rand

class Types:
    def __init__(self, immune, veffective):
        self.immune = immune
        self.veffective = veffective

    def isImmune(self, target):
        return self.immune == target
    def isEffective(self, target):
        return self.veffective == target

class Attacks:
    def __init__(self, name, dmg, type, chancetohit: float = 1.00, heals = False):
        self.dmg = dmg
        self.name = name
        self.heals = heals
        if heals:
            self.dmg = -self.dmg
        self.chancetohit = chancetohit

class Fighter:
    def __init__(self, name, health, type, attacks, immunes, veffective):
        self.name = name
        self.health = health
        self.attacks = attacks
        self.immunes = immunes
        self.veffective = veffective
        self.type = type
    def attack(self, num, target):
        temp = rand.randrange(0, self.attacks[num-1])
        if temp < self.attacks[num-1].chancetohit:
            temp2 = self.checkTypes(target, self.attacks[num-1].type, False)
            if temp2 == "immune":
                pass
            elif temp2 == "effective":
                pass
            elif temp2 == "neutral":
                pass
            else:
                print("HOW DA FUCK DID YOU GET HERE")
                exit()


    def checkTypes(self, target, attack, incoming):
        if incoming:
            if self.type.isImmune(target):
                return "immune"
            else: return "neutral"
        else:
            if attack.type.isEffective(target):
                return "effective"
            else:
                return "neutral"
