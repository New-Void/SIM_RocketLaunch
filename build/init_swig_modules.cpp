#include <Python.h>
#if PY_VERSION_HEX >= 0x03000000
extern "C" {

PyObject * PyInit__mb7c3ca89939274de2120b11c785a840a(void) ; /* /home/void/trick_sims/SIM_rocket_launch/S_source.hh */
PyObject * PyInit__m08942d8513c549eaf48fd075dee7e151(void) ; /* /home/void/trick_sims/SIM_rocket_launch/models/rocket/include/Engine.hh */
PyObject * PyInit__md979d5b88e1b5223e2529b0ae5738c70(void) ; /* /home/void/trick_sims/SIM_rocket_launch/models/rocket/include/Rocket.hh */
PyObject * PyInit__sim_services(void) ;
PyObject * PyInit__top(void) ;
PyObject * PyInit__swig_double(void) ;
PyObject * PyInit__swig_int(void) ;
PyObject * PyInit__swig_ref(void) ;

void init_swig_modules(void) {

    PyImport_AppendInittab("_m08942d8513c549eaf48fd075dee7e151", PyInit__m08942d8513c549eaf48fd075dee7e151) ;
    PyImport_AppendInittab("_md979d5b88e1b5223e2529b0ae5738c70", PyInit__md979d5b88e1b5223e2529b0ae5738c70) ;
    PyImport_AppendInittab("_mb7c3ca89939274de2120b11c785a840a", PyInit__mb7c3ca89939274de2120b11c785a840a) ;
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

void init_mb7c3ca89939274de2120b11c785a840a(void) ; /* /home/void/trick_sims/SIM_rocket_launch/S_source.hh */
void init_m08942d8513c549eaf48fd075dee7e151(void) ; /* /home/void/trick_sims/SIM_rocket_launch/models/rocket/include/Engine.hh */
void init_md979d5b88e1b5223e2529b0ae5738c70(void) ; /* /home/void/trick_sims/SIM_rocket_launch/models/rocket/include/Rocket.hh */
void init_sim_services(void) ;
void init_top(void) ;
void init_swig_double(void) ;
void init_swig_int(void) ;
void init_swig_ref(void) ;

void init_swig_modules(void) {

    init_m08942d8513c549eaf48fd075dee7e151() ;
    init_md979d5b88e1b5223e2529b0ae5738c70() ;
    init_mb7c3ca89939274de2120b11c785a840a() ;
    init_sim_services() ;
    init_top() ;
    init_swig_double() ;
    init_swig_int() ;
    init_swig_ref() ;
    return ;
}

}
#endif
