@client.command()
@commands.is_owner()
@commands.has_role("Admin")
async def ban(ctx, member: discord.Member, *, reason=None):
    """allows admin users to ban other members while providing reason"""
    if reason is None:  # reason = none handling

        # declares user was banned in text channel
        await ctx.channel.send(f"{member} was banned from the server. Don't be like {member.name}")  

        none_embed = discord.Embed()
        ctx.content = (f'Dear {member}, \n Recently, you used an unacceptable word or did some dumb shit' \
                      f' in the server {ctx.guild.name}.' \
                      f' Due to this infraction, you have been banned. Rip broh')
        none_embed.description = ctx.content
        await member.send(embed=none_embed)

    else:  # if reason is stated
        await ctx.channel.send(f"{member} was banned from the server. Don't be like {member}")
        embed = discord.Embed()
        ctx.content = f'Dear {member}, \n you were kicked from the server because of these reasons :' \
                      f'\n {reason}'
        embed.description = ctx.content
        await member.send(embed=embed)
        await member.ban(reason=reason)
