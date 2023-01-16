/***************************************************************
PURPOSE: (Simulate variables needed for rocket flight)
LIBRARY DEPENDENCY:
    ((Engine.o)(Rocket.o))
***************************************************************/

#include "../include/Rocket.hh"
#include "trick/integrator_c_intf.h"
#include "trick/exec_proto.h"
#include "math.h"
#include <stddef.h>
#include <stdio.h>


const double GM = 3.986004418e14;

const int numElements = 20;
const double altitudes[numElements] = {0, 1000, 2000, 3000, 4000, 5000, 600, 7000, 8000, 9000, 10000, 15000, 20000, 25000, 30000, 40000, 50000, 60000, 70000, 80000};
const double airPressures[numElements] = {1.225, 1.112, 1.007, 0.9093, 0.8194, 0.7364, 0.6601, 0.590, 0.5258, 0.4671, 0.4135, 0.1948, 0.08891, 0.04008, 0.01841, 0.003996, 0.001027, 0.0003097, 0.00008283, 0.00001846};

int Rocket::default_data()
{   //(dry mass (lbm), fuel (lbm), time of operation (s), thrust (lbf))
    engStage1.default_data(174179, 1277316, 20, 32027195.52 );
    engStage2.default_data(85275, 1043262, 60, 8896443.2);
    engStage3.default_data(2500, 30248, 1, 110093.48);

    payloadMass = 26762;
    totalMass = 2639722;

    crossArea = 2 * M_PI * (pow(4.1, 2)  + 2 * pow(3.66, 2));

    Cd = 0.6;

    earthRadius = 6378100;

    return 0;
}

int Rocket::initial_data()
{
    engStage1.initial_data();
    engStage2.initial_data();
    engStage3.initial_data();


    totalMass = payloadMass + engStage1.fuelMass + engStage1.engineMass
                + engStage2.fuelMass + engStage2.engineMass
                + engStage3.fuelMass + engStage3.engineMass;

    originalMass = totalMass;

    stage = 1;

    return 0;
}

int Rocket::rocket_deriv()
{
    double velocity = pow(vel[0], 2) + pow(vel[1], 2);
    airDensity = InterpolateDensity(pos[1], altitudes, airPressures);

    dragForce[1] = -0.5 * Cd * airDensity * crossArea * velocity;

    gravitationalForce[1] =  totalMass * GM/((earthRadius * earthRadius) + pos[1]); 

    switch (stage)
    {
    case 1:
        thrustForce[1] = engStage1.thrust;

        changeInMass = -engStage1.massFlowRate;

        break;
    case 2:
        thrustForce[2] = engStage2.thrust;

        changeInMass = -engStage2.massFlowRate;
                
        break;
    case 3:
        thrustForce[3] = engStage3.thrust;
        dragForce[1] = 0;

        changeInMass = -engStage3.massFlowRate;

        break;
    default:
        break;
    }

    totalForce[1] = dragForce[1] + gravitationalForce[1] + thrustForce[1];
    if (!impact)
    {
        acc[1] = totalForce[1] / totalMass;
    }
    
    return 0;
}

int Rocket::rocket_integ()
{
    int ipass;

    load_state(
        &pos[0],
        &pos[1],
        &vel[0],
        &vel[1],
        &totalMass,
        NULL);

    load_deriv(
        &vel[0],
        &vel[1],
        &acc[0],
        &acc[1],
        &changeInMass,
        NULL);

    ipass = integrate();

    unload_state(
        &pos[0],
        &pos[1],
        &vel[0],
        &vel[1],
        &totalMass,
        NULL);

    return ipass;
}

