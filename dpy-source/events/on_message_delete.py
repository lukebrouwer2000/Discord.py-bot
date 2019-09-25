@client.event
async def on_message_delete(message):
    """creates an embed when a message is deleted in the channel"""
                                                           
    embed = discord.Embed()
    embed.set_author(name=message.author, icon_url=message.author.avatar_url)                       
    embed.set_footer(text=f"Message seen in {message.guild.name} in {message.channel.name} | "
                              f"\nYou've been caught by Vive bot")                                  

    if len(message.content) > 0:                                                                    
        embed.description = message.content                                                         
    else:
        embed.description = 'No message content'                                                    
  
    await message.channel.send(embed=embed) # prints embed in channel
