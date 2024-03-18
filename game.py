# Simple pygame program

# Import and initialize the pygame lib
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([800, 500])

# Run until the user asks to quit
running = True
while running:
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    
    # Flip the display
    pygame.display.flip()
    
# Done! Time to quit.
pygame.quit()

