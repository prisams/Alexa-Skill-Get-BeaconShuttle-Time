"""Contains the utility functions for the application"""

from datetime import datetime
from typing import List

import pytz

from constant import OUTPUT_STRING

def get_current_time() -> int:
    """Returns the current hour and min in number format"""
    hour_min = datetime.now(
        pytz.timezone('US/Eastern')
    ).strftime("%H,%M").split(',')

    return int(''.join(hour_min))

def get_day_of_week() -> str:
    """Returns the day of the week"""
    return datetime.now(pytz.timezone('US/Eastern')).strftime("%a").lower()

def format_output(output_time: List[int]) -> str:

    if len(output_time) == 1:
        return f'{OUTPUT_STRING}{format_time(output_time[0])}'

    return f'{OUTPUT_STRING}{format_time(output_time[0])} \
    and then at {format_time(output_time[1])}'


def format_time(time: int) -> str:
    """Formats the time in am/pm and returns it back"""
    min = time % 100
    hour = int(time / 100)

    if hour >= 12:
        if hour > 12:
            hour = hour -12
        response = f'{hour} {min} pm'
    else:
        response = f'{hour} {min} am'

    return response
