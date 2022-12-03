import pygame
from game import Game

#defining screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

def main():
    # Initialize all imported pygame modules
    pygame.init()
    
    # Set the width and height of the screen [width, height]
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    # Set the current window caption
    pygame.display.set_caption("Pacman Project")
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # Create a game object
    game = Game()
    # -------- Main Program Loop -----------
    while not done:
        # --- Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()
        # --- Game logic should go here
        game.run_logic()
        # --- Draw the current frame
        game.display_frame(screen)
        # --- Limit to 30 frames per second
        clock.tick(30)
        #tkMessageBox.showinfo("GAME OVER!","Final Score = "+(str)(GAME.score))
    # Close the window and quit.
    pygame.quit()

if __name__ == '__main__':
    main()
