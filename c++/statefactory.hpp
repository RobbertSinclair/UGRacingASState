
#include <iostream>

enum States {
    AS_OFF = 0,
    AS_READY = 1,
    AS_DRIVING = 2,
    AS_EMERGENCY = 3,
    AS_FINISHED = 4,
    MANUAL_DRIVING = 5
}

enum ASSIStates {
    OFF = 0,
    YELLOW_FLASH = 1,
    BLUE_FLASH = 2,
    YELLOW_CONT = 3,
    BLUE_CONT = 4
}


class StateFactory
{
    public:
        StateFactory(States State);
        void setTS(bool TS);
        bool getTS();
        void setSA(bool SA);
        bool getSA();
        void setEBS(bool EBS);
        bool getEBS();
        void setR2D(bool R2D);
        ASSIStates getASSI();
        void setASSI(ASSIStates assi);
    private:
        bool TS;
        bool SA;
        bool SB;
        bool EBS;
        bool R2D;
        ASSIStates ASSI;
        States State;
};