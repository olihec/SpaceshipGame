import pygame
import random
 
# --- Global constants ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE =(0,100,255)
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
 
# --- Classes ---
class Train(pygame.sprite.Sprite):
    #This is the train
    def __init__(self):
        
        super().__init__()
        self.image = pygame.Surface([30, 20])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        
    
    def update(self):
    
        self.rect.x = self.rect.x + 5
    
        
    
        
        
class Sky(pygame.sprite.Sprite):
    #This is our sky
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 500])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
    
 
class Platform(pygame.sprite.Sprite):
    """ This class represents th e two platrorms the train/ car has to get from and to """
 
    def __init__(self):
        """ Constructor, create the image of the platforms. """
        super().__init__()
        self.image = pygame.Surface([50, 250])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
 
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the tool the player draws with. """
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Update the player location. """
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
 
 
class Game(object):
    """ This class represents an instance of the game. If we need to
        reset the game we'd just need to create a new instance of this
        class. """
 
    def __init__(self):
        """ Constructor. Create all our attributes and initialize
        the game. """
 
        self.score = 0
        self.game_over = False
 
        # Create sprite lists
        self.sky_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.train_list = pygame.sprite.Group()

        # Create all sky sprites
        for i in range(140):
            for j in range(100):
                sky = Sky()
                sky.rect.x = i * 5
                sky.rect.y = - j * 5
                
                self.sky_list.add(sky)
                self.all_sprites_list.add(sky)
        
        # Create the platform sprites
        for i in range(2):
            platform = Platform()
            if i == 1:
                platform.rect.x = 0
            else:
                platform.rect.x = 650

            platform.rect.y = 250
 
            self.platform_list.add(platform)
            self.all_sprites_list.add(platform)
 
        # Create the player
        self.player = Player()
        self.all_sprites_list.add(self.player)

        # Creat train

        train = Train()
        
        self.train_list.add(train)
        train.rect.x = 10
        train.rect.y = 230
        
 
    def process_events(self):
        """ Process all of the events. Return a "True" if we need
            to close the window. """
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_SPACE]:
                    
                self.train_list.update()
                    
                    
        if pygame.mouse.get_pressed()[0]:               
            pygame.sprite.spritecollide(self.player, self.sky_list, True)

                    
 
        return False
 
    def run_logic(self):
        """
        This method is run each time through the frame. It
        updates positions and checks for collisions.
        """
        if not self.game_over:
            # Move all the sprites
            self.all_sprites_list.update()
            
            
 
            # See if the player block has collided with anything.
                       
 
    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        screen.fill(RED)
 
        if self.game_over:
            # font = pygame.font.Font("Serif", 25)
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, click to restart", True, BLACK)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
 
        if not self.game_over:
            self.all_sprites_list.draw(screen)
            self.train_list.draw(screen)
        pygame.display.flip()
 
 
def main():
    """ Main program function. """
    # Initialize Pygame and set up the window
    pygame.init()
 
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("My Game")
    pygame.mouse.set_visible(False)
 
    # Create our objects and set the data
    done = False
    clock = pygame.time.Clock()
 
    # Create an instance of the Game class
    game = Game()
    
    # Main game loop
    while not done:
 
        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()
        
        # Update object positions, check for collisions
        game.run_logic()
 
        # Draw the current frame
        game.display_frame(screen)
 
        # Pause for the next frame
        clock.tick(120)
 
    # Close window and exit
    pygame.quit()
 
# Call the main function, start up the game
if __name__ == "__main__":
    main()
