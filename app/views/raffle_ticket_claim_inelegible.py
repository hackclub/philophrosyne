from blockkit import Input
from blockkit import Modal
from blockkit import PlainTextInput
from blockkit import Section
from slack_bolt.async_app import AsyncAck
from slack_sdk.web.async_client import AsyncWebClient


async def get_raffle_ticket_claim_inelegible():
    modal = (
        Modal()
        .callback_id("raffle_ticket_claim_inelegible")
        .title("Not Eligible")
        .add_block(Section("You are not eligible for this raffle ticket. Complete the required task first!"))
        .build()
    )
    return modal


async def raffle_ticket_claim_inelegible_handler(ack: AsyncAck, client: AsyncWebClient, body: dict):
    await ack()
    user = body["user"]["id"]
    view = body["view"]
    
    pass
