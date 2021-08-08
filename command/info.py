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

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('Info is working.')

    
    @commands.command()
    async def info(self, ctx, member: discord.Member = 'None'):
        guild = ctx.guild
        if member == 'None':
            member = ctx.author
        if discord.utils.get(guild.roles, id=roles.kp) in member.roles:
            role = 'Cố vấn'
        elif discord.utils.get(guild.roles, id=roles.bonkerpp) in member.roles:
            role = 'Thủ tướng'
        elif discord.utils.get(guild.roles, id=roles.bonker) in member.roles:
            role = 'Thẩm phán'
        elif discord.utils.get(guild.roles, id=roles.truongphong) in member.roles:
            role = 'Tham mưu trưởng'
        elif discord.utils.get(guild.roles, id=roles.phophong) in member.roles:
            role = 'Phó tham mưu trưởng'
        elif discord.utils.get(guild.roles, id=roles.botrole) in member.roles:
            role = 'Đặc vụ toàn quyền'
        elif discord.utils.get(guild.roles, id=roles.suimem) in member.roles:
            role = 'Thanh tra đặc biệt'
        elif discord.utils.get(guild.roles, id=roles.viprole) in member.roles:
            role = 'Thanh tra'
        elif discord.utils.get(guild.roles, id=roles.godofsui) in member.roles:
            role = 'Điều tra viên cấp cao'
        elif discord.utils.get(guild.roles, id=roles.suixuyenvutru) in member.roles:
            role = 'Điều tra viên cấp cao'
        elif discord.utils.get(guild.roles, id=roles.suidividoichophep) in member.roles:
            role = 'Điều tra viên'
        elif discord.utils.get(guild.roles, id=roles.suitrieunam) in member.roles:
            role = 'Điều tra viên'
        elif discord.utils.get(guild.roles, id=roles.vanvatdieusui) in member.roles:
            role = 'Đặc vụ'
        elif discord.utils.get(guild.roles, id=roles.canbosui) in member.roles:
            role = 'Đặc vụ'
        else:
            role = 'Nhân viên thường'

        embed = discord.Embed(title='Tên nhân viên:',
                              description=member.mention,
                              colour=discord.Colour.blue())
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name='Chức vụ:', value=role, inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Info(client))