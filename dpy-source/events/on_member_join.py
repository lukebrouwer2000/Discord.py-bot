@client.event
async def on_member_join(member):
    """adds a welcome message when a new user joins the server"""
    print(f'{member} has joined a server.')                           # prints in the console
    await member.send(f'{member} has joined the server!')             # prints in the guild chat
