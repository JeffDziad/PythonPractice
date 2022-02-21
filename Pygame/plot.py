import pygame

GAME_HEIGHT = 500
GAME_WIDTH = 500
TILE_SIZE = 25
COLS = int(GAME_WIDTH / TILE_SIZE)
ROWS = int(GAME_HEIGHT / TILE_SIZE)

pygame.init()

screen = pygame.display.set_mode([GAME_HEIGHT, GAME_WIDTH])

pygame.display.set_caption('Python Snake')

clock = pygame.time.Clock()
speed = 5
running = True


# Objects
# Head
class SnakeHead:
    def __init__(self, start_x, start_y, direction="right"):
        self.alive = True

        self.rect = pygame.Rect(start_x, start_y, TILE_SIZE, TILE_SIZE)
        self.direction = direction

    def draw(self):
        pygame.draw.rect(screen, "blue", self.rect)

    def update(self):
        if self.alive:
            d = self.direction
            x, y = 0, 0
            if d == "up":
                x = self.rect.x
                y = self.rect.y - TILE_SIZE
            elif d == "down":
                x = self.rect.x
                y = self.rect.y + TILE_SIZE
            elif d == "left":
                x = self.rect.x - TILE_SIZE
                y = self.rect.y
            elif d == "right":
                x = self.rect.x + TILE_SIZE
                y = self.rect.y

            if x + TILE_SIZE > GAME_WIDTH:
                self.alive = False
                x -= TILE_SIZE
            elif x < 0:
                self.alive = False
            elif y + TILE_SIZE > GAME_HEIGHT:
                y -= TILE_SIZE
                self.alive = False
            elif y < 0:
                self.alive = False

            self.rect.update((x, y), (TILE_SIZE, TILE_SIZE))
        self.draw()


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


head = SnakeHead(int((COLS / 2) * TILE_SIZE), int((ROWS / 2) * TILE_SIZE))


def updateGame():
    screen.fill((255, 255, 255))
    drawGrid()
    head.update()


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
