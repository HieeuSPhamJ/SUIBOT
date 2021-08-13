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


class Roulette(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Roulette is working.')

    @commands.command()
    async def roulette(self,ctx, bet = 0):
      with open("./bank.json", "r") as f:
        users = json.load(f)
      
      if not str(ctx.author.id) in users:
          users[str(ctx.author.id)] = {}
          users[str(ctx.author.id)]['wallet'] = 0
          users[str(ctx.author.id)]['totalbet'] = 0  

      if bet <= 0:
        await ctx.send('Số tiền không hợp lệ!')
        return

      wallet = users[str(ctx.author.id)]['wallet']
      if wallet < bet:
        await ctx.send('Số tiền không hợp lệ!')
        return
      embed = discord.Embed(title='Roulette',
                                description='''Chơi quá '180h' một ngày sẽ bị ngu?''',
                                colour=discord.Colour.blue())
      embed.add_field(name='1-36 (Một số):', value='x35', inline=False)
      embed.add_field(name='odd/even (Lẻ/Chẵn):', value='x2', inline=False)
      embed.add_field(name='first (1-18):', value='x2', inline=False)
      embed.add_field(name='second (19-36):', value='x2', inline=False)
      embed.add_field(name='Cách chơi:', value='Chat 1, ...,36, odd, even, first, second', inline=False)
      embed.add_field(name='Số tiền còn lại của bạn:', value=wallet, inline=False)
      await ctx.send(embed=embed)

      deal = random.randint(1,36)

      try:
        mess = await self.client.wait_for('message', check=lambda m: m.author == ctx.author and m.channel, timeout=30)
        
      except asyncio.TimeoutError:
        await ctx.send('Lỗi')
      else:

        bettor = mess.content.lower()
        bettorOut = mess.content.lower()
        dealOut = deal
        

        if bettor == 'odd' or bettor == 'even':
          if bettor == 'odd':
            bettor = 1
          else:
            bettor = 0
          deal %= 2
          if bettor == deal:
            desc = f'{ctx.author.mention} đã thắng {bet*2}!!'
          else:
            desc = f'{ctx.author.mention} đã thua {bet}!!'
            bet = -bet

          users[str(ctx.author.id)]['wallet'] += bet
          users[str(ctx.author.id)]['totalbet'] += abs(bet)
          wallet = users[str(ctx.author.id)]['wallet']

          embed = discord.Embed(title='Roulette',
                                description=desc,
                                colour=discord.Colour.blue())
          embed.add_field(name='Nhà cái:', value=dealOut, inline=True)
          embed.add_field(name='Bạn:', value=bettorOut, inline=True)
          embed.add_field(name='Số tiền còn lại của bạn:', value=wallet, inline=False)
          await ctx.send(embed=embed)


        elif bettor == 'first':
          bettor = 18
          if deal <= bettor:
            desc = f'{ctx.author.mention} đã thắng {bet*2}!!'
          else:
            desc = f'{ctx.author.mention} đã thua {bet}!!'
            bet = -bet

          users[str(ctx.author.id)]['wallet'] += bet
          users[str(ctx.author.id)]['totalbet'] += bet
          wallet = users[str(ctx.author.id)]['wallet']

          embed = discord.Embed(title='Roulette',
                                description=desc,
                                colour=discord.Colour.blue())
          embed.add_field(name='Nhà cái:', value=dealOut, inline=True)
          embed.add_field(name='Bạn:', value=bettorOut, inline=True)
          embed.add_field(name='Số tiền còn lại của bạn:', value=wallet, inline=False)
          await ctx.send(embed=embed)


        elif bettor == 'second':
          bettor = 18
          if deal > bettor:
            desc = f'{ctx.author.mention} đã thắng {bet*2}!!'
          else:
            desc = f'{ctx.author.mention} đã thua {bet}!!'
            bet = -bet

          users[str(ctx.author.id)]['wallet'] += bet
          users[str(ctx.author.id)]['totalbet'] += abs(bet)
          wallet = users[str(ctx.author.id)]['wallet']

          embed = discord.Embed(title='Roulette',
                                description=desc,
                                colour=discord.Colour.blue())
          embed.add_field(name='Nhà cái:', value=dealOut, inline=True)
          embed.add_field(name='Bạn:', value=bettorOut, inline=True)
          embed.add_field(name='Số tiền còn lại của bạn:', value=wallet, inline=False)
          await ctx.send(embed=embed)

        
        elif int(bettor)-36 <= 0:

          if int(bettor) == int(deal):
            desc = f'{ctx.author.mention} đã thắng {bet*35}!!'
            bet *= 34
          else:
            desc = f'{ctx.author.mention} đã thua {bet}!!'
            bet = -bet

          users[str(ctx.author.id)]['wallet'] += bet
          users[str(ctx.author.id)]['totalbet'] += abs(bet)
          wallet = users[str(ctx.author.id)]['wallet']

          embed = discord.Embed(title='Roulette',
                                description=desc,
                                colour=discord.Colour.blue())
          embed.add_field(name='Nhà cái:', value=dealOut, inline=True)
          embed.add_field(name='Bạn:', value=bettorOut, inline=True)
          embed.add_field(name='Số tiền còn lại của bạn:', value=wallet, inline=False)
          await ctx.send(embed=embed)
        else:
          await ctx.send('Lỗi!!')

      with open("./bank.json", "w") as f:
        json.dump(users, f)


def setup(client):
    client.add_cog(Roulette(client))
