/***************************************************************
PURPOSE: (Describe variables needed for rocket flight)
***************************************************************/

#ifndef _rocket_hh_
#define _rocket_hh_

#include "Engine.hh"

class Rocket
{
    public:
        Engine engStage1;
        Engine engStage2;
        Engine engStage3;


        double thrustForce[2];          /* N Force produced by thrust*/
        double dragForce[2];            /* N Force produced by Drag*/
        double gravitationalForce[2];   /* N Force produced by Earth and Moon*/
        double totalForce[2];           /* N */

        double acc[2] ;                 /* m/s2 xy-acceleration  */
        double vel[2] ;                 /* m/s xy-velocity */
        double pos[2] ;                 /* m xy-position */

        bool impact ;                   /* -- Has impact occured? */
        double impactTime;              /* s Time of Impact */
        int stage;                      /* -- Stage of Rocket*/
        int stage1Time;                 /* s Time of Stage 1 finished*/
        int stage2Time;                 /* s Time of Stage 2 finished*/
        int stage3Time;                 /* s Time of Stage 3 finished*/

        double payloadMass;             /* kg Mass of cargo rocket contains*/
        double totalMass;               /* kg */
        double changeInMass;            /* -- */
        double Cd;                      /* -- Coefficient of Drag*/
        double airDensity;              /* kg/m^3 */
        double crossArea;               /* m^2 */
        double earthRadius;             /* m */



        int default_data();
        int intial_data();
        int rocket_deriv();
        int rocket_integ();
        double InterpolateDensity(double x, const double xValues[], const double yValues[]);
        int rocket_stage1();
        int shutdown();
};

#endif