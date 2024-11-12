import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode([500, 500])

# Game Object
class GameObject(pygame.sprite.Sprite):
  # Remove width and height and add image here!
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    # self.surf = pygame.Surface((width, height)) REMOVE!
    # self.surf.fill((255, 0, 255)) REMOVE!
    self.surf = pygame.image.load(image) # ADD!
    self.x = x
    self.y = y

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))  

# Make an instance of GameObject
# box = GameObject(120, 300, 50, 50) REMOVE!
apple = GameObject(120, 300, 'apple.png') # ADD!

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

    # Fill the screen with a white background
    screen.fill((255, 255, 255))

    # box.render(screen) REMOVE!
    apple.render(screen) # ADD!

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
