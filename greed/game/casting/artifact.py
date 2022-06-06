
from game.casting.actor import Actor
class Artifact(Actor):

    def __init__(self):

        super().__init__()
        #Create the starting score
        self.score = 10

    def gems_score(self):
    #Indicate score if the user touches a gem
        self.score += 1
    def rocks_score(self):    
    #Indicate score if the user touches a rock
       self.score -= 1

    
#Director, despues de "linea 62"
    """   for artifact in artifacts:
            if robot.get_position().equals(self.gems_object()):
               self.gems_score()
            
            elif robot.get_position().equals(self.rocks_object()):
                self.rocks_score()  
       
    """