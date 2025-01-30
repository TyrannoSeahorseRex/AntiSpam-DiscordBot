import discord
from discord import app_commands
from discord.ext import tasks
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
