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

class Roll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('Roll is working.')
      
    @commands.command()
    async def roll(self,ctx, choose = '', bet = 0):
      if choose == 'red' or choose == 'blue' or choose == 'green':
        if bet == 0:
          await ctx.send('Vui lòng nhập số tiền!!')
          return
        with open("./bank.json","r") as f:
          users = json.load(f)
        if not str(ctx.author.id) in users:
          users[str(ctx.author.id)] = {}
          users[str(ctx.author.id)]['wallet'] = 0
        wallet = users[str(ctx.author.id)]['wallet']
        if wallet >= bet:
          deal = random.randint(0,30)
          if deal == 0:
            deal = 'green'
          elif deal % 2 == 0:
            deal = 'blue'
          elif deal % 2 == 1:
            deal = 'red'
          if choose == deal and deal != 'green':
            desc = f'{ctx.author.mention} đã ăn {bet*2}!!'
            bet = bet
          elif choose == deal and deal == 'green':
            desc = f'{ctx.author.mention} đã ăn {bet*18}!!'
            bet = bet*17
          else:
            desc = f'{ctx.author.mention} đã thua {bet}!!'
            bet=-bet
          if deal == 'blue':
            deal = '🔵'
          elif deal == 'red':
            deal = '🔴'
          elif deal == 'green':
            deal = '🟢'
          if choose == 'blue':
            choose = '🔵'
          elif choose == 'red':
            choose = '🔴'
          elif choose == 'green':
            choose = '🟢'
          users[str(ctx.author.id)]['wallet'] += bet
          wallet = users[str(ctx.author.id)]['wallet']
          embed = discord.Embed(title='Roll',
                                description=desc,
                                colour=discord.Colour.blue())
          embed.add_field(name='Nhà cái:', value=deal, inline=True)
          embed.add_field(name='Bạn:', value=choose, inline=True)
          embed.add_field(name='Số tiền còn lại của bạn:', value=wallet, inline=False)
          await ctx.send(embed=embed)
        else:
          await ctx.send('Bạn không đủ tiền!!!')
        with open("./bank.json","w") as f:
          json.dump(users, f)
      
def setup(client):
    client.add_cog(Roll(client))