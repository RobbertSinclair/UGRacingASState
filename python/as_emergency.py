from state import State

class AS_EMERGENCY(State):

    def __init__(self):
        super().__init__(TS=False, R2D=False, ASSI="BLUE FLASH", EBS=True)