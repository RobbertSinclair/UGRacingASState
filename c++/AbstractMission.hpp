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
}