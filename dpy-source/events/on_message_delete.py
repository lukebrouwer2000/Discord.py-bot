@client.event
async def on_message_delete(message):
    """creates an embed when a message is deleted in the channel"""

    bad_send = client.get_channel(628755221266563072)
    regular_send = client.get_channel(628758306042675200)

    embed = discord.Embed()
    embed.set_author(name=message.author, icon_url=message.author.avatar_url)  
    embed.description = message.content  
    embed.set_footer(text=f'Message seen in {message.guild.name} in {message.channel.name} | '
                        f"\nYou've been caught by Vive bot")

    if len(message.content) > 0:
        embed.description = message.content
    else:
        embed.description = 'No message content'

    bad_word = ''
    if bad_word in message.content:
        await bad_send.send(embed=embed)
    else: 
        await regular_send.send(embed=embed)
