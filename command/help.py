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

class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('Help is working.')

    
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='HƯỚNG DẪN CỦA S.U.I',
                              description='',
                              colour=discord.Colour.blue())
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.add_field(name='s+ping', value='Gọi cho tôi', inline=False)
        embed.add_field(name='s+kick <đối tượng>',
                        value='Đá ai đó ra khỏi server',
                        inline=False)
        embed.add_field(name='s+ban <đối tượng>',
                        value='Đá ai đó ra khỏi server nhưng là vĩnh viễn',
                        inline=False)
        embed.add_field(
            name='s+mute <đối tượng> <thời gian> <lý do>',
            value='Nhốt ai đó vào tù (nếu không có thời gian sẽ là vĩnh viễn)',
            inline=False)
        embed.add_field(name='s+unmute <đối tượng>',
                        value='Ân xá cho tù nhân',
                        inline=False)
        embed.add_field(
            name='s+info <đối tượng>',
            value=
            'Kiểm tra thẻ nhân viên của tổ chức Secret Universe Investigation Organization',
            inline=False)
        embed.add_field(
            name='s+vanmau <đối tượng>',
            value=
            'Văn mẫu tất nhiên rồi!',
            inline=False)

        await ctx.send(embed=embed)
    

def setup(client):
    client.add_cog(Kick(client))