@client.command()
@commands.has_role("Admin")
@commands.is_owner()
async def clear(ctx, amount=5000): # default value set to 5k automatically
    """clears all messages in chat based on amount=value"""
    channel_send = client.get_channel(628749903220310016)
    allowable_channels = ["general", "todo", "development"]

    today = date.today()

    day = today.strftime("%B %d, %Y")

    if str(ctx.channel) in allowable_channels:
        start_time = time.time()
        purge_count = await ctx.channel.purge(limit=amount)
        end_time = time.time()

        await channel_send.send(f'Scheduled purge deleted {len(purge_count)} messages in channel {ctx.channel.mention}. \nPurge took {(end_time - start_time):0.2f} seconds. \nToday\'s date: {day}')
        
        message = await ctx.channel.send("While this channel is labeled as NSFW breaking discord's Terms of Services (<https://discordapp.com/terms>) will not be allowed.")
        await message.pin()
