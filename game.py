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

# Create an instance of Apple
apple = Apple()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

    # Fill the screen with a white background
    screen.fill((255, 255, 255))

    # Draw apple
    apple.move()
    apple.render(screen)

    # Update the window
    pygame.display.flip()

    # Tick the clock!
    clock.tick(60)
