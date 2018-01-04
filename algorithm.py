"""Parses the yaml schedule and loads the bus schedule in the python objects"""

from typing import Any, Dict, List

import yaml

def get_schedule(schedule: str) -> Dict[str, Any]:
    """Parses the bus schedule from the yaml file and stores in the python
    object
    """

    with open(schedule, 'r') as file_obj:
        data = yaml.load(file_obj)

    return data

def get_the_closest_value(value: int, list_of_values: List[int]) -> int:
    for time in list_of_values:
        if value < time:
            break
    return time
