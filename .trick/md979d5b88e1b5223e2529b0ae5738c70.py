# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _md979d5b88e1b5223e2529b0ae5738c70
else:
    import _md979d5b88e1b5223e2529b0ae5738c70

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _md979d5b88e1b5223e2529b0ae5738c70.delete_SwigPyIterator

    def value(self):
        return _md979d5b88e1b5223e2529b0ae5738c70.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _md979d5b88e1b5223e2529b0ae5738c70.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _md979d5b88e1b5223e2529b0ae5738c70.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _md979d5b88e1b5223e2529b0ae5738c70.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _md979d5b88e1b5223e2529b0ae5738c70.SwigPyIterator_equal(self, x)

    def copy(self):
        return _md979d5b88e1b5223e2529b0ae5738c70.SwigPyIterator_copy(self)

    def next(self):
        return _md979d5b88e1b5223e2529b0ae5738c70.SwigPyIterator_next(self)

    def __next__(self):
        return _md979d5b88e1b5223e2529b0ae5738c70.SwigPyIterator___next__(self)

    def previous(self):
        return _md979d5b88e1b5223e2529b0ae5738c70.SwigPyIterator_previous(self)

    def advance(self, n):
        return _md979d5b88e1b5223e2529b0ae5738c70.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _md979d5b88e1b5223e2529b0ae5738c70.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _md979d5b88e1b5223e2529b0ae5738c70.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _md979d5b88e1b5223e2529b0ae5738c70.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _md979d5b88e1b5223e2529b0ae5738c70.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _md979d5b88e1b5223e2529b0ae5738c70.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _md979d5b88e1b5223e2529b0ae5738c70.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _md979d5b88e1b5223e2529b0ae5738c70:
_md979d5b88e1b5223e2529b0ae5738c70.SwigPyIterator_swigregister(SwigPyIterator)


def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    all_keys = [attr for attr in dir(class_type) if not attr.startswith('__')and attr != '_s' ]
    data_keys = sorted(class_type.__swig_setmethods__.keys())
    method_keys = [ x for x in all_keys if x not in data_keys ]
    raise AttributeError("Type %s does not contain member %s.\n%s data = %s\n%s methods = %s" %
     (self.__class__.__name__,name,self.__class__.__name__,data_keys,self.__class__.__name__,method_keys))

def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
# this line is changed to handle older swigs that used PySwigObject instead of the current SwigPyObject
        if type(value).__name__ == 'SwigPyObject' or type(value).__name__ == 'PySwigObject' :
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        all_keys = [attr for attr in dir(class_type) if not attr.startswith('__') and attr != '_s' ]
        data_keys = sorted(class_type.__swig_setmethods__.keys())
        method_keys = [ x for x in all_keys if x not in data_keys ]
        raise AttributeError("Type %s does not contain member %s.\n%s data = %s\n%s methods = %s" %
         (self.__class__.__name__,name,self.__class__.__name__,data_keys,self.__class__.__name__,method_keys))

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,1)

