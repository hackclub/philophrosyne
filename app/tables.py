# An example of how to create a table. Read the docs for more info: https://piccolo-orm.readthedocs.io/
# from piccolo.table import Table
# from piccolo.columns import Integer, Text, Varchar
# class Person(Table):
#     slack_id = Varchar(length=20, index=True)
#     age = Integer()
from piccolo.table import Table
from piccolo.columns import Text, Integer, Timestamptz, Varchar, UUID

class RaffleTickets(Table):
    ticket_id = UUID(primary_key=True)
    owner_slack_id = Varchar(length=20, null=False)
    ticket_kind = Text(null=False)
    claim_timestamp = Timestamptz(null=False)