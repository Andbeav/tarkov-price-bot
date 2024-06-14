from os import environ

ACCESS_TOKEN = environ['ACCESS_TOKEN']
COMMAND_PREFIX = environ.get('COMMAND_PREFIX', '!')
CHANNEL_NAME = environ['CHANNEL_NAME']
TARKOV_DEV_GRAPHQL_TRANSPORT = environ['TARKOV_DEV_GRAPHQL_TRANSPORT']

# GraphQL client
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

transport = AIOHTTPTransport(url=TARKOV_DEV_GRAPHQL_TRANSPORT)
client = Client(transport=transport, fetch_schema_from_transport=True)

async def fetchItemData(item_name):
    query = gql(
        """
        query {
          items(name: "%s") {
            normalizedName
            lastLowPrice
          }
        }
        """ % item_name
    )
    result = await client.execute_async(query)
    data = result['items']

    if len(data) == 0: return False
    return data[0]

# twitchio

from twitchio.ext import commands

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=ACCESS_TOKEN, prefix=COMMAND_PREFIX, initial_channels=[CHANNEL_NAME])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        if message.echo: return
        await self.handle_commands(message)

    @commands.command()
    async def p(self, ctx: commands.Context):
        item_name = ctx.message.content.removeprefix('%sp ' % COMMAND_PREFIX)
        item_data = await fetchItemData(item_name)
        if item_data == False:
            await ctx.send(f'Unable to fetch price of {item_name}.')
        else:
            await ctx.send(f'The last low price of {item_data['normalizedName']} was {item_data['lastLowPrice']} roubles.')


bot = Bot()
bot.run()
