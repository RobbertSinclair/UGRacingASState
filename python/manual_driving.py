from state import State

class MANUAL_DRIVING(State):

    def __init__(self):
        super().__init__(TS=True, R2D=True, ASSI="OFF", SA=False, SB=False, EBS=False)