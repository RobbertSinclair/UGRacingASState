
#include "statefactory.hpp"

StateFactory::StateFactory(States State) 
{
    State = State;
}

ASSIStates StateFactory::getASSI() 
{
    return ASSI;
}

void StateFactory::setASSI(ASSIStates assi)
{
    ASSI = assi;
}

bool StateFactory::getEBS()
{
    return EBS;
}

void StateFactory::setEBS(bool EBS)
{
    EBS = EBS;
}

bool StateFactory::getR2D()
{
    return R2D;
}

void StateFactory::setR2D(bool R2D)
{
    R2D = R2D;
}

bool StateFactory::getTS()
{
    return TS;
}

void StateFactory::setTS(bool TS)
{
    TS = TS;
}

bool StateFactory::getSA()
{
    return SA;
}

void StateFactory::setSA(bool SA)
{
    SA = SA;
}

bool StateFactory::getSB()
{
    return SB;
}

void StateFactory::setSB(bool SB)
{
    SB = SB;
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