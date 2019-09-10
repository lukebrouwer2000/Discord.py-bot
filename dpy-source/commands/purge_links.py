@client.command()
async def clear2(ctx, amount=5000):
    """clears all links and images"""
    my_channel = ctx.message.channel
    messages = []
    for message in client.history(my_channel, limit=int(amount)):
        messages.append(message)
    await ctx.message.delete(messages)
    await ctx.my_channel.send('Bad links and images deleted!')
