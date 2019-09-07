import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix=".")


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.event
async def on_ready():
    """shows the bot's status as online, playing xyz game"""
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game("World of Warcraft: Classic"))

    print('{0.user} is ready for action :)'.format(client))


@client.event
async def on_member_join(member):
    """adds a welcome message when a new user joins the server"""
    print(f'{member} has joined a server.')


@client.event
async def on_member_remove(member):
    """adds a goodbye message when an existing user leaves the server"""
    print(f'{member} has left a server.')


@client.command()
async def ping(ctx):
    """allows user to verify ping associated with discord server"""
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def clear(ctx, amount=5000):
    """clears all messages in chat based on amount=value"""
    await ctx.channel.purge(limit=amount)


@client.event
async def on_message_delete(message):
    """creates an embed when a message is deleted in the channel """
    client.get_channel(616811413847146498)

    embed = discord.Embed(description=message.content)

    embed.set_author(name=message.author, icon_url=message.author.avatar_url)

    embed.set_footer(text=message.channel.name)

    if len(message.content) > 0:
        embed.description = message.content
    else:
        embed.description = 'No message content'

    await message.channel.send(embed=embed)


client.run('NjE3MTIwNDkxMDUxOTQxOTI4.XXM-EA.3Apx0FUPszYcXt6OVXSfjNE3TrQ')
