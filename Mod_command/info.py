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
        elif discord.utils.get(guild.roles, id=roles.namdausv) in member.roles:
            role = 'Tổng thống S.U.I'
        elif discord.utils.get(guild.roles, id=roles.bonkerpp) in member.roles:
            role = 'Thủ tướng'
        elif discord.utils.get(guild.roles, id=roles.bonker) in member.roles:
            role = 'Thống tướng'
        elif discord.utils.get(guild.roles, id=roles.truongphong) in member.roles:
            role = 'Đại tướng'
        elif discord.utils.get(guild.roles, id=roles.phophong) in member.roles:
            role = 'Trung tướng'
        elif discord.utils.get(guild.roles, id=roles.botrole) in member.roles:
            role = 'Thiếu tướng'
        elif discord.utils.get(guild.roles, id=roles.suimem) in member.roles:
            role = 'Đại tá'
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
        
        
        with open("./bank.json","r") as f:
          users = json.load(f)
        if not str(member.id) in users:
          users[str(member.id)] = {}
          users[str(member.id)]['wallet'] = 0

        wallet = users[str(member.id)]['wallet']

        embed = discord.Embed(title='Tên nhân viên:',
                              description=member.mention,
                              colour=discord.Colour.blue())
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name='Chức vụ:', value=role, inline=False)
        embed.add_field(name='Tiền còn lại:', value=wallet, inline=False)

        await ctx.send(embed=embed)

        with open("./bank.json","w") as f:
          json.dump(users, f)


def setup(client):
    client.add_cog(Info(client))