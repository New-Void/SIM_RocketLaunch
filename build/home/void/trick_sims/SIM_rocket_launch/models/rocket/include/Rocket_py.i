%module md979d5b88e1b5223e2529b0ae5738c70

%include "trick/swig/trick_swig.i"


%insert("begin") %{
#include <Python.h>
#include <cstddef>
%}

%{
#include "/home/void/trick_sims/SIM_rocket_launch/models/rocket/include/Rocket.hh"
%}

%trick_swig_class_typemap(Rocket, Rocket)




#ifndef _rocket_hh_
#define _rocket_hh_

%import "build/home/void/trick_sims/SIM_rocket_launch/models/rocket/include/Engine_py.i"
%import(module="sim_services") "trick/regula_falsi.h"

class Rocket
{
    public:
        Engine engStage1;
        Engine engStage2;
        Engine engStage3;


        double thrustForce[2];          

        double dragForce[2];            

        double gravitationalForce[2];   

        double totalForce[2];           


        double acc[2] ;                 

        double vel[2] ;                 

        double pos[2] ;                 


        bool impact ;                   

        double impactTime;              

        int stage;                      

        double stage1Time;              

        double stage2Time;              

        double stage3Time;              


        double payloadMass;             

        double totalMass;               

        double originalMass;            

        double changeInMass;            

        double Cd;                      

        double airDensity;              

        double crossArea;               

        double earthRadius;             


        REGULA_FALSI rf;

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
#define TRICK_SWIG_DEFINED_Rocket

#endif
#ifdef TRICK_SWIG_DEFINED_Rocket
%trick_cast_as(Rocket, Rocket)
#endif
