/***************************************************************
PURPOSE: (Simulate a rocket engine)
***************************************************************/

#include "../include/Engine.hh"

int Engine::default_data(int m, int fm, int ot, int th)
{
    engineMass = m;
    fuelMass = fm;
    operationalTime = ot;
    thrust = th;

}

int Engine::initial_data()
{
    massFlowRate = fuelMass / operationalTime;
}

double Engine::fuel_mass(double time)
{
   return fuelMass - (massFlowRate * time);
}

