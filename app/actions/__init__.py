from slack_bolt.async_app import AsyncApp

from app.actions.hello_world import hello_world_handler
from app.actions.claim_ticket_button import claim_ticket_button_handler


ACTIONS = [
    {
        "id": "hello_world",
        "handler": hello_world_handler,
    },
    {
        "id": "claim_ticket",
        "handler": claim_ticket_button_handler,
    },
]


def register_actions(app: AsyncApp):
    for action in ACTIONS:
        app.action(action["id"])(action["handler"])
