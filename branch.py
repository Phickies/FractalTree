import math
import pygame

color_change = 10


class Branch:

    finish = False

    def __init__(self, x, y, next_x, next_y, width, color):
        self.x = x
        self.y = y
        self.next_x = next_x
        self.next_y = next_y
        self.width = width
        self.color = color
        self.angle = self.set_angle()
        self.length = math.sqrt(pow(next_x-x, 2) + pow(next_y-y, 2))

    def set_begin(self, x, y):
        self.x = x
        self.y = y

    def set_end(self, x, y):
        self.next_x = x
        self.next_y = y

    def get_begin(self):
        return pygame.Vector2(self.x, self.y)

    def get_end(self):
        return pygame.Vector2(self.next_x, self.next_y)

    def set_angle(self):
        return math.degrees(math.atan2(self.next_y-self.y, self.next_x-self.x))

    def set_color_right(self):
        if self.color[0]+color_change > 255 or self.color[1]+color_change > 255 or self.color[2]+color_change > 255:
            new_color = pygame.Color(255, 255, 255)
        else:
            new_color = pygame.Color(self.color[0]+color_change, self.color[1]+color_change, self.color[2]+color_change)
        return new_color

    def set_color_left(self):
        if self.color[0]-color_change < 0 or self.color[1]-color_change < 0 or self.color[2]-color_change < 0:
            new_color = pygame.Color(0, 0, 0)
        else:
            new_color = pygame.Color(self.color[0]-color_change, self.color[1]-color_change, self.color[2]-color_change)
        return new_color

    def branch_left(self, coefficient) -> 'Branch':
        new_next_x = self.next_x + math.cos(math.radians(self.angle-coefficient)) * self.length*0.67
        new_next_y = self.next_y + math.sin(math.radians(self.angle-coefficient)) * self.length*0.67
        new_color = self.set_color_left()
        return Branch(self.next_x, self.next_y, new_next_x, new_next_y, self.width, new_color)

    def branch_right(self, coefficient) -> 'Branch':
        new_next_x = self.next_x + math.cos(math.radians(self.angle+coefficient)) * self.length*0.67
        new_next_y = self.next_y + math.sin(math.radians(self.angle+coefficient)) * self.length*0.67
        new_color = self.set_color_right()
        return Branch(self.next_x, self.next_y, new_next_x, new_next_y, self.width, new_color)

    def display(self, screen):
        pygame.draw.line(screen, self.color, self.get_begin(), self.get_end(), self.width)
