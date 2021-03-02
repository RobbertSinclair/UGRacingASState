
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