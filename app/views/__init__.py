from slack_bolt.async_app import AsyncApp

from app.views.hello_world import hello_world_handler
from app.views.raffle_ticket_claim_error import raffle_ticket_claim_error_handler
from app.views.raffle_ticket_claim_inelegible import raffle_ticket_claim_inelegible_handler

VIEWS = [
    {
        "id": "hello_world",
        "handler": hello_world_handler,
    },
    {
        "id": "raffle_ticket_claim_error",
        "handler": raffle_ticket_claim_error_handler,
    },
    {
        "id": "raffle_ticket_claim_inelegible",
        "handler": raffle_ticket_claim_inelegible_handler,
    },
]


def register_views(app: AsyncApp):
    for view in VIEWS:
        app.view(view["id"])(view["handler"])
