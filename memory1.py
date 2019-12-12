# Memory Version 1
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
        
        
        # Check whether to continue game or not
        
        self.close_clicked = False
        self.continue_game = True
        self.frame_counter = 0
        
        # === game specific objects
        self.board = []
        self.tiles = []
        self.create_board()
        

       
    def create_board(self):
        # create the board shown
        # - self is the game class
        # sets surfaceself of game
        Tile.set_surface(self.surface) 
        

        self.tiles=[pygame.image.load('image1.bmp'),pygame.image.load('image2.bmp'),pygame.image.load('image3.bmp'),pygame.image.load('image4.bmp'),pygame.image.load('image5.bmp'),pygame.image.load('image6.bmp'),pygame.image.load('image7.bmp'),pygame.image.load('image8.bmp')]

        # making it double and shuffle
        self.tiles = self.tiles + self.tiles
        # shuffle board
        random.shuffle(self.tiles)

    def play(self):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not.

        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_events()
            self.draw()
           
            if self.continue_game:
                self.update()
                
            

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True
           

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw
        
        self.surface.fill(self.bg_color) # clear the display surface first
        # Draw the tiles
        for each_row in self.board:
            for each_tile in each_row:
                each_tile.draw()
        
        # draws text
       
        pygame.display.update() # make the updated surface appear on the display


    def update(self):
        # Update the game objects for the next frame.
        # - self is the Game to update

        # inits height and index
        
        counter = 0

        # Creating tile for each column and row
        for row_number in range(0, 4):
            row=list()
            
            for column_number in range(0, 4):
                tile = Tile(counter, row_number, column_number, self.tiles[counter])
                
                row.append(tile)
                counter += 1
                

            # append the list in the board list
            # (this will be like a 4x4 matrix)
            self.board.append(row)

        self.frame_counter = self.frame_counter + 1


class Tile:
    # An object in this class represents a Tile 
    # Shared Attributes or Class Attributes
       
    height = 103
    # decorator with class attributes that sets surface
    @classmethod
    def set_surface(cls, game_surface):
        # Sets the surface of Tile
        # - cls is the class (i.e. Tile)
        # - game_surface is the surface to draw on

        cls.surface = game_surface

    # Instance Methods
    def __init__(self, index = 0, col_index = 0, row_index = 0, image = 0):
        # Initialize a Tile.
        # - self is the Tile to initialize
        # - index is the index of tile
        # - col_index is the column number of tile
        # - row_index is the row number of tile
        # - image is a obj containing the image of tile

        self.x = Tile.height * col_index + 3
        self.y = Tile.height * row_index + 3
        

        self.image = image
    

    def draw(self):
        # Draw the tile on the surface
        # - self is the Tile

        
        Tile.surface.blit(self.image, (self.x, self.y))
       


    
main()