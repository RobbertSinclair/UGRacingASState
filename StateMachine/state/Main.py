import Missions
from AbstractMission import AbstractMission

if __name__ == "__main__" :

	#selection = input("Missions:\n\tTrackdrive [t]\n\tManual [m] \n\nSelect Mission:- ")
	selection = "t"
	if selection == "t":
		from Missions import TrackDriveMission
		mission = TrackDriveMission(False, False, False, False, False, False, "ASOFF")
		mission.run()




