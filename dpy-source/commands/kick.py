@client.command()
@commands.is_owner()
@commands.has_role("Admin")
async def kick(ctx, member: discord.Member, *, reason=None):  # reason = none for easy kicking; no context
    """allows admin users to kick other members while providing reason"""
    # reason = none exception handling
    if reason is None:  
        none_embed = discord.Embed()
        ctx.content = f'Dear {member}, \n You were kicked from the server {ctx.guild.name} because ...'
        none_embed.description = ctx.content
        await member.send(embed=none_embed)

    else:  
        await ctx.channel.send(f'{member} was kicked from the server.')

        embed = discord.Embed()
        ctx.content = f'Dear {member}: \nYou were kicked from the server, ' \
                      f'{ctx.guild.name}, because: {reason}.'
        embed.description = ctx.content

        await member.send(embed=embed)
        await member.kick(reason=reason)
