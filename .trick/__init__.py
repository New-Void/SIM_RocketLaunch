from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)
import sys
import os
sys.path.append(os.getcwd() + "/trick.zip/trick")

import _sim_services
from sim_services import *

# create "all_cvars" to hold all global/static vars
all_cvars = new_cvar_list()
combine_cvars(all_cvars, cvar)
cvar = None

# /home/void/trick_sims/SIM_rocket_launch/S_source.hh
import _mb7c3ca89939274de2120b11c785a840a
combine_cvars(all_cvars, cvar)
cvar = None

# /home/void/trick_sims/SIM_rocket_launch/models/rocket/include/Engine.hh
import _m08942d8513c549eaf48fd075dee7e151
combine_cvars(all_cvars, cvar)
cvar = None

# /home/void/trick_sims/SIM_rocket_launch/models/rocket/include/Rocket.hh
import _md979d5b88e1b5223e2529b0ae5738c70
combine_cvars(all_cvars, cvar)
cvar = None

# /home/void/trick_sims/SIM_rocket_launch/S_source.hh
from mb7c3ca89939274de2120b11c785a840a import *
# /home/void/trick_sims/SIM_rocket_launch/models/rocket/include/Engine.hh
from m08942d8513c549eaf48fd075dee7e151 import *
# /home/void/trick_sims/SIM_rocket_launch/models/rocket/include/Rocket.hh
from md979d5b88e1b5223e2529b0ae5738c70 import *

# S_source.hh
import _mb7c3ca89939274de2120b11c785a840a
from mb7c3ca89939274de2120b11c785a840a import *

import _top
import top

import _swig_double
import swig_double

import _swig_int
import swig_int

import _swig_ref
import swig_ref

from shortcuts import *

from exception import *

cvar = all_cvars

