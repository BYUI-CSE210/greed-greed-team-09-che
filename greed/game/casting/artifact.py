from game.casting.actor import Actor
from game.shared.point import Point
import random

class Artifact(Actor):
    """An artifact in this game could be a rock or a gem
    
    The responsability of the artifact is to keep track of the 
    score earned by the player
    
    Attributes:
        score (int) = the score earned depending if the character is a gem or a rock
    """
    
    def __init__(self):
        """construct a new instance of an artifact"""   
        super().__init__()
        #Create the starting score
        self.score = int(0)

    def gems_score(self):
        """add one point to the score"""

        self.score = 1

    def rocks_score(self):    
        """substract a point from the score"""
        
        self.score = -1

    def cross_score(self):    
        """substract a five from the score
        
        returns: the score"""
        
        self.score = -5
    
    def hashtag_score(self):
        """add five point to the score
        
        returns: the score"""

        self.score = 5

    def get_score(self):
        """gets the score of the artifact
        
        returns: the score value
        """

        return self.score

    def relocate(self):
        """removes the gem or rock from the screen
        then, changes its position to a random cell at the 
        top of the screen"""

        #get the text of the artifact to use it later
        text = self.get_text()
        #clear the text
        self._text = ""
        #set the new position and scale it to the cell size (25)
        x = random.randint(1, 59)
        y = 1
        new_p = Point(x, y)
        new_p = new_p.scale(25)
        self.set_position(new_p)
        #set the text to the original value
        self._text = text