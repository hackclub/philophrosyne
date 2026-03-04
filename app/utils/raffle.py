from app.tables import RaffleTickets
from loguru import logger
from typing import Optional

# If exits with code 0, the ticket was claimed successfully. 
# 1, the user is not eligible for the ticket
# 2, there was an error claiming the ticket 
async def claim_ticket(
    user_id: str, ticket_kind: str
) -> int:
    logger.info(f"User {user_id} is trying to claim a ticket '{ticket_kind}'")
    eligibility_event = await search_for_elegible_event(user_id, ticket_kind)

    if eligibility_event == False:
        return 1
    
    if eligibility_event == None:
        return 2
    
    inserted = None

    try: 
        print(user_id,ticket_kind,eligibility_event)
        inserted = await RaffleTickets.insert(
            RaffleTickets(
                {RaffleTickets.owner_slack_id:user_id,
                 RaffleTickets.ticket_kind:ticket_kind,
                 # TODO: Store the event that made the user elegible for the ticket
                 RaffleTickets.related_event: None,
                 }
            )
        )
    except Exception as e:
        logger.error(f"Error claiming ticket for user {user_id} and ticket kind {ticket_kind}: {e}")
        return 2
    
    if inserted == None or len(inserted) == 0:
        logger.error(f"Failed to insert ticket for user {user_id} and ticket kind {ticket_kind}")
        return 2
    


    return 0

    pass

async def search_for_elegible_event(user_id: str, ticket_kind: str) -> Optional[str]:
    # TODO: Search in orchid for events that confirm the user is elegible for the ticket
    match ticket_kind:
        case "event_signup":
            return True
        case "coc_cipher":
            return False
        case _:
            logger.warning(f"Unknown ticket kind: {ticket_kind}")
            return None