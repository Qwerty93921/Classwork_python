import pygame
from controllable import Controllable

class Block(Controllable):

    SPEED = 5

    def __init__(self, size, color):
        self.size = size
        self.color = color
        self.position = [0,0]
        super().__init__()
        self.body = pygame.Surface(size)
        self.body.fill(self.color)
        

    def default_controls(self):
        return (
            {"key": pygame.K_w, "action": self.moveUp},
            {"key": pygame.K_a, "action": self.moveLeft},
            {"key": pygame.K_d, "action": self.moveRight},
            {"key": pygame.K_s, "action": self.moveDown}
        )     

    def set_position(self, position):
        self.hide()
        self.position = position
        self.show()

    def moveUp(self):
        self.position[1] -= self.SPEED
    
    def moveDown(self):
        self.position[1] += self.SPEED

    def moveLeft(self):
        self.position[0] -= self.SPEED

    def moveRight(self):
        self.position[0] += self.SPEED
    
    def show(self):
        self.owner.blit(self.body, self.position)
    
    def placeTo(self, owner):
        self.owner = owner
