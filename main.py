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
