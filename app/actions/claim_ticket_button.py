from slack_bolt.async_app import AsyncAck
from slack_bolt.async_app import AsyncRespond
from slack_sdk.web.async_client import AsyncWebClient

from app.views.raffle_ticket_claim_error import get_raffle_ticket_claim_error
from app.views.raffle_ticket_claim_inelegible import get_raffle_ticket_claim_inelegible
from app.utils.raffle import claim_ticket
from blockkit import Modal, Section

async def claim_ticket_button_handler(
    ack: AsyncAck, respond: AsyncRespond, client: AsyncWebClient, body: dict
):
    await ack()
    user = body["user"]
    trigger_id = body["trigger_id"]
    value = body["actions"][0]["value"]

    new_ticket: int = await claim_ticket(user["id"], value)
    if new_ticket == 2:
        view = await get_raffle_ticket_claim_error()
        await client.views_open(view=view, user=user["id"], trigger_id=trigger_id)
    elif new_ticket == 1:
        view = await get_raffle_ticket_claim_inelegible()
        await client.views_open(view=view, user=user["id"], trigger_id=trigger_id)

    elif new_ticket == 0:
        modal = (
            Modal()
            .title("Success!")
            .add_block(
                Section(
                    "You have successfully claimed a raffle ticket!"
                )
            )
            .build()
        )
        await client.views_open(view=modal, user=user["id"], trigger_id=trigger_id)
