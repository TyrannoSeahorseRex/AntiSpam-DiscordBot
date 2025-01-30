import discord
from discord import app_commands
from datetime import datetime, timedelta

## CLIENT AND CUSTOM CHANGING STATUS

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False
        self.message_count = {}  # Track message counts
        self.timeout_users = set()  # Track users who are timed out

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"We have logged in as User: {self.user}. ID: {self.user.id}.")

client = aclient()
tree = app_commands.CommandTree(client)

## ANTI-SPAM

@client.event
async def on_message(message):
    if isinstance(message.channel, discord.TextChannel) and not message.author.bot:
        user_id = message.author.id
        current_time = datetime.now()

        # Initialize message count and timestamp if not present
        if user_id not in client.message_count:
            client.message_count[user_id] = {'count': 0, 'timestamp': current_time}

        # Check if 60 seconds have passed since the last message
        if (current_time - client.message_count[user_id]['timestamp']).seconds >= 60:
            client.message_count[user_id] = {'count': 1, 'timestamp': current_time}
        else:
            client.message_count[user_id]['count'] += 1

        # Anti-spam check
        if client.message_count[user_id]['count'] > 5:
            await message.delete()
            await message.channel.send(f"{message.author.mention}, don't spam!", delete_after=10)

            if user_id not in client.timeout_users:
                client.timeout_users.add(user_id)
                await message.author.timeout(timedelta(minutes=10), reason="Spamming")
                try:
                    await message.author.send("You have been muted for spamming!")
                    await message.author.send("https://tenor.com/view/yellow-emoji-no-no-emotiguy-no-no-no-gif-gif-9742000569423889376")
                except Exception as e:
                    print(f"Failed to send DM: {e}")

# RUN

TOKEN = 'ENTER_TOKEN_HERE'
client.run(TOKEN)
