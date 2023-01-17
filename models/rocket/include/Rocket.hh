/***************************************************************
PURPOSE: (Describe variables needed for rocket flight)
***************************************************************/

#ifndef _rocket_hh_
#define _rocket_hh_

#include "Engine.hh"
#include "trick/regula_falsi.h"

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
        bool inSpace;                   /* -- Has the rocket reached space? */
        int stage;                      /* -- Stage of Rocket*/
        double stage1Time;              /* s Time of Stage 1 finished*/
        double stage2Time;              /* s Time of Stage 2 finished*/
        double stage3Time;              /* s Time of Stage 3 finished*/

        double payloadMass;             /* kg Mass of cargo rocket contains*/
        double totalMass;               /* kg */
        double originalMass;            /* kg */
        double changeInMass;            /* -- */
        double Cd;                      /* -- Coefficient of Drag*/
        double airDensity;              /* kg/m^3 */
        double crossArea;               /* m^2 */
        double earthRadius;             /* m */

        REGULA_FALSI rf1;
        REGULA_FALSI rf2;
        REGULA_FALSI rf3;
        REGULA_FALSI rfOrbit;
        REGULA_FALSI rfImpact;

        int default_data();
        int initial_data();
        int rocket_deriv();
        int rocket_integ();
        double InterpolateDensity(double x, const double xValues[], const double yValues[]);
        double rocket_stage1();
        double rocket_stage2();
        double rocket_stage3();
        double rocket_orbit();
        double rocket_impact();
        int shutdown();
};

#endif