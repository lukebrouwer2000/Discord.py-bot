@client.event
async def on_member_join(member):
    """adds a welcome message when a new user joins the server"""
    for channel in member.guild.channels:
        if str(channel) == "general":
            print(f'{member} has joined the server.')
            await member.send(f'{member} has joined the server!')            # prints in the console
            await member.send_message(f'Welcome to the server!')             # prints in the guild chat
