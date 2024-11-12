import pygame
from random import randint, choice

pygame.init()

screen = pygame.display.set_mode([500, 500])

# Get the clock
clock = pygame.time.Clock()

lanes = [93, 218, 343]

# GameObject class
class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.rect = self.surf.get_rect()
        self.rect.topleft = (x, y)

    def render(self, screen):
        screen.blit(self.surf, self.rect)

# Apple class
class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, 'apple.png')
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.rect.y += self.dy
        if self.rect.y > 500:
            self.reset()

    def reset(self):
        self.rect.x = choice(lanes)
        self.rect.y = -64

# Strawberry class
class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, 0, 'strawberry.png')
        self.dx = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.rect.x += self.dx
        if self.rect.x > 500:
            self.reset()

    def reset(self):
        self.rect.x = -64
        self.rect.y = choice(lanes)

# Player class
class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(0, 0, 'player.png')
        self.pos_x = 1
        self.pos_y = 1
        self.reset()

    def reset(self):
        self.rect.x = lanes[self.pos_x]
        self.rect.y = lanes[self.pos_y]
        self.update_dx_dy()

    def update_dx_dy(self):
        self.dx = lanes[self.pos_x]
        self.dy = lanes[self.pos_y]

    def left(self):
        if self.pos_x > 0:
            self.pos_x -= 1
            self.update_dx_dy()

    def right(self):
        if self.pos_x < len(lanes) - 1:
            self.pos_x += 1
            self.update_dx_dy()

    def up(self):
        if self.pos_y > 0:
            self.pos_y -= 1
            self.update_dx_dy()

    def down(self):
        if self.pos_y < len(lanes) - 1:
            self.pos_y += 1
            self.update_dx_dy()

    def move(self):
        self.rect.x -= (self.rect.x - self.dx) * 0.25
        self.rect.y -= (self.rect.y - self.dy) * 0.25

# Create an instance of Player
player = Player()
apple = Apple()
strawberry = Strawberry()

# Make a group
all_sprites = pygame.sprite.Group()
# Add sprites to group
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)

running = True
while running:
    # Looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()

    # Clear screen
    screen.fill((255, 255, 255))

    # Move and render Sprites
    for entity in all_sprites:
        entity.move()
        entity.render(screen)

    # Update the window
    pygame.display.flip()

    # tick the clock!
    clock.tick(60)

pygame.quit()
