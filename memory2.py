# Memory Version 2
# This is a  matching game that consists of a 4x4 matrix.
# User clicks on the tile and try to match 2 same tiles of two chooses tiles

import pygame
import random

# User-defined functions

def main():
    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window
    pygame.display.set_mode((520, 415))
    # set the title of the display window
    pygame.display.set_caption('Memory')   
    # get the display surface
    w_surface = pygame.display.get_surface() 
    # create a game object
    game = Game(w_surface)
    # start the main game loop by calling the play method on the game object
    game.play() 
    # quit pygame and clean up the pygame window
    pygame.quit() 


# User-defined classes

class Game:
    # An object in this class represents a complete game.

    def __init__(self, surface):
        # Initialize a Game.
        # - self is the Game to initialize
        # - surface is the display window surface object

        # === objects that are part of every game

        self.surface = surface
        self.bg_color = pygame.Color('black')
        self.timer_color = pygame.Color('white')
        
        # timing, frames and some inits for the game
        
        self.game_Clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True
        self.frame_counter = 0
        
        # === game specific objects
        self.board = []
        self.tiles = []
        self.create_board()
        self.timer()

        # state of the whole board and clicked point
        self.pos = [0, 0]

        self.tile_selected_flag = False
        self.time_pause = False

    def create_board(self):
        # create the board shown
        # - self is the game class
        # sets surfaceself of game
        Tile.set_surface(self.surface) 
        
        for image in range(1,9):
            self.tiles.append(pygame.image.load('image' + str(image) + '.bmp'))

        # amke it double then shuffle
        self.tiles = self.tiles+self.tiles
        # shuffle board
        random.shuffle(self.tiles)

    def play(self):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not.

        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_events()
            self.draw()
            # check to continue or not
            if self.continue_game:
                self.update()
                self.decide_continue()
            self.game_Clock.tick(60)

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.pos = pygame.mouse.get_pos()

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw
        
        self.surface.fill(self.bg_color) # clear the display surface first
        # Draw the tiles
        for each_row in self.board:
            for each_tile in each_row:
                each_tile.draw()
        
        # draws text
        self.timer()
        pygame.display.update() # make the updated surface appear on the display


    def update(self):
        # Update the game objects for the next frame.
        # - self is the Game to update

        
        counter = 0

        # create a tile class object
        for row_number in range(0, 4):
            row=list()
            
            for column_number in range(0, 4):
                tile = Tile(counter, row_number, column_number, self.tiles[counter])
                collision = tile.collision(self.pos, self.tile_selected_flag)

                # if collides with tile that has not been clicked
                if collision:
                    # change state is it is shown and log the index
                    tile.change_state(1)

               
                    self.pos = [0, 0]
                
                row.append(tile)
                counter += 1
                

            # append the list in the board list
            # (this will be like a 4x4 matrix)
            self.board.append(row)

        self.frame_counter = self.frame_counter + 1

    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check

        # if all cards flipped,
        # end the game 
        if not Tile.check_empty(self):
            self.continue_game = False
        else:
            self.continue_game = True

    def timer(self):
        # displays the text score
        # - self is the Game class
        # set font to 75 and if the game is still going, display time
        # else, do not change the time for the game has ended
        font = pygame.font.SysFont('', 75)
        
        if self.continue_game:
            self.time = str(pygame.time.get_ticks()//1000)


        # displays text box at the top, right hand side
        text_box = font.render(self.time, True, self.timer_color, self.bg_color)
        text_rect = text_box.get_rect() # get rect from textbox
        text_rect.right = self.surface.get_width()
        coordinate = text_rect

        # prints to surface
        self.surface.blit(text_box, coordinate)


class Tile:
    # An object in this class represents a Tile 

    # Shared Attributes or Class Attributes
    
    state = [0]*16 
    height = 103
    question = pygame.image.load('image0.bmp')
   

    # decorator with class attributes that sets surface
    @classmethod
    def set_surface(cls, game_surface):
        # Sets the surface of Tile
        # - cls is the class (i.e. Tile)
        # - game_surface is the surface to draw on

        cls.surface = game_surface

    # Instance Methods
    def __init__(self, index = 0, column_index = 0, row_index = 0, image = 0):
        # Initialize a Tile.
        # - self is the Tile to initialize

        self.x = Tile.height * column_index + 3
        self.y = Tile.height * row_index + 3
        self.current_state = index
        self.image = image

    def draw(self):
        # Draw the tile on the surface
        # - self is the Tile

        if Tile.state[self.current_state]:
            Tile.surface.blit(self.image, (self.x, self.y))
        else:
            Tile.surface.blit(Tile.question, (self.x, self.y))

    def change_state(self, new_state):
    
        # new_state is 1 for flipped or 0 for not flipped

        Tile.state[self.current_state] = new_state


    def collision(self, pos, flag):
        # collision is to test collision given compare_tile

        is_collided = pygame.Rect(self.x, self.y, Tile.height, Tile.height).collidepoint(pos[0], pos[1])

        collision_with_unknown = is_collided and not Tile.state[self.current_state]
        

     
        # return if it is collided and if it has not been click before
        if collision_with_unknown:
            return 1
        else:
            return 0
        


    def check_empty(self):
        # checks to see if all the tiles have been flipped
  
        if 0 in Tile.state:
            ref=True
        else:
            ref=False
        
        
        return ref

main()
