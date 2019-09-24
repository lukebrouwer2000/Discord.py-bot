@client.command()
@commands.has_role(role)
async def clear(ctx, amount=5000):
    """clears all messages in chat based on amount=value"""
    start_time = time.time()                                                    # execution timer start
    purge_count = await ctx.channel.purge(limit=amount)                         # purge code to run
    end_time = time.time()                                                      # execution timer stop

    await ctx.channel.send('Deleted {} messages in channel {}'                  
                           .format(len(purge_count), ctx.channel.mention))
    await ctx.channel.send('Purge took {0:0.1f} seconds'
                           .format(end_time - start_time))
