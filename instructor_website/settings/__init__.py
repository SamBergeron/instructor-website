from .base import *

#Import local settings, skip if not there
try:
    from .local import *
except ImportError:
    pass