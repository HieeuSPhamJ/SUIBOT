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


class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('Ban is working.')

    
    @commands.command()
    @has_permissions(kick_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason='None'):
        await ctx.send(f"{member.mention}, Bạn đã bị loại bỏ khỏi đa vũ trụ!!!")
        await member.ban(reason=reason)
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            await ctx.send("Tôi chỉ nghe lệnh từ cấp trên!")
    

def setup(client):
    client.add_cog(Ban(client))