from game.casting.actor import Actor

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
        """add one point to the score
        
        returns: the score"""

        self.score = self.score + 1

    def rocks_score(self):    
        """substract a point from the score
        
        returns: the score"""
        
        self.score -= 1

    def cross_score(self):    
        """substract a five from the score
        
        returns: the score"""
        
        self.score = self.score - 5
    
    def diamon_score(self):
        """add five point to the score
        
        returns: the score"""

        self.score = self.score + 5

    def get_score(self):
        """gets the score of the artifact"""

        return self.score

    def vanish(self):
        """removes the gem or rock from the screen"""

        self._text = ""
