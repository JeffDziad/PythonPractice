import pygame
from random import randrange

GAME_HEIGHT = 800
GAME_WIDTH = 800
TILE_SIZE = 25
COLS = int(GAME_WIDTH / TILE_SIZE)
ROWS = int(GAME_HEIGHT / TILE_SIZE)
APPLE_LIMIT = 2

pygame.init()
screen = pygame.display.set_mode([GAME_HEIGHT, GAME_WIDTH])

pygame.display.set_caption('Python Snake')

clock = pygame.time.Clock()
speed = 10
running = True


# Objects
class Apple:
    def __init__(self):
        self.position = randSpawnPos()

    def draw(self):
        pygame.draw.circle(screen, "red", (self.position[0] - TILE_SIZE / 2, self.position[1] - TILE_SIZE / 2), TILE_SIZE / 2)


class Part:
    def __init__(self, start_x, start_y):
        self.rect = pygame.Rect(start_x, start_y)


class Snake:
    def __init__(self, start_x, start_y, direction="right"):
        self.alive = True
        self.parts = []

        self.rect = pygame.Rect(start_x, start_y, TILE_SIZE, TILE_SIZE)
        self.direction = direction

    def draw(self):
        pygame.draw.rect(screen, "blue", self.rect)

    def update(self):
        if self.alive:
            # Determine next position
            d = self.direction
            x, y = self.rect.x, self.rect.y
            if d == "up":
                y -= TILE_SIZE
            elif d == "down":
                y += TILE_SIZE
            elif d == "left":
                x -= TILE_SIZE
            elif d == "right":
                x += TILE_SIZE

            # Test new position for collisions
            if x + TILE_SIZE > GAME_WIDTH:
                self.alive = False
                x -= TILE_SIZE
            elif x < 0:
                x += TILE_SIZE
                self.alive = False
            elif y + TILE_SIZE > GAME_HEIGHT:
                y -= TILE_SIZE
                self.alive = False
            elif y < 0:
                y += TILE_SIZE
                self.alive = False

            # Apply new position
            self.rect.update((x, y), (TILE_SIZE, TILE_SIZE))

            # After update, check for apple collisions
            for apple in apples:
                if self.rect.x == apple.position[0] and self.rect.y == apple.position[1]:
                    print("Apple Collision")
        self.draw()


head = Snake(int((COLS / 2) * TILE_SIZE), int((ROWS / 2) * TILE_SIZE))
apples = []


def randSpawnPos():
    x, y = 0, 0
    found = False
    while not found:
        found = True
        (x, y) = round(randrange(0, COLS)) * TILE_SIZE, round(randrange(0, ROWS)) * TILE_SIZE
        if head.rect.x == x or head.rect.y == y:
            print("Head Convergence")
            found = False
        for apple in apples:
            if apple.position == (x, y):
                print("Apple Convergence")
                found = False
    # Test position for collisions to prevent overlap
    return x, y


def drawGrid():
    for col in range(0, COLS):
        x1 = TILE_SIZE * col
        y1 = 0
        x2 = TILE_SIZE * col
        y2 = GAME_HEIGHT
        pygame.draw.line(screen, "black", (x1, y1), (x2, y2))
    for row in range(0, ROWS):
        x1 = 0
        y1 = TILE_SIZE * row
        x2 = GAME_WIDTH
        y2 = TILE_SIZE * row
        pygame.draw.line(screen, "black", (x1, y1), (x2, y2))


def handleApples():
    if len(apples) < APPLE_LIMIT:
        for x in range(0, APPLE_LIMIT - len(apples)):
            a = Apple()
            print(a.position)
            apples.append(a)
    for apple in apples:
        apple.draw()


def updateGame():
    screen.fill((255, 255, 255))
    drawGrid()
    head.update()
    handleApples()


while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                head.direction = "up"
            elif event.key == pygame.K_DOWN:
                head.direction = "down"
            elif event.key == pygame.K_LEFT:
                head.direction = "left"
            elif event.key == pygame.K_RIGHT:
                head.direction = "right"

    # Content Update
    updateGame()

    # Engine Update
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
