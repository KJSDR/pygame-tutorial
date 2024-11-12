# Import and initialize pygame
import pygame
pygame.init()
# Configure the screen
screen = pygame.display.set_mode([500, 500])

circle_color = (50, 50, 50)
# Creat the game loop
running = True
while running:
    # Looks at events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Clear the screen
    screen.fill((255, 255, 255))
    # Draw a circle
    circle_positions = [
        (100, 100),
        (400, 100),
        (250, 250),
        (100, 400),
        (400, 400)
    ]
    circle_colors = [
        (255, 25, 0),   
        (255, 153, 0),  
        (255, 247, 0),  
        (0, 255, 4),
        (17, 0, 255) 
    ]

    for i, position in enumerate(circle_positions):
        pygame.draw.circle(screen, circle_colors[i], position, 30)
    # Update the display
    pygame.display.flip()


