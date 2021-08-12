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


class Gamehelp(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @commands.Cog.listener()
    async def on_ready(self):
        print('Gamehelp is working.')

    @commands.command()
    async def gamehelp(self, ctx):
        embed = discord.Embed(title='HƯỚNG DẪN CỦA CÁC MINIGAME',
                              description='',
                              colour=discord.Colour.blue())
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.add_field(name='s+roll <red/blue/green> <tiền>',
                        value='''Red x2
                        Blue x2
                        Green x18''',
                        inline=False)
        embed.add_field(name='s+roulette <tiền>',
                        value='''Chơi cò quay''',
                        inline=False)
        embed.add_field(name='s+add <đối tượng> <tiền>',
                        value='''thêm tiền free?''',
                        inline=False)
        embed.add_field(name='s+give <đối tượng> <tiền>',
                        value='''chuyển tiền''',
                        inline=False)
        embed.add_field(name='s+daily',
                        value='''Nhận tiền free mỗi ngày''',
                        inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Gamehelp(client))
