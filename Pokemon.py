class Pokemon:
    def __init__(self, name, type, lvl, hp):
        self.name = name
        self.type = type
        self.lvl = lvl
        self.hp = hp

    def is_fainted(self):
        if self.hp <= 0:
            return True
        else:
            return False

    def evolvl(self):
        if self. lvl < 35:
            return 1
        if self.lvl >= 35:
            return 2