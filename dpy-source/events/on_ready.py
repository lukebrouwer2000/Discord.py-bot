@client.event
async def on_ready():
    """shows the bot's status as online, playing xyz game"""
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game("Battlefield IV"))

    print(f'{client.user.name} is ready for action :)')
