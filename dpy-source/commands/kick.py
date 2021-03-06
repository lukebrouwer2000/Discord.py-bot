@client.command()
@commands.is_owner()
@commands.has_role("Admin")
async def kick(ctx, member: discord.Member, *, reason=None):  # reason = none for easy kicking; no context
    """allows admin users to kick other members while providing reason"""
    # reason = none exception handling
    if reason is None:  
        
        await member.send(f'Dear {member}, \nYou were kicked from the server {ctx.guild.name}. Lata bitch')

    else:  
        await ctx.channel.send(f'{member} was kicked from the server.')

        await member.send(f'Dear {member}: \nYou were kicked from the server, ' \
                      f'{ctx.guild.name}, \n\nReason: {reason}.')
        await member.kick(reason=reason)
