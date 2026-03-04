from slack_bolt.async_app import AsyncSay
from slack_sdk.web.async_client import AsyncWebClient
from blockkit import Home, Section, Divider, Actions, Button, Header, ImageEl
from app.tables import RaffleTickets

available_raffle_tickets = [
    {
        "text": "Join the #welcome-to-hack-club channel and introduce yourself!",
        "ticket_kind": "wthc_message_sent",
    },
    {
        "text": "Solve the Code of Conduct cipher",
        "ticket_kind": "coc_cipher",
    },
    {
        "text": "Go sign up for a Hack Club event!",
        "ticket_kind": "event_signup",
    }
]

async def app_home_opened_handler(client: AsyncWebClient,body: dict):
    user = body["event"]["user"]
    #TODO: Do not render big tutorial (raffle view) until the user has completed the first onboarding part
    should_render_big_tutorial = True
    
    if should_render_big_tutorial:
        tickets = await pull_user_tickets(user)
        view = render_raffle_home_view(tickets)

        await client.views_publish(
            user_id=user,
            view=view,
        )



def render_raffle_home_view(tickets: list[str]):
    base = (
        Home()
        .add_block(
            Header(text="Welcome to the Hack Club Slack!"),
        )
        .add_block(
            Section(text="Get raffle tickets by completing tasks within the Hack Club community!")
            .accessory(ImageEl(image_url="https://avatars.githubusercontent.com/u/5633654?s=200&v=4", alt_text="Hack Club logo")),
        )
        .add_block(Divider())
    )

    for item in available_raffle_tickets:
        if item["ticket_kind"] in tickets:
            base.add_block(
                Section(text=f"• *{item['text']}* | Already claimed", )
                #.accessory(
                #    ImageEl(
                #    image_url="https://placedog.net/500/200?r",
                #    alt_text="Already claimed"
                #    )
                #),
            )
        else:
            base.add_block(
                Section(text=f"• *{item['text']}*", )
                .accessory(
                    Button(
                        text="Claim",
                        action_id="claim_ticket",
                        value=item["ticket_kind"],
                    )
                ),
            )
    base.add_block(Divider())

    base.add_block(
        Actions()
        .add_element(
            Button(
                text="Rules and prizes",
                url="https://philophrosyne.hackclub.com/raffle-info",
            ))
        .add_element(
            Button(
                text="🎟️ Allocate tickets",
                style="primary",
                action_id="allocate_tickets_to_raffles",
            )
        )
        )

    return (base.build())

async def pull_user_tickets(slack_id: str) -> list[str]:
    q = await RaffleTickets.select().columns(RaffleTickets.ticket_kind).where(
        RaffleTickets.owner_slack_id == slack_id
    )
    return list(map(lambda r: r.get("ticket_kind"), q))