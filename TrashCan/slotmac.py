import discord
import os
import random
import asyncio
import roles
import channels
import members
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions
from discord.ext.commands import CheckFailure
from host import host
from replit import db

class Slotmac(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('Slotmac is working.')

    
    @commands.command()
    async def slotmac(self,ctx):
      with open("./bank.json","r") as f:
          users = json.load(f)
      earn = rando
      users[str(member.id)]['wallet'] += int(earn)


      with open("./bank.json","w") as f:
        json.dump(users, f)

def setup(client):
    client.add_cog(Slotmac(client))