import m08942d8513c549eaf48fd075dee7e151
import sim_services
class Rocket(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    engStage1 = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_engStage1_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_engStage1_set)
    engStage2 = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_engStage2_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_engStage2_set)
    engStage3 = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_engStage3_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_engStage3_set)
    thrustForce = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_thrustForce_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_thrustForce_set)
    dragForce = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_dragForce_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_dragForce_set)
    gravitationalForce = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_gravitationalForce_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_gravitationalForce_set)
    totalForce = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_totalForce_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_totalForce_set)
    acc = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_acc_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_acc_set)
    vel = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_vel_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_vel_set)
    pos = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_pos_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_pos_set)
    impact = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_impact_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_impact_set)
    impactTime = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_impactTime_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_impactTime_set)
    stage = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_stage_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_stage_set)
    stage1Time = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_stage1Time_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_stage1Time_set)
    stage2Time = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_stage2Time_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_stage2Time_set)
    stage3Time = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_stage3Time_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_stage3Time_set)
    payloadMass = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_payloadMass_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_payloadMass_set)
    totalMass = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_totalMass_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_totalMass_set)
    originalMass = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_originalMass_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_originalMass_set)
    changeInMass = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_changeInMass_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_changeInMass_set)
    Cd = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_Cd_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_Cd_set)
    airDensity = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_airDensity_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_airDensity_set)
    crossArea = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_crossArea_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_crossArea_set)
    earthRadius = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_earthRadius_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_earthRadius_set)
    rf = property(_md979d5b88e1b5223e2529b0ae5738c70.Rocket_rf_get, _md979d5b88e1b5223e2529b0ae5738c70.Rocket_rf_set)

    def default_data(self, *args):
        return _md979d5b88e1b5223e2529b0ae5738c70.Rocket_default_data(self, *args)

    def initial_data(self, *args):
        return _md979d5b88e1b5223e2529b0ae5738c70.Rocket_initial_data(self, *args)

    def rocket_deriv(self, *args):
        return _md979d5b88e1b5223e2529b0ae5738c70.Rocket_rocket_deriv(self, *args)

    def rocket_integ(self, *args):
        return _md979d5b88e1b5223e2529b0ae5738c70.Rocket_rocket_integ(self, *args)

    def InterpolateDensity(self, *args):
        return _md979d5b88e1b5223e2529b0ae5738c70.Rocket_InterpolateDensity(self, *args)

    def rocket_stage1(self, *args):
        return _md979d5b88e1b5223e2529b0ae5738c70.Rocket_rocket_stage1(self, *args)

    def rocket_stage2(self, *args):
        return _md979d5b88e1b5223e2529b0ae5738c70.Rocket_rocket_stage2(self, *args)

    def rocket_stage3(self, *args):
        return _md979d5b88e1b5223e2529b0ae5738c70.Rocket_rocket_stage3(self, *args)

    def rocket_orbit(self, *args):
        return _md979d5b88e1b5223e2529b0ae5738c70.Rocket_rocket_orbit(self, *args)

    def rocket_impact(self, *args):
        return _md979d5b88e1b5223e2529b0ae5738c70.Rocket_rocket_impact(self, *args)

    def shutdown(self, *args):
        return _md979d5b88e1b5223e2529b0ae5738c70.Rocket_shutdown(self, *args)

    def __getitem__(self, *args):
        return _md979d5b88e1b5223e2529b0ae5738c70.Rocket___getitem__(self, *args)

    def __len__(self, *args):
        return _md979d5b88e1b5223e2529b0ae5738c70.Rocket___len__(self, *args)

    def __init__(self, **kwargs):
        import _sim_services
        this = _md979d5b88e1b5223e2529b0ae5738c70.new_Rocket()
        try: self.this.append(this)
        except: self.this = this
        if 'TMMName' in kwargs:
            self.this.own(0)
            isThisInMM = _sim_services.get_alloc_info_at(this)
            if isThisInMM:
                _sim_services.set_alloc_name_at(this, kwargs['TMMName'])
            else:
                _sim_services.TMM_declare_ext_var(this, _sim_services.TRICK_STRUCTURED, "Rocket", 0, kwargs['TMMName'], 0, None)
            alloc_info = _sim_services.get_alloc_info_at(this)
            alloc_info.stcl = _sim_services.TRICK_LOCAL
            alloc_info.alloc_type = _sim_services.TRICK_ALLOC_NEW


    __swig_destroy__ = _md979d5b88e1b5223e2529b0ae5738c70.delete_Rocket

# Register Rocket in _md979d5b88e1b5223e2529b0ae5738c70:
_md979d5b88e1b5223e2529b0ae5738c70.Rocket_swigregister(Rocket)


def castAsRocket(*args):
    return _md979d5b88e1b5223e2529b0ae5738c70.castAsRocket(*args)

