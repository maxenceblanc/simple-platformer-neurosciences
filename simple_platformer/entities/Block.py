
# IMPORTS
import pygame

# FILE IMPORTS
import game_config as cfg

####################################################
###################| CLASSES |######################
####################################################

class Block:
    """block entity.

    INPUTS:
            x coordinate
            y coordinate
            type of the block (str)
    """

    def __init__(
        self, 
        block_x: float, 
        block_y: float, 
        type: str="default"
    ) -> None:

        # Applies coordinates and sizes.
        self.rect : pygame.Rect = pygame.Rect(block_x, block_y, cfg.BLOCK_WIDTH, cfg.BLOCK_HEIGHT)

        # Sets block attributes
        self.type : str = type

    def move(
        self, 
        distance_x: float, 
        distance_y: float
    ) -> None:
        """Moves the blocks relatively.

        INPUTS:
                distance in x
                distance in y
        """
        self.rect.x += int(round(distance_x,0))
        self.rect.y += int(round(distance_y,0))

####################################################
####################| PROGRAM |#####################
####################################################

if __name__ == "__main__":
    pass
