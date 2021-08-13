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


class Give(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Give is working.')

    @commands.command()
    async def give(self, ctx, member: discord.Member, *, money=0):
        if money < 0:
          await ctx.send("Tiền không thể là số âm!")
          return
        with open("./bank.json", "r") as f:
            users = json.load(f)
            
        if not str(member.id) in users:
          users[str(member.id)] = {}
          users[str(member.id)]['wallet'] = 0
          users[str(member.id)]['totalbet'] = 0

        money = abs(money)
        if users[str(ctx.author.id)]['wallet'] >= money:
            users[str(ctx.author.id)]['wallet'] -= money
            users[str(member.id)]['wallet'] += money
            embed = discord.Embed(title='ĐƠN CHUYỂN TIỀN',
                                  description='',
                                  colour=discord.Colour.blue())
            embed.add_field(name='Người chuyển:',
                            value=ctx.author.mention,
                            inline=False)
            embed.add_field(name='Người nhận:',
                            value=member.mention,
                            inline=False)
            embed.add_field(name='Số tiền',
                            value=money,
                            inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f'{ctx.author.mention}Lỗi!!!')
        with open("./bank.json", "w") as f:
            json.dump(users, f)


def setup(client):
    client.add_cog(Give(client))
