from random import randint


class Die:
    # 单个骰子🎲 1-num_sides 的类
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
