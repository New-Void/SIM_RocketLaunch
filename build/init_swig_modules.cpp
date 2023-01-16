#include <Python.h>
#if PY_VERSION_HEX >= 0x03000000
extern "C" {

PyObject * PyInit__ma68d583be73bccbeff58c5e9dc2de9ad(void) ; /* /home/bahram/trick_sims/SIM_rocket_launch/S_source.hh */
PyObject * PyInit__m8637df2a7f4da249c8fb9d8469376cbd(void) ; /* /home/bahram/trick_sims/SIM_rocket_launch/models/rocket/include/Engine.hh */
PyObject * PyInit__ma25239703302c923bc361a3f42055bde(void) ; /* /home/bahram/trick_sims/SIM_rocket_launch/models/rocket/include/Rocket.hh */
PyObject * PyInit__sim_services(void) ;
PyObject * PyInit__top(void) ;
PyObject * PyInit__swig_double(void) ;
PyObject * PyInit__swig_int(void) ;
PyObject * PyInit__swig_ref(void) ;

void init_swig_modules(void) {

    PyImport_AppendInittab("_m8637df2a7f4da249c8fb9d8469376cbd", PyInit__m8637df2a7f4da249c8fb9d8469376cbd) ;
    PyImport_AppendInittab("_ma25239703302c923bc361a3f42055bde", PyInit__ma25239703302c923bc361a3f42055bde) ;
    PyImport_AppendInittab("_ma68d583be73bccbeff58c5e9dc2de9ad", PyInit__ma68d583be73bccbeff58c5e9dc2de9ad) ;
    PyImport_AppendInittab("_sim_services", PyInit__sim_services) ;
    PyImport_AppendInittab("_top", PyInit__top) ;
    PyImport_AppendInittab("_swig_double", PyInit__swig_double) ;
    PyImport_AppendInittab("_swig_int", PyInit__swig_int) ;
    PyImport_AppendInittab("_swig_ref", PyInit__swig_ref) ;
    return ;
}

}
#else
extern "C" {

void init_ma68d583be73bccbeff58c5e9dc2de9ad(void) ; /* /home/bahram/trick_sims/SIM_rocket_launch/S_source.hh */
void init_m8637df2a7f4da249c8fb9d8469376cbd(void) ; /* /home/bahram/trick_sims/SIM_rocket_launch/models/rocket/include/Engine.hh */
void init_ma25239703302c923bc361a3f42055bde(void) ; /* /home/bahram/trick_sims/SIM_rocket_launch/models/rocket/include/Rocket.hh */
void init_sim_services(void) ;
void init_top(void) ;
void init_swig_double(void) ;
void init_swig_int(void) ;
void init_swig_ref(void) ;

void init_swig_modules(void) {

    init_m8637df2a7f4da249c8fb9d8469376cbd() ;
    init_ma25239703302c923bc361a3f42055bde() ;
    init_ma68d583be73bccbeff58c5e9dc2de9ad() ;
    init_sim_services() ;
    init_top() ;
    init_swig_double() ;
    init_swig_int() ;
    init_swig_ref() ;
    return ;
}

}
#endif
