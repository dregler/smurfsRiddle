import random
from enum import Enum

class LightStatus(Enum):
    ON = 0
    OFF = 1

class Prison:

    def __init__(self, lightStatus):
        self.smurfs = []
        self.light = lightStatus 
    
    def imprison_smurf(self, smurf):
        self.smurfs.append(smurf)

    def next_day(self):
        chosen_smurf = random.choice(self.smurfs) 
        self.light = chosen_smurf.into_light_room(self.light)
        chosen_smurf.ask_me_finished()
        



class BasicSmurf:

    def __init__(self, name):
        self.smurf = name
    
    def into_light_room(self, lightStatus):
        return lightStatus

    def ask_me_finished(self):
        return False
        


prison = Prison(LightStatus.ON)

smurf0 = BasicSmurf("Petra")
smurf1 = BasicSmurf("Peter")
smurf2 = BasicSmurf("Torbine")

prison.imprison_smurf(smurf0) #TODO: prison.imprison_smurf(smurf0, smurf1, smurf2)
prison.imprison_smurf(smurf1)
prison.imprison_smurf(smurf2)

prison.next_day()
