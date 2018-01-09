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

def get_the_closest_value(current_time: int, list_of_time: List[int]) -> List[int]:
    """Gets the time of the next available bus"""

    sorted_time = sorted(list_of_time)
    for i in range(len(sorted_time)):
        if current_time < sorted_time[i] and sorted_time[i] - current_time > 2:
            output = [sorted_time[i]]
            break
        elif current_time < sorted_time[i] and sorted_time[i] - current_time <= 2:
            output = [sorted_time[i], sorted_time[i+1]]
            break
    return output
