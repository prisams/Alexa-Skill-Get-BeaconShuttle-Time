"""Stores the configuration needed for the application"""

import os


#############################################################################
# Paths
#############################################################################
PATH_ROOT = os.path.dirname(os.path.abspath(__file__))
PATH_SCHEDULE = os.path.join(PATH_ROOT, 'bus_schedule.yaml')
