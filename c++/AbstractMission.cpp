#include <iostream>
#include "missions.hpp"

void AbstractMission::run() {
    States theState = stateDecider.getCurrentState();
    switch(theState) {
        case AS_READY:
            runASReady();
            run();
            break;
        case AS_DRIVING:
            runASDriving();
            run();
            break;
        case AS_EMERGENCY:
            runASEmergency();
            run();
            break;
        case AS_FINISHED:
            runASFinished();
            run();
            break;
        case AS_OFF:
            runASOff();
            run();
            break;
        case MANUAL_DRIVING:
            runManualDriving();
            run();
            break;
        default:
            break;
    }
}

void AbstractMission::transitionControl() {
    
}