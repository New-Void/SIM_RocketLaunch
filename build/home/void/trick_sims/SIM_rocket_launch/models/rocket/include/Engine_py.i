%module m08942d8513c549eaf48fd075dee7e151

%include "trick/swig/trick_swig.i"


%insert("begin") %{
#include <Python.h>
#include <cstddef>
%}

%{
#include "/home/void/trick_sims/SIM_rocket_launch/models/rocket/include/Engine.hh"
%}

%trick_swig_class_typemap(Engine, Engine)




class Engine
{
    public:

        double engineMass;      

        double fuelMass;        

        double operationalTime; 

        double thrust;          

        double massFlowRate;     



        int default_data(int engineMass, int fuelMass, int operationalTIme, int thrust);
        int initial_data();
        double fuel_mass(double time);

};
#define TRICK_SWIG_DEFINED_Engine
#ifdef TRICK_SWIG_DEFINED_Engine
%trick_cast_as(Engine, Engine)
#endif
