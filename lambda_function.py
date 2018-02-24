"""Main application code"""

from typing import Any

from config import PATH_SCHEDULE
from pkg.algorithm import (
    get_schedule,
    get_the_closest_value,
)
from pkg.utils import (
    get_current_time,
    get_day_of_week, format_output,
)
import pkg.constant as cnst


def lambda_handler(event, context) -> Any:
    """The lambda enabler for Alexa skill set"""

    event_request = event['request']
    event_session = event['session']

    #Start of the session
    if event['session']['new']:
        on_session_start()

    #LaunchRequest
    if event_request['type'] == 'LaunchRequest':
        return welcome_response()

    #IntentRequest
    elif event_request['type'] == "IntentRequest":
        return on_intent(
            event_request,
            event_session,
        )
    #EndRequest
    elif event_request['type'] == "SessionEndedRequest":
        return on_session_ended(
            event_request,
            event_session,
        )


def on_session_start():
    """Called when the session is started"""
    print('Started new session')


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "FromBeacon":
        output = get_the_schedule_from_beacon()

        return build_response("", build_speechlet_response(
            "", output, "", True))
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])


def get_the_schedule_from_beacon() -> str:
    """Gets the schedule from the Beacon"""

    schedule = get_schedule(PATH_SCHEDULE)

    day_of_week = get_day_of_week()
    current_time = get_current_time()

    if day_of_week == 'sat':
        today_schedule = schedule[cnst.SATURDAY][cnst.SCHEDULE]
    elif day_of_week == 'sun':
        today_schedule = schedule[cnst.SUNDAY][cnst.SCHEDULE]
    else:
        today_schedule = schedule[cnst.WEEKDAY][cnst.SCHEDULE]

    next_bus_timing = get_the_closest_value(current_time, today_schedule)

    return format_output(next_bus_timing)


def welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = 'Welcome'
    speech_output = 'Welcome to the Beacon Shuttle App. ' \
                    'Please ask me for the next shuttle from beacon by saying,' \
                    'When is the next bus?'
    reprompt_text = 'Please ask me for the next shuttle from beacon by saying,' \
                    'When is the next bus?'
    should_end_session = False
    return(build_response(
        session_attributes,
        build_speechlet_response(
            card_title,
            speech_output,
            reprompt_text,
            should_end_session,
        )
    ))


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
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
