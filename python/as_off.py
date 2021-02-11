from state import State

class AS_OFF(State):

    def __init__(self):
        #Get the constructor of the State class to define the metrics
        #It means that we don't have to repeat ourselves
        super().__init__(TS=False, R2D=False, ASSI="OFF", SA=False, SB=False)

    def selectAutonomousMission(self):
        #TODO add functionality to this.
        self.getReady()

    def getReady():
        if EBS and ASMS and TS:
            #Move to the Ready State
            pass
        