import pygame
from objects import Player
from render import MapRender


class SkyWars:
    def __init__(self):
        self.size = self.width, self.height = (800, 450)
        self.screen = pygame.display.set_mode(self.size, pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.map_render = MapRender(self)

    def update(self):
        self.player.update()
        self.map_render.update()

    def draw(self):
        self.map_render.draw()
        pygame.display.flip()

    def run(self):
        while True:
            self.clock.tick(144)
            pygame.display.set_caption(f'FPS: {self.clock.get_fps()}')
            
            # отрисовка
            self.update()
            self.draw()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    exit(-1)


if __name__ == '__main__':
    game = SkyWars()
    game.run()
