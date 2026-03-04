from blockkit import Input
from blockkit import Modal
from blockkit import PlainTextInput
from blockkit import Section
from slack_bolt.async_app import AsyncAck
from slack_sdk.web.async_client import AsyncWebClient


async def get_raffle_ticket_claim_error():
    modal = (
        Modal()
        .callback_id("raffle_ticket_claim_error")
        .title("An error occurred :(")
        .add_block(Section("There was a problem checking whether you were eligible for this raffle ticket. Please try again later."))
        .build()
    )
    return modal


async def raffle_ticket_claim_error_handler(ack: AsyncAck, client: AsyncWebClient, body: dict):
    await ack()
    user = body["user"]["id"]
    view = body["view"]
    
    pass
