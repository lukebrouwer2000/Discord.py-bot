import discord
import os
from discord.ext import commands
import time

client = commands.Bot(command_prefix="!")



@client.event
async def on_ready():
    """shows the bot's status as online, playing xyz game"""
    start = time.time()
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Battlefield IV"))
    end = time.time()
    print(f'{client.user.name} is ready for action. Start-up took {end-start} seconds')


@client.event
async def on_member_join(member):
    """adds a welcome message when a new user joins the server"""
    for channel in member.guild.channels:
        if str(channel) == "general":
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

@client.command()
async def ping(ctx):
    """allows user to verify ping associated with discord server"""
    allowable_channels = ["general"]
    if str(ctx.channel) in allowable_channels:
        await ctx.send(f'Pong! Your ping to discord servers :  {round(client.latency * 1000)}ms')


@client.command()
@commands.has_role(role)
async def clear(ctx, amount=5000):
    """clears all messages in chat based on amount=value"""
    allowable_channels = ["general", "todo"]
    if str(ctx.channel) in allowable_channels:
        start_time = time.time()
        purge_count = await ctx.channel.purge(limit=amount)
        end_time = time.time()

        await ctx.channel.send('Deleted {} messages in channel {}'
                               .format(len(purge_count), ctx.channel.mention))
        await ctx.channel.send('Purge took {0:0.1f} seconds'
                               .format(end_time - start_time))


@client.command()
@commands.has_role(role)
async def kick(ctx, member: discord.Member, *, reason=None):  # reason = none for easy kicking; no context
    """allows admin users to kick other members while providing reason"""
    if reason is None:  # reason = none handling
        none_embed = discord.Embed()
        ctx.content = f'Dear {member}, \n You were kicked from the server {ctx.guild.name} because you were a dickhead.'
        none_embed.description = ctx.content
        await member.send(embed=none_embed)

    else:  # if reason is stated
        await ctx.channel.send(f'{member} was kicked from the server.')

        embed = discord.Embed()
        ctx.content = f'Dear {member}: \nYou were kicked from the server, ' \
                      f'{ctx.guild.name}, because: {reason}.'
        embed.description = ctx.content

        await member.send(embed=embed)
        # await member.kick(reason=reason)


@client.command()
@commands.has_role(role)
async def ban(ctx, member: discord.Member, *, reason=None):
    """allows admin users to ban other members while providing reason"""
    if reason is None:  # reason = none handling
        await ctx.channel.send(f"{member} was banned from the server. Don't be like {member.name}")  # declares user was
        # banned in text channel

        none_embed = discord.Embed()
        ctx.content = f'Dear {member}, \n you recently used an unacceptable word or did some dumb shit' \
                      f' in the server {ctx.guild.name}.' \
                      f' Due to this infraction, you have been banned. Rest in pieces, {member}. Such a woefully ' \
                      f'short life.'
        none_embed.description = ctx.content
        await member.send(embed=none_embed)

    else:  # if reason is stated
        await ctx.channel.send(f"{member} was banned from the server. Don't be like {member}")
        embed = discord.Embed()
        ctx.content = f'Dear {member}, \n you were kicked from the server because of these reasons :' \
                      f'\n {reason}'
        embed.description = ctx.content
        await member.send(embed=embed)
        #  await member.ban(reason=reason)


# @client.command()
# async def ban(ctx, member: discord.Member, *, reason=None):  # reason = none for easy banning; no context
#     await member.ban(reason=reason)


ident = client.get_guild(server_id)
client.run(token)

# @client.command()
# async def clear2(ctx, amount=5000):
#     """clears all links and images"""
#     my_channel = ctx.message.channel
#     messages = []
#     for message in client.history(my_channel, limit=int(amount)):
#         messages.append(message)
#     await ctx.message.delete(messages)
#     await ctx.my_channel.send('Bad links and images deleted!')


# @client.event
# async def embed_errors(message):
#     exception = discord.DiscordException()
#     embed = discord.Embed()
#
#     exception.text = embed.description
#
#     embed.set_author(name=message.author, icon_url=message.author.avatar_url)
#     embed.description = message.content
