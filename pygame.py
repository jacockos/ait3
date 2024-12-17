import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

class Tank:
    def __init__(self, x, y, color, controls):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 2
        self.color = color
        self.hp = 5
        self.shield = 0
        self.cooldown = 0
        self.controls = controls

    def draw(self):
        # Draw the tank body
        tank_rect = pygame.Rect(0, 0, 40, 60)
        tank_rect.center = (self.x, self.y)
        rotated_tank = pygame.transform.rotate(pygame.Surface((40, 60), pygame.SRCALPHA), -math.degrees(self.angle))
        pygame.draw.rect(rotated_tank, self.color, tank_rect)
        screen.blit(rotated_tank, rotated_tank.get_rect(center=(self.x, self.y)))

        # Draw the cannon
        cannon_x = self.x + math.cos(self.angle) * 30
        cannon_y = self.y + math.sin(self.angle) * 30
        pygame.draw.line(screen, BLACK, (self.x, self.y), (cannon_x, cannon_y), 5)

        # Draw the shield
        if self.shield > 0:
            pygame.draw.circle(screen, BLUE, (int(self.x), int(self.y)), 35, 3)

    def move(self, keys):
        if keys[self.controls['forward']]:
            self.x += math.cos(self.angle) * self.speed
            self.y += math.sin(self.angle) * self.speed
        if keys[self.controls['backward']]:
            self.x -= math.cos(self.angle) * self.speed
            self.y -= math.sin(self.angle) * self.speed
        if keys[self.controls['left']]:
            self.angle -= 0.05
        if keys[self.controls['right']]:
            self.angle += 0.05

    def shoot(self, bullets):
        if self.cooldown == 0:
            bullets.append(Bullet(self.x, self.y, self.angle))
            self.cooldown = 30 if self.shield == 0 else 15

class Bullet:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 5

    def draw(self):
        pygame.draw.circle(screen, YELLOW, (int(self.x), int(self.y)), 5)

    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

class Obstacle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        pygame.draw.rect(screen, GRAY, self.rect)

class Ability:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.radius = 15

    def draw(self):
        color = BLUE if self.type == 'shield' else RED
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)

# Initialize players
player1 = Tank(200, 300, BLUE, {
    'forward': pygame.K_w,
    'backward': pygame.K_s,
    'left': pygame.K_a,
    'right': pygame.K_d,
    'shoot': pygame.K_SPACE
})

player2 = Tank(600, 300, RED, {
    'forward': pygame.K_UP,
    'backward': pygame.K_DOWN,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'shoot': pygame.K_RETURN
})

bullets1 = []
bullets2 = []
obstacles = [
    Obstacle(300, 200, 100, 100),
    Obstacle(500, 400, 150, 50)
]
abilities = [
    Ability(400, 400, 'shield'),
    Ability(100, 100, 'fasterShoot')
]

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Update players
    player1.move(keys)
    player2.move(keys)

    # Shooting
    if keys[player1.controls['shoot']]:
        player1.shoot(bullets1)
    if keys[player2.controls['shoot']]:
        player2.shoot(bullets2)

    # Draw bullets
    for bullet in bullets1 + bullets2:
        bullet.move()
        bullet.draw()

    # Draw obstacles and abilities
    for obstacle in obstacles:
        obstacle.draw()
    for ability in abilities:
        ability.draw()

    # Update screen
    player1.draw()
    player2.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
