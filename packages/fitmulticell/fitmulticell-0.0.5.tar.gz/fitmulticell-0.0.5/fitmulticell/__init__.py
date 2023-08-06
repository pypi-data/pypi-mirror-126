"""
FitMultiCell
============

Fitting of multi-cellular models combining the tools morpheus and pyABC.
"""

from .version import __version__
from .model import MorpheusModel, MorpheusModels
from .sumstat import *  # noqa: F403
from .distance import *  # noqa: F403

import os
import logging

# Set log level
try:
    loglevel = os.environ['FitMultiCell_LOG_LEVEL'].upper()
except KeyError:
    loglevel = 'INFO'
logger = logging.getLogger("FitMultiCell")
logger.setLevel(loglevel)
sh = logging.StreamHandler()
sh.setFormatter(logging.Formatter('%(name)s %(levelname)s: %(message)s'))
logger.addHandler(sh)
