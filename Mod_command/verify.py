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


class Verify(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Verify is working.')

    @commands.command()
    async def verify(self, ctx):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, id=roles.checkrole)
        await ctx.author.add_roles(role)
        channel = self.client.get_channel(channels.chung)
        await channel.send(
            f'''Rạp xiếc trung ương Sủiteam xin chào đón bạn {ctx.author.mention}
  Ở Sủiteam bạn có thể:
  + 1p mới vô, bạn sẽ biến thành gay (?)
  + BẠn sẽ gặp đội ngũ dịch giả kiến thức thì ít mà tấu hài bằng gg dịch là nhiều
  + Nơi trú ẩn của các teito, winner ẩn danh.
  + Giao lưu cùng Sủi trúa, người tiên phong trong việc truyền đạo sủi tới tận nửa kia trái đất.
  + Sv nhiều tài lẻ: làm game, hát hò, hoạ sĩ, buckfoi, vvvv...
  + Lâu lâu nó dảk vãi lone.
  + Cướp waifu như cướp kẹo con nít!
  + Bot nhạc **Đường tôi chở em về** độc quyền: Hoàngkun!
  + Gái không nhiều nhưng chăm online.
  + Gặp gỡ các idol giới trẻ.
  + Tôm chúa, tôm hùm, tôm sông, nói chung là lắm tôm vcl!
  ''')
        await channel.send(file=discord.File('./file/intro.mov'))
        await channel.send(file=discord.File('./file/intro.png'))

def setup(client):
    client.add_cog(Verify(client))
