from AbstractMission import AbstractMission

#class AbstractMissionAbstractMission(AbstractMission):
#	def __init__(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS, stage):
#		super().__init__(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS, stage)

class AccelerationMission(AbstractMission):
	print("AccelerationMission Loaded")

class SkidpadMission(AbstractMission):
	print("SkidpadMission Loaded")

class AutocrossMission(AbstractMission):
	print("AutocrossMission Loaded")

class TrackDriveMission(AbstractMission):
	print("TrackDriveMission Loaded")

class EBSTest(AbstractMission):
	print("EBSTest Loaded")

class Inspection(AbstractMission):
	print("Inspection Loaded")

class ManualDriving(AbstractMission):
	print("ManualDriving Loaded")



