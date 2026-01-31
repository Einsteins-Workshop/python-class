import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
SKY_BLUE = (107, 140, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
YELLOW = (255, 215, 0)
ORANGE = (255, 165, 0)

# Game variables
gravity = 0.8
scroll = 0
game_over = 0
score = 0


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0

        # Create 8-bit Mario sprite
        self.image = self.create_mario_sprite()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = 32
        self.height = 32
        self.vel_y = 0
        self.jumped = False
        self.direction = 1
        self.in_air = True

    def create_mario_sprite(self):
        # Create a 32x32 surface for Mario
        sprite = pygame.Surface((32, 32))
        sprite.set_colorkey(BLACK)
        sprite.fill(BLACK)

        # Define colors
        skin = (255, 206, 180)
        red = (255, 0, 0)
        blue = (0, 0, 255)
        brown = (139, 69, 19)

        # 8-bit Mario pixel art (simplified)
        # Hat (red)
        for x in range(8, 24):
            sprite.set_at((x, 4), red)
        for x in range(4, 28):
            sprite.set_at((x, 8), red)

        # Face (skin)
        for x in range(8, 24):
            sprite.set_at((x, 12), skin)
        for x in range(4, 28):
            sprite.set_at((x, 16), skin)

        # Eyes
        sprite.set_at((12, 12), BLACK)
        sprite.set_at((20, 12), BLACK)

        # Mustache
        for x in range(8, 24):
            sprite.set_at((x, 18), brown)

        # Body (red shirt)
        for x in range(8, 24):
            sprite.set_at((x, 20), red)
            sprite.set_at((x, 24), red)

        # Overalls (blue)
        sprite.set_at((8, 22), blue)
        sprite.set_at((12, 22), blue)
        sprite.set_at((20, 22), blue)
        sprite.set_at((24, 22), blue)

        # Legs (blue)
        for y in range(26, 30):
            sprite.set_at((10, y), blue)
            sprite.set_at((22, y), blue)

        # Shoes (brown)
        for x in range(8, 14):
            sprite.set_at((x, 30), brown)
        for x in range(20, 26):
            sprite.set_at((x, 30), brown)

        return sprite

    def update(self, game_over):
        dx = 0
        dy = 0
        walk_cooldown = 5

        if game_over == 0:
            # Get key presses
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and not self.jumped and not self.in_air:
                self.vel_y = -15
                self.jumped = True
            if not key[pygame.K_SPACE]:
                self.jumped = False
            if key[pygame.K_LEFT]:
                dx -= 5
                self.direction = -1
            if key[pygame.K_RIGHT]:
                dx += 5
                self.direction = 1

            # Add gravity
            self.vel_y += gravity
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            # Check collision with platforms
            self.in_air = True
            for platform in platform_group:
                # Collision in x direction
                if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                # Collision in y direction
                if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # Check if below platform (jumping)
                    if self.vel_y < 0:
                        dy = platform.rect.bottom - self.rect.top
                        self.vel_y = 0
                    # Check if above platform (falling)
                    elif self.vel_y >= 0:
                        dy = platform.rect.top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            # Check collision with enemies
            if pygame.sprite.spritecollide(self, enemy_group, False):
                game_over = -1

            # Check collision with coins
            coin_collected = pygame.sprite.spritecollide(self, coin_group, True)
            if coin_collected:
                global score
                score += len(coin_collected) *10

            # Update player position
            self.rect.x += dx
            self.rect.y += dy

            if self.rect.left<0:
                self.rect.left = 0

            if self.rect.right>SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

        elif game_over == -1:
            self.image.fill((WHITE))

        # Draw player
        screen.blit(self.image, self.rect)

        return game_over


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        screen.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction * 2
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1

        screen.blit(self.image, self.rect)


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        screen.blit(self.image, self.rect)


# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Super Mario Bros - Pygame')

# Create clock
clock = pygame.time.Clock()

# Create sprite groups
platform_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()


# Create level
def create_level():
    # Ground platforms
    platform = Platform(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50)
    platform_group.add(platform)

    # Floating platforms
    platform = Platform(200, 450, 150, 20)
    platform_group.add(platform)

    platform = Platform(230, 350, 100, 20)
    platform_group.add(platform)

    platform = Platform(100, 300, 100, 20)
    platform_group.add(platform)

    platform = Platform(600, 400, 150, 20)
    platform_group.add(platform)

    platform = Platform(350, 200, 100, 20)
    platform_group.add(platform)

    # Enemies
    enemy = Enemy(250, 420)
    enemy_group.add(enemy)

    enemy = Enemy(600, 370)
    enemy_group.add(enemy)

    # Coins
    coin = Coin(220, 400)
    coin_group.add(coin)

    coin = Coin(260, 400)
    coin_group.add(coin)

    coin = Coin(470, 300)
    coin_group.add(coin)

    coin = Coin(370, 150)
    coin_group.add(coin)

    coin = Coin(620, 350)
    coin_group.add(coin)

    coin = Coin(660, 350)
    coin_group.add(coin)

    coin = Coin(300, 350)
    coin_group.add(coin)

    coin = Coin(250, 350)
    coin_group.add(coin)

    coin = Coin(500, 350)
    coin_group.add(coin)

    coin = Coin(400, 350)
    coin_group.add(coin)

# Create player
player = Player(100, SCREEN_HEIGHT - 130)

# Create level
create_level()

# Font for score
font = pygame.font.Font(None, 36)

# Game loop
run = True
while run:
    clock.tick(FPS)

    # Draw background
    screen.fill(SKY_BLUE)

    # Update and draw sprites
    platform_group.update()
    enemy_group.update()
    coin_group.update()

    # Update player
    game_over = player.update(game_over)

    # Draw score
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

    # Game over text
    if game_over == -1:
        game_over_text = font.render('GAME OVER! Press R to Restart', True, RED)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_over_text, text_rect)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over == -1:
                # Restart game
                game_over = 0
                score = 0
                player.rect.x = 100
                player.rect.y = SCREEN_HEIGHT - 130
                player.vel_y = 0
                player.image=player.create_mario_sprite()

                # Clear and recreate level
                platform_group.empty()
                enemy_group.empty()
                coin_group.empty()
                create_level()

    pygame.display.update()

pygame.quit()
sys.exit()