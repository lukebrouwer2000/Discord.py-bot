# Discord.py-bot
Discord bot made in Python using the extensive Discord.py library.

Includes events and commands

Events - 
1. on_ready - when the user runs the code, shows the bot's status as online, playing xyz game

2. on_member_join - adds a welcome message when a new user joins the server

3. on_member_remove - adds a goodbye message when an existing user leaves the server

4. on_message_delete - creates an embed when a message is deleted in the channel



Commands - 
1. ping - allows user to verify ping associated with discord server

2. clear - clears all messages in chat based on amount=value

3. kick - allows admin users to kick other members while providing reason (includes reason/no-reason handlind)

4. ban - allows admin users to ban other members while providing reason (includes reason/no-reason handlind)

5. ctc(create_text_channel) - allows users with proper permissions to create text channels

6. dtc(delete_channel) - allows admin user to delete channel



TO:DO

• Add cogs and classes to organize events and commands 

• Finish hosting to ensure bot uptime of 100%

• Refactor execution time module - switch from time to timeit
