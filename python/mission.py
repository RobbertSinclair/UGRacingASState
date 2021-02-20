from state import State

class Missions(enum.Enum):
    AMI_NOT_SELECTED = 0
    AMI_ACCELERATION = 1
    AMI_SKIDPAD = 2
    AMI_AUTOCROSS = 3
    AMI_TRACK_DRIVE = 4
    AMI_BRAKE_TEST = 5
    AMI_INSPECTION = 6
    AMI_MANUAL = 7

class MissionStatus(enum.Enum):
    MISSION_NOT_SELECTED = 0
    MISSION_SELECTED = 1
    MISSION_RUNNING = 2
    MISSION_FINISHED = 3


class Mission():

    def __init__(self):
        pass

    def run(self):
        #While in SLAM method
        #Run all of the Velocity Estimation and SLAM
        #Run UGRDV.cpp in this method
        pass




