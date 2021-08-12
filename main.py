import discord
import os
import random
import asyncio
import variable
import test
import json
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions
from discord.ext.commands import CheckFailure
from host import host
from replit import db

client = commands.Bot(command_prefix='s+')
client.remove_command('help')

for filename in os.listdir('./Mod_command'):
  if filename.endswith('.py'):
    client.load_extension(f'Mod_command.{filename[:-3]}')
for filename in os.listdir('./EconomyAndGamble'):
  if filename.endswith('.py'):
    client.load_extension(f'EconomyAndGamble.{filename[:-3]}')





host()
client.run(os.environ['token'])
