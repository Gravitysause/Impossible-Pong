import pygame


class Layout(pygame.sprite.Sprite):
    def __init__(self, surface, colour, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.surface = surface

        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        self.rect = self.image.get_rect()

    def draw(self):
        self.surfaec.blit(self.image, self.rect)
    
    def update(self):
        self.draw()
