"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/inheritance/materials/greed-specification.html
"""


from game.shared.point import Point


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = 0

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.

        Args:
            cast (Cast): The cast of actors.
        """
        
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity) 

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.

        Args:
            cast (Cast): The cast of actors.
        """

        #get the robot (actor) object
        robot = cast.get_first_actor("robots")
        #get the max_width and max_height of the screen
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        #get the banner object (actor)
        banner = cast.get_first_actor("banners")
        #get the artifacts into a list
        gems_rocks = cast.get_actors("artifacts")

        #with every update / update the y axis of the artifacts
        for n in gems_rocks:
            n.move_next(max_x, max_y)

            #if the artifact's position is the same as the robot
            #update the score
            if robot.get_position().equals(n.get_position()):
                    if n.get_text() == "*":
                        n.vanish()
                        n.gems_score()
                        self._score = self._score + (n.get_score())
                        banner.set_text(f"The Score: {self._score}")
                         
                    elif n.get_text() == "o":
                        n.vanish()
                        n.rocks_score()
                        self._score = self._score + (n.get_score())
                        banner.set_text(f"The Score: {self._score}")

                    elif n.get_text() == "#":
                        n.vanish()
                        n.diamon_score()
                        self._score = self._score + (n.get_score())
                        banner.set_text(f"The Score: {self._score}")

                    elif n.get_text() == "+":
                        n.vanish()
                        n.cross_score()
                        self._score = self._score + (n.get_score())
                        banner.set_text(f"The Score: {self._score}")
        
            
    def _do_outputs(self, cast):
        """Draws the actors on the screen.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()