double Rocket::InterpolateDensity(double x, const double xValues[], const double yValues[])
{
    int i = 0;
    for (i; i+2 < numElements && xValues[i] < x; i++)
    {
        if(xValues[i + 1] == x)
        {
            return yValues[i + 1];
        }
    }

    double lowerX = xValues[i];
    double upperX = xValues[i + 1];
    double lowerY = yValues[i];
    double upperY = yValues[i + 1];

    if (x <= lowerX)
    {
        return yValues[0];
    }
    else if (x > upperX)
    {
        return 0;
    }
    else
    {
        return (((upperY - lowerY) / (upperX - lowerX)) * (x - lowerX) + lowerY);
    }
}

double Rocket::rocket_stage1()
{
    double tgo;
    double now;

    now = get_integ_time();
    rf.error = (engStage1.fuel_mass(now));

    tgo = regula_falsi( now, &rf);

    if (tgo == 0.0 && stage == 1) 
    {                     
        now = get_integ_time() ;
        reset_regula_falsi( now, &rf) ; 

        stage = 2;
        originalMass -= (engStage1.engineMass + engStage1.fuelMass);
        totalMass -= engStage1.engineMass;
        stage1Time = now;

        fprintf(stderr, "\n\n Stage 1 ends at: %.9f", stage1Time);
    }

    return tgo;
}

double Rocket::rocket_stage2()
{
    double tgo;
    double now;
    

    now = get_integ_time();
    rf.error = (engStage2.fuel_mass(now - stage1Time));

    tgo = regula_falsi( now, &rf);

    if (tgo == 0.0 && stage == 2) 
    {                     
        now = get_integ_time() ;
        reset_regula_falsi( now, &rf) ; 

        stage = 3;
        originalMass -= (engStage2.engineMass + engStage2.fuelMass);
        totalMass -= engStage2.engineMass;
        stage2Time = now;

        fprintf(stderr, "\n\n Stage 2 ends at: %.9f", stage2Time);
    }

    return tgo;
}

double Rocket::rocket_stage3()
{
    double tgo;
    double now;

    now = get_integ_time();
    rf.error = (engStage3.fuel_mass(now - stage2Time));

    tgo = regula_falsi( now, &rf);

    if (tgo == 0.0 && stage == 3) 
    {                     
        now = get_integ_time() ;
        reset_regula_falsi( now, &rf) ; 

        stage = 4;
        changeInMass = 0;
        stage3Time = now;

        fprintf(stderr, "\n\n Out of fuel");
    }

    return tgo;
}

double Rocket::rocket_orbit()
{
    double tgo;
    double now;

    rf.error = pos[1] - 10000;

    now = get_integ_time();
    tgo = regula_falsi( now, &rf);

    if (tgo == 0.0) 
    {                     
        now = get_integ_time() ;
        reset_regula_falsi( now, &rf) ; 

        fprintf(stderr, "\n\n Rocket has reached space at: %.9f", now);
    }
    return tgo;
}

double Rocket::rocket_impact()
{
    double tgo;
    double now;

    rf.error = pos[1];

    now = get_integ_time();
    tgo = regula_falsi( now, &rf);

    if (tgo == 0.0) 
    {                     
        now = get_integ_time() ;
        reset_regula_falsi( now, &rf) ; 

        impact = true ;
        impactTime = now ;
        vel[0] = 0.0 ;
        vel[1] = 0.0 ;
        acc[0] = 0.0 ; 
        acc[1] = 0.0 ;
        fprintf(stderr, "\n\nIMPACT: t = %.9f, pos[0] = %.9f\n\n", now, pos[0] ) ;

    }
    return tgo;
}

int Rocket::shutdown()
{
    double t = exec_get_sim_time();
    printf( "========================================\n");
    printf( "      Rocket State at Shutdown     \n");
    printf( "t = %g\n", t);
    printf( "pos = [%.9f, %.9f]\n", pos[0], pos[1]);
    printf( "vel = [%.9f, %.9f]\n", vel[0], vel[1]);
    printf( "acc = [%.9f, %.9f]\n", acc[0], acc[1]);
    printf( "========================================\n");
    return 0 ;
}