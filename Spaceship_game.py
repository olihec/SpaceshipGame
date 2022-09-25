# Import all our libraries

import pygame
import random
import math

# Set our constants

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# Classes 

class Player(pygame.sprite.Sprite):
    # This is the spaceship that the player controls
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([40, 30])
        
        self.rect = self.image.get_rect()        
        
        self.alive_time = 0
        self.start = False
        self.shield = True
        
        
        self.player_image = pygame.image.load("shieldUP.png").convert()
        self.player_image.set_colorkey(BLACK)        
        
        
        self.rect.x = 340
        self.rect.y = 240
        
        self.x_speed = 0
        self.y_speed = 0
    
        self.direction = ""
    def change_y_speed(self, y):
        
        self.y_speed = y
        if y < 0:
            self.change_direction("UP")
        elif y > 0:
            self.change_direction("DOWN")
        
    def change_x_speed(self, x):
        
        self.x_speed = x
        if x < 0:
            self.change_direction("LEFT")
        elif x > 0:
            self.change_direction("RIGHT")
       
        
    def change_direction(self, direction):
        self.start = True
        
        self.direction = direction
    def update(self):
        
        if self.rect.x > 0 and self.rect.x < 680:
            self.rect.x += self.x_speed
        elif self.rect.x > 679:
            self.rect.x += -3
        elif self.rect.x < 1:
            self.rect.x += 3
            
            
        if self.rect.y > 0 and self.rect.y < 480:
            self.rect.y += self.y_speed
        elif self.rect.y > 479:
            self.rect.y += -3
        elif self.rect.y < 1:
            self.rect.y += 3    
            
        
        if self.direction == "LEFT":
            self.image = pygame.Surface([40, 30])
            
            if self.shield == True:
                self.player_image = pygame.image.load("shieldLEFT.png").convert()
                self.player_image.set_colorkey(BLACK)
            else:
                self.player_image = pygame.image.load("playerShip1_blueLEFT.png").convert()
                self.player_image.set_colorkey(BLACK)            
        
        elif self.direction == "RIGHT":
            self.image = pygame.Surface([40, 30])
            
            if self.shield == True:
                self.player_image = pygame.image.load("shieldRIGHT.png").convert()
                self.player_image.set_colorkey(BLACK)
            else:                    
                self.player_image = pygame.image.load("playerShip1_blueRIGHT.png").convert()
                self.player_image.set_colorkey(BLACK)
                
        elif self.direction == "UP":
            self.image = pygame.Surface([30, 40])
            
            if self.shield == True:
                self.player_image = pygame.image.load("shieldUP.png").convert()
                self.player_image.set_colorkey(BLACK)
            else:                    
                self.player_image = pygame.image.load("playerShip1_blueUP.png").convert()
                self.player_image.set_colorkey(BLACK)            
        
        elif self.direction == "DOWN":
            self.image = pygame.Surface([30, 40])
            
            if self.shield == True:
                self.player_image = pygame.image.load("shieldDOWN.png").convert()
                self.player_image.set_colorkey(BLACK)
            else:                    
                self.player_image = pygame.image.load("playerShip1_blueDOWN.png").convert()
                self.player_image.set_colorkey(BLACK)            
    
class Block(pygame.sprite.Sprite):
    # This is the class for the block the player is trying to avoid
    
    def __init__(self):
        super().__init__()
        x = random.randrange(0,3)
        if x == 0:
            self.image = pygame.Surface([28, 28])
            self.block_image = pygame.image.load("meteorBrown_small1.png").convert()
            self.block_image.set_colorkey(BLACK)
        elif x == 1:
            self.image = pygame.Surface([29, 26])
            self.block_image = pygame.image.load("meteorBrown_small2.png").convert()
            self.block_image.set_colorkey(BLACK)
        elif x == 2:
            self.image = pygame.Surface([18, 18])
            self.block_image = pygame.image.load("meteorBrown_tiny1.png").convert()
            self.block_image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = -100
        # The "center" the sprite will orbit
        self.center_x = random.randrange(SCREEN_WIDTH)
        self.center_y = random.randrange(SCREEN_HEIGHT)
 
        # Current angle in radians
        self.angle = random.random() * 2 * math.pi
 
        # How far away from the center to orbit, in pixels
        

        self.radius = random.randrange(10, 200)
 
        # How fast to orbit, in radians per frame
        self.speed = 0.02      
        
    def update(self):
        """ Update the ball's position. """
        # Calculate a new x, y
        self.rect.x = round(self.radius * math.sin(self.angle) + self.center_x)
        self.rect.y = round(self.radius * math.cos(self.angle) + self.center_y)
 
        # Increase the angle in prep for the next round.
        self.angle += self.speed        
         
