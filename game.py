import pygame
from random import randint

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode([500, 500])

# Get the clock
clock = pygame.time.Clock()

# Create the GameObject class
class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.rect = self.surf.get_rect()
        self.rect.topleft = (x, y)

    def render(self, screen):
        screen.blit(self.surf, self.rect)

# Create an Apple class
class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, 'apple.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()  # call reset here!

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        # Check the y position of the apple
        if self.rect.y > 500:
            self.reset()

    # add a new method
    def reset(self):
        self.rect.x = randint(50, 400)
        self.rect.y = -64

# Create a Player class
class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(0, 0, 'player.png')
        self.dx = self.rect.x  # Starting x position
        self.dy = self.rect.y  # Starting y position
        self.speed = 5         # Speed of movement
        self.reset()

    def left(self):
        self.dx -= self.speed

    def right(self):
        self.dx += self.speed

    def up(self):
        self.dy -= self.speed

    def down(self):
        self.dy += self.speed

    def move(self):
        # Use the easing formula to smoothly move towards the target (dx, dy)
        self.rect.x -= (self.rect.x - self.dx) * 0.25
        self.rect.y -= (self.rect.y - self.dy) * 0.25

    def reset(self):
        self.rect.x = 250 - 32
        self.rect.y = 250 - 32

# Create an instance of Player
player = Player()

# Create an instance of Apple
apple = Apple()

# Game loop
running = True
while running:
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

    # Fill the screen with a white background
    screen.fill((255, 255, 255))

    # Draw apple
    apple.move()
    apple.render(screen)

    # Draw player 
    player.move()
    player.render(screen)

    # Update the window
    pygame.display.flip()

    # Tick the clock!
    clock.tick(60)