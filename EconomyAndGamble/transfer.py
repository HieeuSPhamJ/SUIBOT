import discord
import os
import random
import asyncio
import roles
import channels
import members
import json
import tatsu
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions
from discord.ext.commands import CheckFailure
from tatsu.wrapper import ApiWrapper
from host import host
from replit import db


class Transfer(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Give is working.')

    @commands.command()
    async def transfer(self,ctx, member: discord.Member):
      wrapper = ApiWrapper(key=os.environ['token'])
      user_profile = await wrapper.get_profile(member.id)
      await ctx.send(user_profile.id)


def setup(client):
    client.add_cog(Transfer(client))
