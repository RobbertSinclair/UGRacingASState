from AbstractMission import AbstractMission

if __name__ == "__main__" :

	passwordCorrect = "Pukkapad"

	def selections():
		selection = input("""Missions:
		\n\tAccelerationMission [AccM]
		\n\tSkidpadMission [SPM]
		\n\tAutocrossMission [ACM]
		\n\tTrackDriveMission [TDM]
		\n\tEBSTest [EBSTestM]
		\n\tInspection [InspectM]
		\n\tManualDriving [MDM]
		\nSelect Mission:- """)
		return selection
	
	#selection = selections()
	selection = "TDM"

	if selection == "AccM":
		from Missions import AccelerationMission
		mission = AccelerationMission()
		mission.run()
	
	elif selection == "SPM":
		from Missions import SkidpadMission
		mission = SkidpadMission()
		mission.run()
	
	elif selection == "ACM":
		from Missions import AutocrossMission
		mission = AutocrossMission()
		mission.run()
	
	elif selection == "TDM":
		from Missions import TrackDriveMission
		mission = TrackDriveMission()
		mission.run()
	
	elif selection == "EBSTestM":
		from Missions import EBSTest
		mission = EBSTest()
		mission.run()
	
	elif selection == "Inspect":
		from Missions import Inspection
		mission = Inspection()
		mission.run()
	
	elif selection == "MDM":
		from Missions import ManualDriving
		mission = ManualDriving()
		mission.run()
	
	else:
		print("Selection Invalid, Please Try Again.")
		#selections()

