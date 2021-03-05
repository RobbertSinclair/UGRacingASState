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
        void transition();
    private:
        StateFactory stateDecider;
        Missions mission; 
};

class NotSelectedMission : public AbstractMission {
    public:
        void run();
};

class AccelerationMission : public AbstractMission {
    public:
        void run();
};

class SkidPadMission : public AbstractMission {
    public:
        void run();
};

class AutocrossMission : public AbstractMission {
    public:
        void run();
};

class TrackDriveMission : public AbstractMission {
    public:
        void run();
};

class AccelerationMission : public AbstractMission {
    public:
        void run();
};

class BrakeTestMission : public AbstractMission {
    public:
        void run();
};

class ManualMission : public AbstractMission {
    public:
        void run();
};