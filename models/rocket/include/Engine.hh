/***************************************************************
PURPOSE: (Simulate a rockets engine)
***************************************************************/

class Engine
{
    public:

        double engineMass;      /* kg Mass of engine casing*/
        double fuelMass;        /* kg Mass of fuel in engine*/
        double operationalTime; /* s Time the engine is in use*/
        double thrust;          /* kg*m/s^2 */
        double massFlowRate;     /* -- Amount of mass lost per second*/


        int default_data(int engineMass, int fuelMass, int operationalTIme, int thrust);
        int initial_data();
        double fuel_mass(double time);

};