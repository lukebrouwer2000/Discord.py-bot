import discord
import os
from discord.ext import commands
import time

client = commands.Bot(command_prefix="!")


# @client.command()
# async def load(ctx, extension):
#   client.load_extension(f'cogs.{extension}')


@client.event
async def on_ready():
    """shows the bot's status as online, playing xyz game"""
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game("Battlefield IV"))

    print(f'{client.user.name} is ready for action :)')


@client.event
async def on_member_join(member):
    """adds a welcome message when a new user joins the server"""
    print(f'{member} has joined a server.')
    await member.send(f'{member} has joined the server!')


@client.event
async def on_member_remove(member):
    """adds a goodbye message when an existing user leaves the server"""
    print(f'{member} has left a server.')
    await member.send(f'{member} has left the server!')


@client.event
async def on_message_delete(message):
    """creates an embed when a message is deleted in the channel"""
    #
    client.get_channel(620010049422753812)  # post embed in specific channel
    embed = discord.Embed()
    embed.set_author(name=message.author, icon_url=message.author.avatar_url)  # header
    embed.description = message.content  # description
    embed.set_footer(text='Message seen in '
                          + message.guild.name + " in "
                          + message.channel.name + "\n| \nYou've been caught by Vive bot")  # footer

    if len(message.content) > 0:
        embed.description = message.content
    else:
        embed.description = 'No message content'

    await message.channel.send(embed=embed)


@client.command()
async def ping(ctx):
    """allows user to verify ping associated with discord server"""
    await ctx.send(f'Pong! Your ping to discord servers :  {round(client.latency * 1000)}ms')


@client.command()
async def clear(ctx, amount=5000):
    """clears all messages in chat based on amount=value"""
    start_time = time.time()
    purge_count = await ctx.channel.purge(limit=amount)
    end_time = time.time()

    await ctx.channel.send('Deleted {} messages in channel {}'
                           .format(len(purge_count), ctx.channel.mention))
    await ctx.channel.send('Purge took {0:0.1f} seconds'
                           .format(end_time - start_time))


@client.command()
async def clear2(ctx, amount=5000):
    """clears all links and images"""
    my_channel = ctx.message.channel
    messages = []
    for message in client.history(my_channel, limit=int(amount)):
        messages.append(message)
    await ctx.message.delete(messages)
    await ctx.my_channel.send('Bad links and images deleted!')


# @client.event
# async def embed_errors(message):
#     exception = discord.DiscordException()
#     embed = discord.Embed()
#
#     exception.text = embed.description
#
#     embed.set_author(name=message.author, icon_url=message.author.avatar_url)
#     embed.description = message.content


client.run('NjE3MTIwNDkxMDUxOTQxOTI4.XXNNag.m3jABNznKgas5hTBW4oI3SKTIMY')
