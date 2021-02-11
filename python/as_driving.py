from state import State

class AS_DRIVING(State):

    def __init__(self):
        super().__init__(TS=True, R2D=True, ASSI="YELLOW FLASH", SA=True, SB=True, EBS=True)