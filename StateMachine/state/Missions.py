from AbstractMission import AbstractMission

class AccelerationMission(AbstractMission):
	def __init__(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS, stage):
		super().__init__(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS, stage)


class SkidpadMission(AbstractMission):
	def __init__(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS, stage):
		super().__init__(self, TS, R2D, SA, SB, EBS, ASSI, stage)

class AutocrossMission(AbstractMission):
	def __init__(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS, stage):
		super().__init__(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS, stage)

class TrackDriveMission(AbstractMission):
	def __init__(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS, stage):
		super().__init__(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS, stage)

class EBSTest(AbstractMission):
	def __init__(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS, stage):
		super().__init__(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS, stage)

class Inspection(AbstractMission):
	def __init__(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS, stage):
		super().__init__(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS, stage)

class ManualDriving(AbstractMission):
	def __init__(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS, stage):
		super().__init__(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS, stage)



