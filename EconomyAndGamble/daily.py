import discord
import os
import random
import asyncio
import roles
import channels
import members
import json
import datetime
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions
from discord.ext.commands import CheckFailure
from discord.ext.commands.cooldowns import BucketType
from host import host
from replit import db

now = datetime.datetime.now()

class Daily(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('Daily is working.')

    @commands.Cog.listener()
    async def on_message(self, message):
      with open("./bank.json","r") as f:
          users = json.load(f)

      if not str(message.author.id) in users:
          users[str(message.author.id)] = {}
          users[str(message.author.id)]["wallet"] = 0
          users[str(message.author.id)]['totalbet'] = 0

      users[str(message.author.id)]["wallet"] += random.randint(1,10)

      with open("./bank.json","w") as f:
          json.dump(users, f)

    @commands.command()
    async def daily(self,ctx):
        with open("./timetoearn.json","r") as f:
          userstime = json.load(f)
        with open("./bank.json","r") as f:
          users = json.load(f)

        if not str(ctx.author.id) in userstime:
          userstime[str(ctx.author.id)] = {}
          userstime[str(ctx.author.id)]['time'] = 0
        if not str(ctx.author.id) in users:
          users[str(ctx.author.id)] = {}
          users[str(ctx.author.id)]["wallet"] = 0
          users[str(ctx.author.id)]['totalbet'] = 0

        if userstime[str(ctx.author.id)]["time"] != now.day:
          earn = random.randint(10,1000)
          await ctx.send(f'{ctx.author.mention} đã nhận được {earn}!!!')
          users[str(ctx.author.id)]["wallet"] += earn
          userstime[str(ctx.author.id)]['time'] = now.day
        else:
          await ctx.send('Bạn đã nhận rồi!!')

        with open("./bank.json","w") as f:
          json.dump(users, f)
        with open("./timetoearn.json","w") as f:
          json.dump(userstime, f)
    


    @commands.command()
    @has_permissions(kick_members=True)
    async def resetdaily(self,ctx):
      with open("./timetoearn.json","r") as f:
          userstime = json.load(f)
      for i in userstime:
          userstime[str(i)]['time'] = 0
      with open("./timetoearn.json","w") as f:
          json.dump(userstime, f)
      await ctx.send('Đã reset')
    
def setup(client):
    client.add_cog(Daily(client))