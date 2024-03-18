# Simple pygame program

# Import and initialize the pygame lib
import pygame
from settings import Settings

def run_game():
    pygame.init()
    gm_settings = Settings()

    # Set up the drawing window
    screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
    pygame.display.set_caption(gm_settings.caption)


    # Run until the user asks to quit
    running = True
    while running:
        screen.fill(gm_settings.bg_color)
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
    
        # Flip the display
        pygame.display.flip()
    
    # Done! Time to quit.
    pygame.quit()

run_game()