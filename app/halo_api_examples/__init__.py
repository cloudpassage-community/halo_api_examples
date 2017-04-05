import sys
import os

# add the halo_general directory to the path so we can import it
cwd = os.getcwd()
halo_general_path = "%s/../halo_general" % cwd
sys.path.append(halo_general_path)

from config_helper import ConfigHelper # NOQA
from halo_general import HaloGeneral # NOQA
from halo_api_examples import HaloApiExamples # NOQA

__author__ = "CloudPassage"
__version__ = "1.0"
