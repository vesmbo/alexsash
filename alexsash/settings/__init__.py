__author__ = 'alex'

from .main import *

try:
    from .local import *
except ImportError:
    pass