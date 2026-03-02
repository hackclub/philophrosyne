from slack_bolt.async_app import AsyncSay
from slack_sdk.web.async_client import AsyncWebClient
from blockkit import Home, Section, Divider, Actions, Button, Header, Image


tutorial_items = [
    {
        "text": "Join the #general channel and introduce yourself!",
        "emoji": ":wave:",
    },
    {
        "text": "Check out the #events channel to see upcoming events!",
        "emoji": ":calendar:",
    },
]

async def message_handler(client: AsyncWebClient, say: AsyncSay, body: dict):
    user = body["event"]["user"]

    view = render_app_home_view()
    await client.views_publish(
        user_id=user,
        view=view,
    )



def render_app_home_view():
    base = (
        Home()
        .add_block(
            Header(text="Welcome to the Hack Club Slack!"),
        )
        .add_block(
            Section(text="Get raffle tickets by completing tasks within the Hack Club community!"),
        )
    )

    for item in tutorial_items:
        base.add_block(
            Section(text=f"{item['emoji']} {item['text']}", )
            .accessory(
                Image(
                    image_url="https://placedog.net/500/500?r",
                    alt_text="Tutorial item"
                )
            ),
        )
    
    base.add_block(Divider())

    return (base.build())