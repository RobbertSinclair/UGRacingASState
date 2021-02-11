from state import State

class AS_FINISHED(State):
    
    def __init__(self):
        super().__init__(TS=False, R2D=False, ASSI="BLUE CONT", SA=False, EBS=True)