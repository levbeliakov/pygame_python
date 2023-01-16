import pygame
import os
import sys
#hahaha

line =[0] * 10
tetris = []
for i in range(20):
    tetris.append(line[:])

tetris[0][1] = 1
tetris[1][1] = 1
tetris[3][5] = 1
tetris[12][5] = 1

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

def load_image(name, colorkey=None):
    image = pygame.image.load(os.path.join('data', name))
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
player_image = load_image('chel.png', -1)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(pos_x, pos_y)


class b(pygame.sprite.Sprite):
    image = load_image("b.png")

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = b.image
        self.rect = self.image.get_rect().move(y, x)
        self.act = True


    def update(self, *args):
        if args:
            print(1)
            if args[0] == 768:
                print(2)
                if tetris[self.rect.y // 40][self.rect.x // 40] == 1:
                    tetris[self.rect.y // 40][self.rect.x // 40] = 0
                    tetris[self.rect.y // 40][self.rect.x // 40  -1] = 1
                    print(3)
        elif self.rect.y // 40 + 1 == 20 or tetris[self.rect.y // 40 + 1][self.rect.x // 40] == 2:
            tetris[self.rect.y // 40][self.rect.x // 40] = 2
        else:
            tetris[self.rect.y // 40][self.rect.x // 40] = 0
            tetris[self.rect.y // 40 + 1][self.rect.x // 40] = 1
            self.kill()

def update_tetris():
    for i in range(len(tetris) - 1, -1, -1):
        for j in range(len(tetris[i])):
            if tetris[i][j] == 1 or tetris[i][j] == 2:
                b(40 * i, 40 * j)
                continue


def new_figure():
    pass


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('tetris')
    size = width, height = 400, 800
    screen = pygame.display.set_mode(size)
    screen.fill([255, 255, 255])
    Player(100, 100)
    running = True
    fps = 60
    stepp = 2
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(event.type)
                all_sprites.update(event.type)
                print(23)
            if event.type == pygame.QUIT:
                running = False
        if stepp % 30 == 0:
            all_sprites.update()
        update_tetris()
        screen.fill([255, 255, 255])
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
        stepp += 1
    pygame.quit()