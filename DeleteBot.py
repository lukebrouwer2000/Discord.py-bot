import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")                                        #  variable name extends to decorators and functions; 


@client.event
async def on_ready():
    """shows the bot's status as online, playing xyz game"""
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game
                                 ("World of Warcraft: Classic"))

    print(f'{client.user.name} is ready for action :)')


@client.event
async def on_member_join(member):
    """adds a welcome message when a new user joins the server"""
    print(f'{member} has joined a server.')                                       #  f strings because .format is outdated


@client.event
async def on_member_remove(member):
    """adds a goodbye message when an existing user leaves the server"""
    print(f'{member} has left a server.')                                        #  f strings because .format is outdated


@client.command()
async def ping(ctx):
    """allows user to verify ping associated with discord server"""
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def clear(ctx, amount=0):                                                 #  change amount to purge size desired
    """clears all messages in chat based on amount=value"""
    await ctx.channel.purge(limit=amount)


@client.event
async def on_message_delete(message):
    """creates an embed when a message is deleted in the channel """
    client.get_channel(616811413847146498)

    embed = discord.Embed(description=message.content)                          #  allows attribute of set_author/set_footer

    embed.set_author(name=message.author, icon_url=message.author.avatar_url)

    embed.set_footer(text=message.channel.name)

    if len(message.content) > 0:                                                #  in case message description has nothing
        embed.description = message.content
    else:
        embed.description = 'No message content'

    await message.channel.send(embed=embed)


client.run('insert bot token here')
