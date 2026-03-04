from slack_bolt.async_app import AsyncApp
from loguru import logger

from app.events.message import message_handler
from app.events.app_home_opened import app_home_opened_handler

EVENTS = [
    {
        "name": "message",
        "handler": message_handler,
    },
    {
        "name": "app_home_opened",
        "handler": app_home_opened_handler,
    }
]


def register_events(app: AsyncApp):
    for event in EVENTS:
        app.event(event["name"])(event["handler"])
        logger.info(f"Registered event: {event['name']}")
