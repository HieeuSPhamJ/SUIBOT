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


class SPD(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('SPD is working.')

    
    @commands.command()
    @has_permissions(kick_members=True)
    async def spd(self, ctx, *args):
      mess = ctx.message
      await mess.delete()
      await ctx.send(file=discord.File('./file/spd.jpg'))

def setup(client):
    client.add_cog(SPD(client))