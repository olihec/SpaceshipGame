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
        self.image = pygame.Surface([30, 30])
        
        self.rect = self.image.get_rect()        
        
        
        
        
        self.rect.x = 340
        self.rect.y = 240
        
        self.x_speed = 0
        self.y_speed = 0
    
    
    def change_y_speed(self, y):
        
        self.y_speed = y
        
    def change_x_speed(self, x):
        
        self.x_speed = x
    
        
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
        
class Block(pygame.sprite.Sprite):
    # This is the class for the block the player is trying to avoid
    
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(GREEN)
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
        
        if y_speed == 0:
            self.image = pygame.Surface([10, 4])
            self.image.fill(BLUE)
            self.rect = self.image.get_rect()
            
        if x_speed == 0:
            self.image = pygame.Surface([4, 10])
            self.image.fill(BLUE)
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
        self.lives = 3
        self.game_over = False
        self.score = 0
        self.time_s = 0
        self.time_m = 0
        self.player_alive_time = 0
        self.player_start = False
        
        # images
        self.player_image = pygame.image.load("playerShip1_blue.png").convert()
        self.player_image.set_colorkey(BLACK)
                                    
        
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
                if self.game_over:
                    self.__init__()            
            # What the player does when a key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.player.change_x_speed(-3)
                    self.player_start = True
                if event.key == pygame.K_d:
                    self.player.change_x_speed(3)
                    self.player_start = True
                if event.key == pygame.K_w:
                    self.player.change_y_speed(-3)
                    self.player_start = True
                if event.key == pygame.K_s:
                    self.player.change_y_speed(3)
                    self.player_start = True
                    
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
                    
                    self.bullet.rect.x = self.player.rect.x + 5
                    self.bullet.rect.y = self.player.rect.y + 8
                    self.player_start = True
                elif event.key == pygame.K_RIGHT:
                    self.bullet = Bullet(10, 0)
                    self.all_sprites_list.add(self.bullet)
                    self.bullet_list.add(self.bullet)  
                    
                    self.bullet.rect.x = self.player.rect.x + 5
                    self.bullet.rect.y = self.player.rect.y + 8                    
                    self.player_start = True
                elif event.key == pygame.K_UP:
                    self.bullet = Bullet(0, -10)
                    self.all_sprites_list.add(self.bullet)
                    self.bullet_list.add(self.bullet)  
                    
                    self.bullet.rect.x = self.player.rect.x + 8
                    self.bullet.rect.y = self.player.rect.y + 5                    
                    self.player_start = True
                elif event.key == pygame.K_DOWN:
                    self.bullet = Bullet(0, 10)
                    self.all_sprites_list.add(self.bullet)
                    self.bullet_list.add(self.bullet)  
                    
                    self.bullet.rect.x = self.player.rect.x + 8
                    self.bullet.rect.y = self.player.rect.y + 5                    
                    self.player_start = True
 
            
                                
 
        return False        
        
    def run_logic(self):
        # Checks every frame for collisions and updates positions
        self.time_s += 1/60
        if self.player_start == False:
            self.player_alive_time = 0
            
        self.player_alive_time += 1/60
        
        if math.floor(self.time_s) == 60:
            self.time_m += 1
            self.time_s = 0
                   
        
        
        if self.game_over == False:
            # Move all the sprites
            self.all_sprites_list.update() 
            if self.player_start == True:
                if self.player_alive_time > 3:
                    # check for collision between player and block
                
                    block_hit_player_list = pygame.sprite.spritecollide(self.player, self.block_list, True)
                
                    # check collision list            
                    for block in block_hit_player_list:
                        self.lives -= 1 
                        self.block= Block()
                        self.block_list.add(self.block)
                        self.all_sprites_list.add(self.block)                 
                        self.player.__init__()     
                        self.player_alive_time = 0
                        self.player_start = False
            if self.lives <= 0:
                self.game_over = True
                
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
        if self.game_over:
            screen.fill(WHITE)
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, click to restart", True, BLACK)
            center_x = round((SCREEN_WIDTH // 2) - (text.get_width() // 2))
            center_y = round((SCREEN_HEIGHT // 2) - (text.get_height() // 2))
            screen.blit(text, [center_x, center_y]) 
            
            font = pygame.font.SysFont("serif", 30)
            text = font.render("Final Score: " + str(self.score), True, BLACK)
            
            screen.blit(text, [center_x, center_y + 30])              
            
        if not self.game_over:
            # displays whats on the screen
            screen.fill(BLACK)
            background_image = pygame.image.load("saturn_family1.jpg").convert()
            screen.blit(background_image, [0, 0])
            
            
            self.all_sprites_list.draw(screen)
            
            
            screen.blit(self.player_image, [self.player.rect.x, self.player.rect.y])
            
            
            # font = pygame.font.Font("Serif", 25)
            font = pygame.font.SysFont("serif", 30)
            text = font.render("Lives: " + str(self.lives), True, RED)
            
            screen.blit(text, [600, 20])
            
            font = pygame.font.SysFont("serif", 30)
            text = font.render("Score: " + str(self.score), True, WHITE)
            
            screen.blit(text, [450, 20])            
             
            font = pygame.font.SysFont("serif", 30)
            text = font.render("Time: " + str(self.time_m) + "." + str(math.floor(self.time_s)), True, WHITE)
            
            screen.blit(text, [300, 20])            
        
        
        pygame.display.flip()
        

def main():
    # This is what we will run
    
    # Initialise pygame and set up window
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
        clock.tick(60)
 
    # Close window and exit
    pygame.quit()
 
# Call the main function, start up the game
if __name__ == "__main__":
    main()    
