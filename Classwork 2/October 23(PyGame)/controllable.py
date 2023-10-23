import pygame

class Controllable():
    def __init__(self, controls = None):
        self.controls = controls if controls else self.default_controls()
    
    def default_controls(self):
        return (
            {"key" : pygame.K_w, "action" : lambda: print("up")},
            {"key" : pygame.K_a, "action" : lambda: print("left")},
            {"key" : pygame.K_d, "action" : lambda: print("right")},
            {"key" : pygame.K_s, "action" : lambda: print("down")}
            # K_клавиша означает что при нажатии будет вызываться функция
            # wsad - управление
        )

    def check_controls(self):
        keys = pygame.key.get_pressed()

        for x in self.controls:
            if keys[x["key"]]:
                x["action"]() # вызов как функцию