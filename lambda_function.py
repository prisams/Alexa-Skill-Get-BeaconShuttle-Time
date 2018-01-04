"""Main application code"""

from config import PATH_SCHEDULE
from algorithm import get_schedule, get_the_closest_value
from utils import get_current_time, get_day_of_week, format_output
import constant


def lambda_handler(event, context):
    """The lambda enabler for Alexa skill set"""
    if event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "FromBeacon":
        output = get_the_schedule_from_beacon()

        return build_response("", build_speechlet_response(
            "", output, "", True))
    else:
        raise ValueError("Invalid intent")


def get_the_schedule_from_beacon() -> str:
    """Gets the schedule from the Beacon"""

    schedule = get_schedule(PATH_SCHEDULE)

    day_of_week = get_day_of_week()
    current_time = get_current_time()

    if day_of_week == 'sat':
        today_schedule = schedule[constant.SATURDAY][constant.SCHEDULE]
    elif day_of_week == 'sun':
        today_schedule = schedule[constant.SUNDAY][constant.SCHEDULE]
    else:
        today_schedule = schedule[constant.WEEKDAY][constant.SCHEDULE]

    next_bus_timing = get_the_closest_value(current_time, today_schedule)

    return format_output(next_bus_timing)

def build_response(session_attributes, speechlet_response):
    """Build the response for Alexa"""

    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    """Build the response for Alexa"""

    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
