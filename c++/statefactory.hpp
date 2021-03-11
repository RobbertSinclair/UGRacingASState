
#include <iostream>

enum States {
    AS_OFF = 0,
    AS_READY = 1,
    AS_DRIVING = 2,
    AS_EMERGENCY = 3,
    AS_FINISHED = 4,
    MANUAL_DRIVING = 5
};

enum ASSIStates {
    OFF = 0,
    YELLOW_FLASH = 1,
    BLUE_FLASH = 2,
    YELLOW_CONT = 3,
    BLUE_CONT = 4
};


class StateFactory
{
    public:
        StateFactory(States State);
        void preUpdateState();
        void postUpdateState();
        void setStateMetrics();
        States getCurrentState();
    private:
        bool TS;
        bool SA;
        bool SB;
        bool EBS;
        bool R2D;
        ASSIStates ASSI;
        States State;
};