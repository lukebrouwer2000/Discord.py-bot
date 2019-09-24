@client.event
async def on_ready():
    """shows the bot's status as online, playing xyz game"""
    start = time.time()
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Battlefield IV"))
    end = time.time()
    print(f'{client.user.name} is ready for action. Start-up took {end-start} seconds')
