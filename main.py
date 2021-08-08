import discord
import os
import random
import asyncio
import variable
import test
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions
from discord.ext.commands import CheckFailure
from host import host
from replit import db

client = commands.Bot(command_prefix='s+')
client.remove_command('help')

for filename in os.listdir('./command'):
  if filename.endswith('.py'):
    client.load_extension(f'command.{filename[:-3]}')



host()
client.run(os.environ['token'])
