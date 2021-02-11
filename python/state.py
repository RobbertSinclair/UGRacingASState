class State():

    def __init__(self, TS, R2D, ASSI, SA=None, SB=None, EBS=None):
        self.TS = TS
        self.R2D = R2D
        self.ASSI = ASSI
        self.SA = SA
        self.SB = SB
        self.EBS = EBS

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


