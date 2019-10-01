import discord
import os
from discord.ext import commands
import time
import asyncio
import random
import schedule

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    """shows the bot's status as online, playing xyz game"""
    start = time.time()
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Candy Crush"))
    end = time.time()
    print(f'{client.user.name} is ready for action. Start-up took {end-start} seconds')


@client.event
async def on_member_join(member):
    """adds a welcome message when a new user joins the server"""
    for _ in member.guild.channels:
            print(f'{member} has joined the server.')
            await member.send(f'{member} has joined the server!')
            await member.send_message(f'Welcome to the server!')


@client.event
async def on_member_remove(member):
    """adds a goodbye message when an existing user leaves the server"""
    print(f'{member} has left the server.')
    await member.send(f'{member} has left the server!')


@client.event
async def on_message_delete(message):
    """creates an embed when a message is deleted in the channel"""
    
    embed = discord.Embed()
    embed.set_author(name=message.author, icon_url=message.author.avatar_url)  
    embed.description = message.content  

    embed.set_footer(text=f'Message seen in {message.guild.name} in {message.channel.name} | '
                        f"\nYou've been caught by Vive bot")

    if len(message.content) > 0:
        embed.description = message.content
    else:
        embed.description = 'No message content'

    await message.channel.send(embed=embed)



@client.command()
@commands.has_role("Admin")
async def ctc(ctx, name):
    """allows user to create text channels on the discord server"""
    guild = ctx.message.guild
    await guild.create_text_channel(name)
    await ctx.send('I created a text channel with the name: ' + name)
    
@client.command()
@commands.has_role("Admin")
async def delete(ctx, reason=None):       
    """allows admin user to delete channels on the discord server"""

    channel = ctx.channel
    await channel.delete(reason=reason) 

class MemberRoles(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return [role.name for role in member.roles[1:]]

@client.command()
@commands.has_role("Admin")
async def roles(ctx, *, roles: MemberRoles):
    """tells you a member's roles"""
    await ctx.send('User has the following roles: ' + ', '.join(roles))



@client.command()
async def ping(ctx):
    """allows user to verify ping associated with discord server"""
    allowable_channels = ["general"]
    if str(ctx.channel) in allowable_channels:
        await ctx.send(f'Pong! Your ping to discord servers :  {round(client.latency * 1000)}ms')


@client.command()
@commands.has_role("Admin")
@commands.is_owner()
async def clear(ctx, amount=5000): # default value set to 5k automatically
    """clears all messages in chat based on amount=value"""
    allowable_channels = ["general", "todo", "development"]
    if str(ctx.channel) in allowable_channels:
        start_time = time.time()
        purge_count = await ctx.channel.purge(limit=amount)
        end_time = time.time()

        await ctx.channel.send(f'Deleted {len(purge_count)} messages in channel {ctx.channel.mention}')
        await ctx.channel.send(f'Purge took {(end_time - start_time):0.2f} seconds')  # execution time rounded to 2 places, works w/ float
        message = await ctx.channel.send("While this channel is labeled as NSFW breaking discord's Terms of Services (<https://discordapp.com/terms>) will not be allowed.")
        await message.pin()







@client.command()
@commands.is_owner()
@commands.has_role("Admin")
async def kick(ctx, member: discord.Member, *, reason=None):  # reason = none for easy kicking; no context
    """allows admin users to kick other members while providing reason"""
    # reason = none exception handling
    if reason is None:  
        
        await member.send(f'Dear {member}, \nYou were auto-kicked from the server {ctx.guild.name}. Lata bitch')

    else:  
        await ctx.channel.send(f'{member} was kicked from the server.')

        await member.send(f'Dear {member}: \nYou were kicked from the server, ' \
                      f'{ctx.guild.name}, \n\nReason: {reason}.')
        await member.kick(reason=reason)


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


# @client.command()
# async def ban(ctx, member: discord.Member, *, reason=None):  # reason = none for easy banning; no context
#     await member.ban(reason=reason)

# @client.command()
# async def purge(ctx, amount=5000):
#     """clears all links and images"""
#     my_channel = ctx.message.channel
#     messages = []
#     for message in ctx.history(my_channel, limit=int(amount)):
#         messages.append(message)
#     await ctx.message.delete(messages)
#     await ctx.my_channel.send('Bad links and images deleted!')

ident = client.get_guild(616811413268070415)
client.run('NjE3MTIwNDkxMDUxOTQxOTI4.XYmYYA.WPMzFDoqcXMBp-STF2ZvzMd3hL4')



# @client.event
# async def embed_errors(message):
#     exception = discord.DiscordException()
#     embed = discord.Embed()
#
#     exception.text = embed.description
#
#     embed.set_author(name=message.author, icon_url=message.author.avatar_url)
#     embed.description = message.content
