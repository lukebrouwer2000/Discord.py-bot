@client.command()
@commands.has_role("bigpapa")
async def ban(ctx, member: discord.Member, *, reason=None):
    """allows admin users to ban other members while providing reason"""
    if reason is None:  # reason = none handling
        await ctx.channel.send(f'{member} was banned from the server.')  # declares user was banned in text channel
        
        none_embed = discord.Embed()
        ctx.content = f'Dear {member}, \n you recently used an unacceptable word in the server {ctx.guild.name}.' \
                      f' Due to this infraction, you have been banned. Rest in pieces, {member}. Such a woefully ' \
                      f'short life.'
        none_embed.description = ctx.content
        
        await member.send(embed=none_embed)

    else:  # if reason is stated
    
        await ctx.channel.send(f'{member} was banned from the server.')  # prints to guild channel before ban
        
        embed = discord.Embed()
        ctx.content = f'Dear {member}, \n you were kicked from the server because of these reasons :' \
                      f'\n {reason}'
        embed.description = ctx.content
        
        await member.send(embed=embed)
        await member.ban(reason=reason)
