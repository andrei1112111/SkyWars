# рендер моделей
import pygame


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


class ModelRender:
    pass
