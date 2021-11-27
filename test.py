import pygame

WIDTH = 1000
HEIGHT = 1000
FPS = 144

BLACK = (169, 169, 169)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

model_fon = (187, 255, 0)
plain1 = [pygame.image.load(f'res/plains/plaint1/{i}.png').convert() for i in range(9)]
plain2 = [pygame.image.load(f'res/plains/plaint2/{i}.png').convert() for i in range(9)]
plain3 = [pygame.image.load(f'res/plains/plaint3/{i}.png').convert() for i in range(9)]
plain4 = [pygame.image.load(f'res/plains/plaint4/{i}.png').convert() for i in range(9)]
plain5 = [pygame.image.load(f'res/plains/plaint5/{i}.png').convert() for i in range(9)]
[plain1[i].set_colorkey((213, 213, 213)) for i in range(9)]
[plain2[i].set_colorkey((208, 208, 208)) for i in range(9)]
[plain3[i].set_colorkey((255, 255, 255)) for i in range(9)]
[plain4[i].set_colorkey((229, 229, 229)) for i in range(9)]
[plain5[i].set_colorkey((213, 213, 213)) for i in range(9)]


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = se[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2 + HEIGHT / 4)

    def update(self, img):
        if img:
            self.image = img


se = plain1
player = Player()
all_sprites.add(player)
running = True
k = 0
kk = 1
while running:
    clock.tick(FPS)
    img = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                k += 1
                img = se[k]
                if k == 8:
                    k = -1
                    kk += 1
                    try:
                        exec(f"se = plain{kk}")
                    except NameError:
                        running = False
    all_sprites.update(img)
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.draw.circle(screen, (255, 255, 255), (WIDTH / 2, HEIGHT / 2 + HEIGHT / 12), 5)
    pygame.display.flip()
else:
    from time import sleep

    sleep(3)
pygame.quit()
