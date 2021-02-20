import enum

class States(enum.Enum):
    AS_OFF = 0
    AS_READY = 1
    AS_EMERGENCY = 2
    AS_FINISHED = 3
    AS_DRIVING = 4
    MANUAL_DRIVING = 5
    


class State():
    #TS=True, R2D=True, ASSI="OFF", SA=False, SB=False, EBS=False
    stateValues =  {
        States.AS_OFF: {"TS": False, "R2D": False, "ASSI": "OFF", "SA": False, "SB": False, "EBS": None},
        States.AS_READY: {"TS": True, "R2D": False, "ASSI": "OFF", "SA": False, "SB": False, "EBS": False },
        States.AS_DRIVING: {"TS": True, "R2D": True, "ASSI": "YELLOW FLASH", "SA": True, "SB": False, "EBS": False },
        States.AS_EMERGENCY: {"TS": False, "R2D": False, "ASSI": "BLUE FLASH", "SA": None, "SB": None, "EBS": True },
        States.AS_FINISHED: {"TS": False, "R2D": False, "ASSI": "OFF", "SA": False, "SB": False, "EBS": None},
        States.AS_FINISHED: {"TS": False, "R2D": False, "ASSI": "BLUE CONT", "SA": False, "SB": None, "EBS": True},
        States.MANUAL_DRIVING: {"TS": True, "R2D": True, "ASSI": "OFF", "SA": False, "SB": False, "EBS": False}
    }
    
    def __init__(self, TS, R2D, ASSI, SA=None, SB=None, EBS=None):
        self.TS = TS
        self.R2D = R2D
        self.ASSI = ASSI
        self.SA = SA
        self.SB = SB
        self.EBS = EBS
        self.the_state = States.AS_OFF

    def setStateMetrics(self):
        #Get the new state inside the classes
        state_dictionary = self.stateValues[self.the_state]
        

    

    def get_TS(self):
        return self.TS 
    
    def set_TS(self, new_ts):
        self.TS = new_ts
    
    def get_R2D(self):
        return self.R2D

    def set_R2D(self, R2D):
        self.R2D = R2D

    def get_ASSI(self):
        return self.ASSI

    def set_ASSI(self, ASSI):
        self.ASSI = ASSI

    def get_SA(self):
        return self.SA

    def set_SA(self, SA):
        self.SA = SA

    def get_SB(self):
        return self.SB

    def set_SB(self, SB):
        self.SB = SB

    def get_EBS(self):
        return self.EBS

    def set_EBS(self, EBS):
        self.EBS = EBS 


