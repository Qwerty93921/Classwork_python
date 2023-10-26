import pygame
from animatedsprite import AnimatedSprite
from block import Block

class Application():
    FPS = 25
    icon = 'resources/pygamelogo.png'
    background_color = (60, 60, 60)
    objects = []

    def __init__(self, size, title):
        self.size = size
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        image = pygame.image.load(self.icon)
        pygame.display.set_icon(image)
        # self.player = Block((50, 50), "yellow")
        self.player = AnimatedSprite(1.2, 'resources/sprites/anime_boy', 12, controllable=True)
        self.player.placeTo(self.screen)
        b = Block((50, 100), "green") # (50, 100) - КОРТЕЖ пикселей, КРУГЛЫЕ СКОБКИ а не КВАДРАТНЫЕ
        b.set_object_list(self.objects)
        self.player.set_object_list(self.objects)
        b.placeTo(self.screen)
        b.set_position((400, 300)) # кортеж, можно написать tuple([400, 300]) с квадратными скобками
        self.objects.append(self.player)
        self.objects.append(b)

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for n in self.objects:
                n.check_controls()

            self.screen.fill(self.background_color)
            for n in self.objects:
                n.show()

            pygame.display.update()
            clock.tick(self.FPS)
        pygame.quit()
