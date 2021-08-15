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


class Addbackground(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Van Mau is working.')

    @commands.command()
    async def addbg(self, ctx, link='None'):
      with open("./background.json","r") as f:
        bgs = json.load(f)
      if not str(ctx.author.id) in bgs:
        await ctx.send('Bạn chưa có quyền để up hay xóa ảnh! (Để up hay xóa ảnh hãy mua ở s+shop)')
        return
        
      if link == 'None':
        await ctx.send('Hãy điền link ảnh!!!')
        return

      bgs[str(ctx.author.id)] = {}
      bgs[str(ctx.author.id)]['background'] = link
      bgs[str(ctx.author.id)]['check'] = 1
      await ctx.send('Đã up ảnh bg xong!!')

      with open("./background.json","w") as f:
        json.dump(bgs, f)


    @commands.command()
    async def removebg(self, ctx):
      with open("./background.json","r") as f:
        bgs = json.load(f)
      if not str(ctx.author.id) in bgs:
        await ctx.send('Bạn chưa có quyền để up hay xóa ảnh! (Để up hay xóa ảnh hãy mua ở s+shop)')
        return

      link = 'https://cdn.discordapp.com/attachments/873964288216289360/876382844145004584/transparent_profilecard.png'

      bgs[str(ctx.author.id)] = {}
      bgs[str(ctx.author.id)]['background'] = link
      bgs[str(ctx.author.id)]['check'] = 1
      await ctx.send('Đã xóa ảnh bg xong!!')

      with open("./background.json","w") as f:
        json.dump(bgs, f)
      

    


def setup(client):
    client.add_cog(Addbackground(client))
