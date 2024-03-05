import random
from branch import Branch


def map_value(value, from_low, from_high, to_low, to_high):
    """
    Map a value from one range to another.

    :param value: The value to be mapped.
    :param from_low: The minimum value of the original range.
    :param from_high: The maximum value of the original range.
    :param to_low: The minimum value of the target range.
    :param to_high: The maximum value of the target range.
    :return: The mapped value.
    """
    if value < from_high and value < from_low:
        value = from_high
    if value > from_high and value > from_low:
        value = from_high
    if value < from_low and value < from_high:
        value = from_low
    if value > from_low and value > from_high:
        value = from_low
    from_range = from_high - from_low
    to_range = to_high - to_low

    scaled_value = float(value - from_low) / float(from_range)

    return to_low + (scaled_value * to_range)


class RecursiveTree:

    def __init__(self, start_pos_x, start_pos_y, color, age, length, width, divergence_weight: int = None):
        self.color = color
        self.length = length
        self.width = width
        self.age = age
        self.divergence_weight = divergence_weight

        self.branches = []
        self.root = Branch(start_pos_x, start_pos_y, start_pos_x, start_pos_y - length, width, self.color)
        self.branches.append(self.root)

    def get_div_weight(self):
        if self.divergence_weight is None:
            return random.randrange(30, 50)
        else:
            return self.divergence_weight

    def grow(self):
        if not self.age <= 0:
            for i in range(len(self.branches)-1, -1, -1):
                if not self.branches[i].finish:
                    self.branches.append(self.branches[i].branch_right(self.get_div_weight()))
                    self.branches.append(self.branches[i].branch_left(self.get_div_weight()))
                self.branches[i].finish = True
            self.age -= 1
            self.grow()

    def display(self, screen):
        for branch in self.branches:
            branch.display(screen)
