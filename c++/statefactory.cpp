
#include "statefactory.hpp"

StateFactory::StateFactory(States State) 
{
    State = State;
}

void StateFactory::setStateMetrics()
{
    switch(State) 
    {
        case AS_OFF:
            TS = false;
            R2D = false;
            SA = false;
            SB = false;
            EBS = NULL;
            ASSI = OFF;
            break;
        case AS_READY:
            TS = true;
            R2D = false;
            SA = true;
            SB = true;
            EBS = false;
            ASSI = YELLOW_CONT;
            break;
        case AS_DRIVING:
            TS = true;
            R2D = true;
            SA = true;
            SB = true;
            EBS = false;
            ASSI = YELLOW_FLASH;
            break;
        case AS_EMERGENCY:
            TS = false;
            R2D = false;
            SA = NULL;
            SB = NULL;
            EBS = true;
            ASSI = BLUE_FLASH;
            break;
        case AS_FINISHED:
            TS = false;
            R2D = false;
            SA = false;
            SB = NULL;
            EBS = true;
            ASSI = BLUE_CONT; 
            break;
        default:
            break;
    }

}