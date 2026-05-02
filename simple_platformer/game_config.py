
import pygame as pg

import levels.levels as levels


################################
###### GAME CONFIGURATION ######
################################

RANDOM_GEN : bool = False  # Toggles random generation
CAN_LOSE : bool = False  # False: Disables losing, for dev/testing purposes

# "play"  "dev"  "debug"  "tas"
APP_MODE : str = "dev"  # Not used yet

FPS : int = 20


MAP_NAME : str = levels.NAME

# Coefficient of Proportions (to increase physics proportionally)
PROPORTION : float = 1

# Size of blocks
BLOCK_WIDTH : float = 16 * PROPORTION
BLOCK_HEIGHT : float = 16 * PROPORTION

# For the display
VISIBILITY_X : float = 45  # Width of WINDOW in amount of blocks.
VISIBILITY_Y : float = 2  # Height of WINDOW in amount of chunk height.
SIZE_X : float = BLOCK_WIDTH * VISIBILITY_X  # Width of WINDOW in pixels.
SIZE_Y : float = (
    levels.CHUNK_HEIGHT * BLOCK_HEIGHT * VISIBILITY_Y
)  # Height of WINDOW in pixels.

# Player size
PLAYER_WIDTH : float = 1 * BLOCK_WIDTH
PLAYER_HEIGHT : float = 2 * BLOCK_HEIGHT

# Start
START_X : float = 0
START_Y : float = SIZE_Y - BLOCK_HEIGHT - PLAYER_HEIGHT

# Colours
WHITE : tuple[int, int, int] = (255, 255, 255)
GREY : tuple[int, int, int] = (30, 30, 30)
ORANGE : tuple[int, int, int] = (255, 125, 0)
RED : tuple[int, int, int] = (255, 0, 0)

# Acceleration
ACCELERATION_X : float = 1 * PROPORTION
ACCELERATION_Y : float = 1.67 * PROPORTION  # 1.67
COEFF_ACCELERATION_X : float = 1.3
SLOWDOWN__X : float = COEFF_ACCELERATION_X * ACCELERATION_X
# Speed
SPEED_X : float = 16 * PROPORTION  # speed_x max
SPEED_Y : float = BLOCK_HEIGHT * (14 / 16)  # speed_y max
# Camera speed
SPEED_CAMERA_X : float = 80 * PROPORTION
# SPEED_CAMERA_Y = 5 * PROPORTION


# Keys
KEY_RIGHT = pg.K_d
KEY_LEFT = pg.K_q
KEY_UP = pg.K_z

KEY_RECORD = pg.K_o
KEY_LOAD = pg.K_p

KEY_RESTART = pg.K_SPACE
KEY_CUSTOM = pg.K_n

# Camera keys
CAMERA_RIGHT = pg.K_RIGHT
CAMERA_LEFT = pg.K_LEFT