class Bullet(pygame.sprite.Sprite):
    # These are the bullets that the player will fire
       
    def __init__(self, x_speed, y_speed):
        super().__init__()
        
        if x_speed < 0:
            self.image = pygame.Surface([17, 4])
            
            self.bullet_image = pygame.image.load("laserBlue16LEFT.png").convert()
            self.bullet_image.set_colorkey(BLACK)            
            self.rect = self.image.get_rect()
            
        elif x_speed > 0:
            self.image = pygame.Surface([17, 4])
            
            self.bullet_image = pygame.image.load("laserBlue16RIGHT.png").convert()
            self.bullet_image.set_colorkey(BLACK)             
            self.rect = self.image.get_rect()        
            
        elif y_speed < 0:
            self.image = pygame.Surface([4, 17])
            
            self.bullet_image = pygame.image.load("laserBlue16UP.png").convert()
            self.bullet_image.set_colorkey(BLACK)             
            self.rect = self.image.get_rect()
        
        elif y_speed > 0:
            self.image = pygame.Surface([4, 17])
            
            self.bullet_image = pygame.image.load("laserBlue16DOWN.png").convert()
            self.bullet_image.set_colorkey(BLACK)             
            self.rect = self.image.get_rect()        
            
        self.x_speed = x_speed
        self.y_speed = y_speed        
        
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

