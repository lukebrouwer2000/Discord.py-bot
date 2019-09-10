@client.event
async def on_message_delete(message):
    """creates an embed when a message is deleted in the channel"""
    
    client.get_channel(620010049422753812)                                                          # post embed in specific channel
    embed = discord.Embed()
    embed.set_author(name=message.author, icon_url=message.author.avatar_url)                       # header
    embed.description = message.content  # description
    embed.set_footer(text=f"Message seen in {message.guild.name} in {message.channel.name} | "
                              f"\nYou've been caught by Vive bot")                                  # footer

    if len(message.content) > 0:                                                                    
        embed.description = message.content                                                         # if length of message > 0
    else:
        embed.description = 'No message content'                                                    # all other conditions
  
    await message.channel.send(embed=embed)                                                         # prints embed in channel
