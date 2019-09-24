@client.command()
@commands.has_role(role)
async def kick(ctx, member: discord.Member, *, reason=None):  # reason = none for easy execution; no context
    """allows admin users to kick other members while providing reason"""
    
    if reason is None:  # reason = none handling
    
        none_embed = discord.Embed()
        ctx.content = f'Dear {member}, \n You were kicked from the server {ctx.guild.name} because y____________.'
        none_embed.description = ctx.content
        
        await member.send(embed=none_embed)
        
    else:  # if reason is stated
        await ctx.channel.send(f'{member} was kicked from the server.')
        
        embed = discord.Embed()
        ctx.content = f'Dear {member}: \nYou were kicked from the server, ' \
                      f'{ctx.guild.name}, because: {reason}.'
        embed.description = ctx.content
        
        await member.send(embed=embed)
        await member.kick(reason=reason)
