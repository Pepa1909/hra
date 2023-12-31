import pygame

FPS = 60
RED = (255,0,0)
BLACK = (0,0,0)

pygame.init()

pygame.display.set_caption("HRA")

WIDTH, HEIGHT = 1280, 800

window = pygame.display.set_mode((WIDTH, HEIGHT))

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
        self.vel = -self.GRAVITY * 7
        self.fall_count = 0

    def move(self, vel):
        self.rect.y += vel
        
    def loop(self, fps):
        self.vel += self.fall_count/fps * self.GRAVITY / 2
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
        self.width = width
        self.height = height
        self.y = y

    def move(self, vel):
        self.rect.x -= vel
    
    def loop(self):
        self.vel = 5
        self.move(self.vel)

    def draw(self, win):
        pygame.draw.rect(win, RED, (self.rect.x, self.rect.y, self.width, self.height))

    def update(self):
        self.rect = pygame.Rect(self.rect.x, self.y, self.width, self.height)
def collide_upper(player, upper):
    if pygame.sprite.collide_rect(player, upper):
        death()
def collide_lower(player, lower):
    if pygame.sprite.collide_rect(player, lower):
        death()       

def death():
    pygame.quit()
    quit()
    

def main(win):
    clock = pygame.time.Clock()

    player = Player(300, HEIGHT/2, 50, 50)
    pipe1 = Pipe(WIDTH, 0, 30, 200)
    pipe2 = Pipe(WIDTH, HEIGHT-400, 30, 400)
    

    run = True
    while run:
        clock.tick(FPS)
        pygame.display.update()
        window.fill(BLACK)
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
        pipe1.loop()
        pipe2.loop()
        player.draw(win)
        pipe1.draw(win)
        pipe2.draw(win)
        player.update()
        pipe1.update()
        pipe2.update()
        collide_upper(player,pipe1)
        collide_lower(player, pipe2)
        if player.rect.bottom >= HEIGHT or player.rect.top <= 0:
            death()
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)