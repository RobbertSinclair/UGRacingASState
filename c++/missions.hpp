#include <iostream>
#include "statefactory.hpp"

enum Missions 
{
    AMI_NOT_SELECTED = 0,
    AMI_ACCELERATION = 1,
    AMI_SKIDPAD = 2,
    AMI_AUTOCROSS = 3,
    AMI_TRACK_DRIVE = 4,
    AMI_BRAKE_TEST = 5,
    AMI_INSPECTION = 6,
    AMI_MANUAL = 7
};

class AbstractMission 
{
    public:
        AbstractMission();
        void run();
        void runASReady();
        void runASDriving();
        void runASEmergency();
        void runASFinished();
        void runManualDriving();        
        void transitionControl();
        void transitionASOff();
        void transitionASEmergency();
        void transitionASReady();
        void transitionASDriving();
        void transitionASFinished();
        void transitionManual();
    private:
        StateFactory stateDecider;
        Missions mission; 
};

class NotSelectedMission : public AbstractMission {
    public:
        void run();
        void runASReady();
        void runASDriving();
        void runASEmergency();
        void runASFinished();
        void runManualDriving();
};

class AccelerationMission : public AbstractMission {
    public:
        void run();
        void runASReady();
        void runASDriving();
        void runASEmergency();
        void runASFinished();
        void runManualDriving();
};

class SkidPadMission : public AbstractMission {
    public:
        void run();
        void runASReady();
        void runASDriving();
        void runASEmergency();
        void runASFinished();
        void runManualDriving();
};

class AutocrossMission : public AbstractMission {
    public:
        void run();
        void runASReady();
        void runASDriving();
        void runASEmergency();
        void runASFinished();
        void runManualDriving();
};

class TrackDriveMission : public AbstractMission {
    public:
        void run();
        void runASReady();
        void runASDriving();
        void runASEmergency();
        void runASFinished();
        void runManualDriving();
};

class AccelerationMission : public AbstractMission {
    public:
        void run();
        void runASReady();
        void runASDriving();
        void runASEmergency();
        void runASFinished();
        void runManualDriving();
};

class BrakeTestMission : public AbstractMission {
    public:
        void run();
        void runASReady();
        void runASDriving();
        void runASEmergency();
        void runASFinished();
        void runManualDriving();
};

class ManualMission : public AbstractMission {
    public:
        void run();
        void runASReady();
        void runASDriving();
        void runASEmergency();
        void runASFinished();
        void runManualDriving();
};