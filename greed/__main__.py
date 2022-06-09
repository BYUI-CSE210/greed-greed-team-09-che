import random

from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.artifact import Artifact

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 25
FONT_SIZE = 25
COLS = 60
ROWS = 40
CAPTION = "Greed Game"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 75
GEM_ROCK = ["*", "o", "+", "#"]
GEM_ROCK_VELOCITY = Point(0, 5)


def main():

    # create the cast
    cast = Cast()

    # create the banner
    banner = Actor()
    banner.set_text("The Score")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    #create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y - 35)
    position = Point(x, y)

    player = Actor()
    player.set_color(WHITE)
    player.set_position(position)
    player.set_font_size(FONT_SIZE)
    player.set_text("@")
    cast.add_actor("players", player)

    #create the artifacts (gems and rocks)
    for n in range(DEFAULT_ARTIFACTS):
        text = random.choice(GEM_ROCK)

        x = random.randint(1, COLS - 1)
        y = random.randint(1, 15)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        gem_rock = Artifact()
        gem_rock.set_text(text)
        gem_rock.set_font_size(FONT_SIZE)
        gem_rock.set_color(color)
        gem_rock.set_position(position)
        gem_rock.set_velocity(GEM_ROCK_VELOCITY)
        cast.add_actor("gems_rocks", gem_rock)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
