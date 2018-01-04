"""Contains the utility functions for the application"""

from datetime import datetime
from typing import List

import pytz


def get_current_time() -> int:
    """Returns the current hour and min in number format"""
    hour_min = datetime.now(
        pytz.timezone('US/Eastern')
    ).strftime("%H,%M").split(',')

    return int(''.join(hour_min))

def get_day_of_week() -> str:
    """Returns the day of the week"""
    return datetime.now(pytz.timezone('US/Eastern')).strftime("%a").lower()

def format_output(output_time: int) -> str:
    """Formats the time in am/pm and returns it back"""
    min = output_time % 100
    hour = int(output_time / 100)

    if hour >= 12:
        if hour > 12:
            hour = hour -12
        response = f'{hour}:{min} pm'
    else:
        response = f'{hour}:{min} am'

    return f'The next bus from Beacon is at {response}'