class Game(object):
    """ This is our game class which we will create a new instance of in order
        to restart the game """
    def __init__(self):
        # Our constructor (where we create instances of our starting sprites)
        # game variables
        self.start_screen = True
        self.lives = 3
    
        self.score = 0
        self.time_s = 0
        self.time_m = 0
    
                                
    
        # Create our sprite lists
        self.all_sprites_list = pygame.sprite.Group()
        self.block_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()        
        
            
        
        # Create instances of our sprites
        self.player = Player()
        self.all_sprites_list.add(self.player)
    
        for i in range(25):
            # This represents a block
            self.block = Block()
     
        
            # Add the block to the list of objects
            self.block_list.add(self.block)
            self.all_sprites_list.add(self.block)        
        
    def process_events(self):
        # Process our game events such as button presses
        
        """ Process all of the events. Return a "True" if we need
                    to close the window. """
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_screen:
                    self.start_screen = False
                    pygame.mouse.set_visible(False)
            # What the player does when a key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.player.change_x_speed(-3)
                    self.player.start = True
                    
                if event.key == pygame.K_d:
                    self.player.change_x_speed(3)
                    self.player.start = True
                    
                if event.key == pygame.K_w:
                    self.player.change_y_speed(-3)
                    self.player.start = True
                    
                if event.key == pygame.K_s:
                    self.player.change_y_speed(3)
                    self.player.start = True
                    
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.player.change_x_speed(0)
                if event.key == pygame.K_d:
                    self.player.change_x_speed(0)
                if event.key == pygame.K_w:
                    self.player.change_y_speed(0)
                if event.key == pygame.K_s:
                    self.player.change_y_speed(0)  
                    
            # What happen when a arrow is pressed to fire bullet
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.bullet = Bullet(-10, 0)
                    self.all_sprites_list.add(self.bullet)
                    self.bullet_list.add(self.bullet)  
                    
                    self.bullet.rect.x = self.player.rect.x + 6
                    self.bullet.rect.y = self.player.rect.y + 18
                    self.player.start = True
                                       
                    self.player.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    self.bullet = Bullet(10, 0)
                    self.all_sprites_list.add(self.bullet)
                    self.bullet_list.add(self.bullet)  
                    
                    self.bullet.rect.x = self.player.rect.x + 6
                    self.bullet.rect.y = self.player.rect.y + 18                  
                    self.player.start = True
                    
                                        
                    self.player.change_direction("RIGHT")
                elif event.key == pygame.K_UP:
                    self.bullet = Bullet(0, -10)
                    self.all_sprites_list.add(self.bullet)
                    self.bullet_list.add(self.bullet)  
                    
                    self.bullet.rect.x = self.player.rect.x + 18
                    self.bullet.rect.y = self.player.rect.y + 6                    
                    self.player.start = True
                                      
                    self.player.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    self.bullet = Bullet(0, 10)
                    self.all_sprites_list.add(self.bullet)
                    self.bullet_list.add(self.bullet)  
                    
                    self.bullet.rect.x = self.player.rect.x + 18
                    self.bullet.rect.y = self.player.rect.y + 6                    
                    self.player.start = True
                                      
                    self.player.change_direction("DOWN")
 
            
                                
 
        return False        
        
    def run_logic(self):
        # Checks every frame for collisions and updates positions
        
                   
        if self.start_screen == False:
            self.time_s += 1/60
            if self.player.start == False:
                self.player.alive_time = 0
            
            self.player.alive_time += 1/60
            
            if math.floor(self.time_s) == 60:
                self.time_m += 1
                self.time_s = 0            
            # Move all the sprites
            self.all_sprites_list.update() 
            if self.player.start == True:
                if self.player.alive_time > 3:
                    self.player.shield = False
                    # check for collision between player and block
                
                    block_hit_player_list = pygame.sprite.spritecollide(self.player, self.block_list, True)
                
                    # check collision list            
                    for block in block_hit_player_list:
                        self.lives -= 1 
                        self.block= Block()
                        self.block_list.add(self.block)
                        self.all_sprites_list.add(self.block)                 
                        self.player.__init__()     
                        self.player.alive_time = 0
                        self.player.start = False
                        self.player.shield = True
                        self.player.player_image = pygame.image.load("shieldUP.png").convert()
                        self.player.player_image.set_colorkey(BLACK)                        
            if self.lives <= 0:
                self.start_screen = True
                
            # chech for collision between bullet and block
            for self.bullet in self.bullet_list:
                block_hit_bullet_list = pygame.sprite.spritecollide(self.bullet, self.block_list, True)
                for block in block_hit_bullet_list:
                    self.block = Block()
                    self.block_list.add(self.block)
                    self.all_sprites_list.add(self.block)                     
                    self.bullet_list.remove(self.bullet)
                    self.all_sprites_list.remove(self.bullet) 
                    self.score += 100
                if self.bullet.rect.x < -10 or self.bullet.rect.x > 700 or self.bullet.rect.y < -10 or self.bullet.rect.y > 500:
                    self.bullet_list.remove(self.bullet)
                    self.all_sprites_list.remove(self.bullet)                    
                   
                    
    def display_frame(self, screen):
        if self.start_screen:
            background_image = pygame.image.load("start_page.png").convert()
            screen.blit(background_image, [0, 0])                        
            
        if not self.start_screen:
            # displays whats on the screen
            screen.fill(BLACK)
            background_image = pygame.image.load("saturn_family1.jpg").convert()
            screen.blit(background_image, [0, 0])
            
            
            self.all_sprites_list.draw(screen)
            
            if self.player.shield == False:
                screen.blit(self.player.player_image, [self.player.rect.x, self.player.rect.y])
            else:
                screen.blit(self.player.player_image, [self.player.rect.x - 18, self.player.rect.y - 34])
            
            for self.block in self.block_list:
                screen.blit(self.block.block_image, [self.block.rect.x, self.block.rect.y])
                
            for self.bullet in self.bullet_list:
                screen.blit(self.bullet.bullet_image, [self.bullet.rect.x, self.bullet.rect.y])            
        
            # font = pygame.font.Font("Serif", 25)
            font = pygame.font.SysFont("serif", 30)
            text = font.render("Lives: " + str(self.lives), True, RED)
            
            screen.blit(text, [600, 20])
            
            font = pygame.font.SysFont("serif", 30)
            text = font.render("Score: " + str(self.score), True, WHITE)
            
            screen.blit(text, [450, 20])            
             
            font = pygame.font.SysFont("serif", 30)
            text = font.render( str(self.time_m) + "m:" + str(math.floor(self.time_s)) + "sec", True, WHITE)
            
            screen.blit(text, [300, 20])            
        
        
        pygame.display.flip()
        

def main():
    # This is what we will run
    
    # Initialise pygame and set up window
    pygame.init()
    
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
     
    pygame.display.set_caption("My Game")
        
    
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
        clock.tick(60)
 
    # Close window and exit
    pygame.quit()
 
# Call the main function, start up the game
if __name__ == "__main__":
    main()    
