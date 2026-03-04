from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from app.tables import RaffleTickets

ID = "2026-03-04T18:44:08:643135"
VERSION = "1.30.0"
DESCRIPTION = "Adds uniqueness constraint to raffle tickets kinds and slack ids"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="", description=DESCRIPTION
    )

    async def run():
        q = "CREATE UNIQUE INDEX ON raffle_tickets (owner_slack_id, ticket_kind)"
        await RaffleTickets.raw(q)
        print(f"running {ID}")

    manager.add_raw(run)

    return manager
