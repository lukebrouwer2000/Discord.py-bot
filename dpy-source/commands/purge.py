@client.command()
@commands.has_role(role)
async def clear(ctx, amount=5000):
    """clears all messages in chat based on amount=value"""
    allowable_channels = [channels]
    
    if str(ctx.channel) in allowable_channels:
        start_time = time.time()
        purge_count = await ctx.channel.purge(limit=amount)
        end_time = time.time()

        await ctx.channel.send(f'Deleted {len(purge_count)} messages in channel {ctx.channel.mention}')
        await ctx.channel.send(f'Purge took {(end_time - start_time):0.2f} seconds')  # execution time rounded to 2 places, works w/ float
