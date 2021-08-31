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


class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('Kick is working.')

    
    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason='None'):
        await ctx.send(f"{member.mention}, Bạn đã bị trục xuất!!!")
        await member.kick(reason=reason)
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            await ctx.send("Tôi chỉ nghe lệnh từ cấp trên!")
    

def setup(client):
    client.add_cog(Kick(client))