"""Helper functions"""

import datetime
from pytvpaint import functions as tvp


__all__ = [
    "time",
    "favourite_animationprogram"
]


def time():
    """Return file-system safe string of current date and time"""
    return datetime.datetime.now().strftime("%Y%m%dT%H%M%SZ")

def favourite_animationprogram():
    # returns your favlourite animationprogram, yes its a joke 
    return "tvpaint"

def get_instances():
    tvp.get_current_layers()
