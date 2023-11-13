import pygame

FPS = 60
RED = (255,0,0)

pygame.init()

pygame.display.set_caption("HRA")

WIDTH, HEIGHT = 1280, 800

win = pygame.display.set_mode((WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite):
    GRAVITY = 1
    OFFSET_X = 100

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.vel = 0
        self.fall_count = 0
        self.width = width
        self.height = height

    def jump(self):
        self.vel = -self.GRAVITY 
        self.fall_count = 0

    def move(self, vel):
        self.rect.y += vel
        
    def loop(self, fps):
        self.vel = self.fall_count/fps * self.GRAVITY*5
        self.move(self.vel)
        self.fall_count += 1

    def draw(self, win):
        pygame.draw.rect(win, RED, (self.OFFSET_X, self.rect.y, self.width, self.height))

    def update(self):
        self.rect = pygame.Rect(self.OFFSET_X, self.rect.y, self.width, self.height)


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)


def death():
    pygame.quit()
    quit()
    

def main(win):
    clock = pygame.time.Clock()

    player = Player(300, HEIGHT/2, 50, 50)


    run = True
    while run:
        clock.tick(FPS)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        player.loop(FPS)
        player.draw(win)
        player.update()
        if player.rect.bottom >= HEIGHT:
            death()
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(win)