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

# /home/bahram/trick_sims/SIM_rocket_launch/S_source.hh
import _ma68d583be73bccbeff58c5e9dc2de9ad
combine_cvars(all_cvars, cvar)
cvar = None

# /home/bahram/trick_sims/SIM_rocket_launch/models/rocket/include/Engine.hh
import _m8637df2a7f4da249c8fb9d8469376cbd
combine_cvars(all_cvars, cvar)
cvar = None

# /home/bahram/trick_sims/SIM_rocket_launch/models/rocket/include/Rocket.hh
import _ma25239703302c923bc361a3f42055bde
combine_cvars(all_cvars, cvar)
cvar = None

# /home/bahram/trick_sims/SIM_rocket_launch/S_source.hh
from ma68d583be73bccbeff58c5e9dc2de9ad import *
# /home/bahram/trick_sims/SIM_rocket_launch/models/rocket/include/Engine.hh
from m8637df2a7f4da249c8fb9d8469376cbd import *
# /home/bahram/trick_sims/SIM_rocket_launch/models/rocket/include/Rocket.hh
from ma25239703302c923bc361a3f42055bde import *

# S_source.hh
import _ma68d583be73bccbeff58c5e9dc2de9ad
from ma68d583be73bccbeff58c5e9dc2de9ad import *

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

