import discord
import os
import random
import asyncio
import roles
import channels
import members
import json
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions
from discord.ext.commands import CheckFailure
from host import host
from replit import db

class Add(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('Add is working.')

    
    @commands.command()
    @has_permissions(kick_members=True)
    async def add(self, ctx, member: discord.Member,*,wallet = 0):
        if wallet < 0:
          await ctx.send("Tiền không thể là số âm!")
          return
        with open("./bank.json","r") as f:
          users = json.load(f)
        if not str(member.id) in users:
          users[str(member.id)] = {}
          users[str(member.id)]['wallet'] = 0
          
        users[str(member.id)]['wallet'] += int(wallet)
        with open("./bank.json","w") as f:
          json.dump(users, f)
        await ctx.send(f'Thêm {wallet} vào tài khoản của {member.mention}')
    @add.error
    async def add_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            await ctx.send("Tôi chỉ nghe lệnh từ cấp trên!")
def setup(client):
    client.add_cog(Add(client))