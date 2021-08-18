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

with open("./EconomyAndGamble/shoproles.json", "r") as f:
    shoproles = json.load(f)

shopitem = len(shoproles)

class Shop(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Shop is working.')
        #print(shopitem)

    @commands.command()
    @has_permissions(kick_members=True)
    async def shopadd(self, ctx, name = 'None',price = 'None', id = 'None'):
      with open("./EconomyAndGamble/shoproles.json", "r") as f:
        shoproles = json.load(f)
      if name == 'None' or id == 'None' or price == 'None':
        await ctx.send('Lỗi!!')
        return

      num =int(shopitem)+1
      shoproles[str(num)] = {}
      shoproles[str(num)]['name'] = name
      shoproles[str(num)]['price'] = price
      shoproles[str(num)]['id'] = id

      await ctx.send('Done!!')
      await ctx.send(num)
      with open("./EconomyAndGamble/shoproles.json", "w") as f:
        json.dump(shoproles, f)
      
      
      
      

    @commands.command()
    async def shop(self, ctx):
        with open("./bank.json", "r") as f:
            users = json.load(f)
        with open("./EconomyAndGamble/shoproles.json", "r") as f:
            shoproles = json.load(f)
        
        embedmain = discord.Embed(title='SHOP S.U.I',
                              description='',
                              colour=discord.Colour.blue())
        embedmain.set_thumbnail(url=self.client.user.avatar_url)
        embedmain.add_field(name='1. Linh Tinh',
                        value='Buff, chỉnh BG, Info,...',
                        inline=False)
        embedmain.add_field(name='2. Role',
                        value='Role tất nhiên rồi!!',
                        inline=False)
        embedmain.add_field(name='Tổng số tiền của bạn:',
                        value=users[str(ctx.author.id)]['wallet'],
                        inline=False)
        await ctx.send(embed=embedmain)

        try:
          mess = await self.client.wait_for('message', check=lambda m: m.author == ctx.author and m.channel, timeout=10)
            
        except asyncio.TimeoutError:
          await ctx.send('Quá thời gian!!')

        if mess.content.lower() == '1':
          embedother = discord.Embed(title='SHOP S.U.I',
                              description='',
                              colour=discord.Colour.blue())
          embedother.set_thumbnail(url=self.client.user.avatar_url)
          embedother.add_field(name='1. Buff',
                              value='Buff tiền daily, tiền mỗi lần chat,..',
                              inline=False)
          embedother.add_field(name='2. Theme info',
                              value='Khung của info',
                              inline=False)
          embedother.add_field(name='3. Tùy chỉnh background info',
                              value='15000',
                              inline=False)
          embedother.add_field(name='Tổng số tiền của bạn:',
                              value=users[str(ctx.author.id)]['wallet'],
                              inline=False)
          await ctx.send(embed=embedother)

          try:
            mess = await self.client.wait_for('message', check=lambda m: m.author == ctx.author and m.channel, timeout=10)

          except asyncio.TimeoutError:
            await ctx.send('Quá thời gian!!')
          
          if mess.content.lower() == '1':
            await ctx.send('Tính năng chưa có!')
          elif mess.content.lower() == '2':
            #await ctx.send('Tính năng chưa có!')
            embedtheme = discord.Embed(title='SHOP S.U.I',
                                      description='',
                                      colour=discord.Colour.blue())
            embedtheme.set_thumbnail(url=self.client.user.avatar_url)
            embedtheme.add_field(name='1. Theme Gốc - 0', value='[Ảnh minh họa](https://media.discordapp.net/attachments/877375163786739722/877375297908015114/profilecard.png)', inline=False)
            embedtheme.add_field(name='2. Theme 2 - 1500', value='[Ảnh minh họa](https://cdn.discordapp.com/attachments/877375163786739722/877375245089136660/profilecard2.png)', inline=False)
            embedtheme.add_field(name='3. Theme 3 - 2000', value='[Ảnh minh họa](https://cdn.discordapp.com/attachments/877375163786739722/877375250503983144/profilecard3.png)', inline=False)
            embedtheme.add_field(name='4. Theme 4 - 10000', value='[Ảnh minh họa](https://cdn.discordapp.com/attachments/877375163786739722/877393717265301524/profilecard4.png)', inline=False)
            embedtheme.add_field(name='5. Theme 5 - 10000', value='[Ảnh minh họa](https://cdn.discordapp.com/attachments/877375163786739722/877393705286389760/profilecard5.png)', inline=False)
            embedtheme.add_field(name='Tổng số tiền của bạn:',
                                value=users[str(ctx.author.id)]['wallet'],
                                inline=False)
            await ctx.send(embed=embedtheme)
            try:
              mess = await self.client.wait_for('message', check=lambda m: m.author == ctx.author and m.channel, timeout=60)

            except asyncio.TimeoutError:
              await ctx.send('Quá thời gian!!')

            with open("./background.json","r") as f:
                bgs = json.load(f)
            
            if mess.content.lower() == '1':
              price = 0
              if users[str(ctx.author.id)]['wallet'] < price:
                await ctx.send('Bạn không đủ tiền!')
                return
              users[str(ctx.author.id)]['wallet'] -= price
              bgs[str(ctx.author.id)] = {}
              bgs[str(ctx.author.id)]['background'] = "https://cdn.discordapp.com/attachments/873964288216289360/876382844145004584/transparent_profilecard.png"
              bgs[str(ctx.author.id)]['theme'] = 1
              await ctx.send('Done!!')

            if mess.content.lower() == '2':
              price = 1500
              if users[str(ctx.author.id)]['wallet'] < price:
                await ctx.send('Bạn không đủ tiền!')
                return
              users[str(ctx.author.id)]['wallet'] -= price
              bgs[str(ctx.author.id)] = {}
              bgs[str(ctx.author.id)]['background'] = "https://cdn.discordapp.com/attachments/873964288216289360/876382844145004584/transparent_profilecard.png"
              bgs[str(ctx.author.id)]['theme'] = 2
              await ctx.send('Done!!')

            if mess.content.lower() == '3':
              price = 2000
              if users[str(ctx.author.id)]['wallet'] < price:
                await ctx.send('Bạn không đủ tiền!')
                return
              users[str(ctx.author.id)]['wallet'] -= price
              bgs[str(ctx.author.id)] = {}
              bgs[str(ctx.author.id)]['background'] = "https://cdn.discordapp.com/attachments/873964288216289360/876382844145004584/transparent_profilecard.png"
              bgs[str(ctx.author.id)]['theme'] = 3
              await ctx.send('Done!!')
            
            if mess.content.lower() == '4':
              price = 10000
              if users[str(ctx.author.id)]['wallet'] < price:
                await ctx.send('Bạn không đủ tiền!')
                return
              users[str(ctx.author.id)]['wallet'] -= price
              bgs[str(ctx.author.id)] = {}
              bgs[str(ctx.author.id)]['background'] = "https://cdn.discordapp.com/attachments/873964288216289360/876382844145004584/transparent_profilecard.png"
              bgs[str(ctx.author.id)]['theme'] = 4
              await ctx.send('Done!!')
            
            if mess.content.lower() == '5':
              price = 10000
              if users[str(ctx.author.id)]['wallet'] < price:
                await ctx.send('Bạn không đủ tiền!')
                return
              users[str(ctx.author.id)]['wallet'] -= price
              bgs[str(ctx.author.id)] = {}
              bgs[str(ctx.author.id)]['background'] = "https://cdn.discordapp.com/attachments/873964288216289360/876382844145004584/transparent_profilecard.png"
              bgs[str(ctx.author.id)]['theme'] = 5
              await ctx.send('Done!!')

            with open("./background.json","w") as f:
                json.dump(bgs, f)

          elif mess.content.lower() == '3':
            #await ctx.send('Tính năng chưa có!')
            price = 15000
            if users[str(ctx.author.id)]['wallet'] < price:
              await ctx.send('Bạn không đủ tiền!')
              return
            await ctx.send('Bạn chắc không?(y/n)')
            try:
              mess = await self.client.wait_for('message', check=lambda m: m.author == ctx.author and m.channel, timeout=10)
            except asyncio.TimeoutError:
              await ctx.send('Quá thời gian!!')

            message = mess.content.lower()
            if message == 'y':
              with open("./background.json","r") as f:
                bgs = json.load(f)

              bgs[str(ctx.author.id)] = {}
              bgs[str(ctx.author.id)]['background'] = "https://cdn.discordapp.com/attachments/873964288216289360/876382844145004584/transparent_profilecard.png"
              bgs[str(ctx.author.id)]['check'] = 1
              users[str(ctx.author.id)]['wallet'] -= price
              await ctx.send('Done!!')

              with open("./background.json","w") as f:
                json.dump(bgs, f)
            else:
              await ctx.send('Lỗi!!')
            





        elif mess.content.lower() == '2':
            embed = discord.Embed(title='SHOP S.U.I',
                                      description='',
                                      colour=discord.Colour.blue())
            embed.set_thumbnail(url=self.client.user.avatar_url)
            for item in shoproles:
              users[str(ctx.author.id)]['wallet']
              embed.add_field(name=f''' {item}. {shoproles[item]['name']} ''',
                              value=shoproles[str(item)]['price'],
                              inline=False)
              shopitem = item
            embed.add_field(name='Tổng số role:',
                              value=shopitem,
                              inline=False)
            embed.add_field(name='Tổng số tiền của bạn:',
                              value=users[str(ctx.author.id)]['wallet'],
                              inline=False)
            await ctx.send(embed=embed)
            
            try:
              mess = await self.client.wait_for('message', check=lambda m: m.author == ctx.author and m.channel, timeout=60)
            
            except asyncio.TimeoutError:
              await ctx.send('Quá thời gian!!')

            message = mess.content.lower()
            choose = mess.content.lower()
            if int(message) <= int(shopitem):
              wallet = users[str(ctx.author.id)]['wallet']
              price = shoproles[str(choose)]['price']
              #await ctx.send(f'{int(price)} - {int(wallet)}')
              if int(price) > int(wallet):
                await ctx.send('Bạn không có đủ tiền?')
                return
              #await ctx.send(message)
              await ctx.send('Bạn chắc không?(y/n)')
              try:
                mess = await self.client.wait_for('message', check=lambda m: m.author == ctx.author and m.channel, timeout=10)

              except asyncio.TimeoutError:
                await ctx.send('Quá thời gian!!')

              message = mess.content.lower()
              if message == 'y':
                guild = ctx.guild
                role = discord.utils.get(guild.roles, id=shoproles[choose]['id'])
                await ctx.author.add_roles(role)
                users[str(ctx.author.id)]['wallet'] -= price
                await ctx.send('Done!!')

            else:
              await ctx.send('Lỗi!!')



        with open("./bank.json", "w") as f:
            json.dump(users, f)
        with open("./EconomyAndGamble/shoproles.json", "w") as f:
            json.dump(shoproles, f)


def setup(client):
    client.add_cog(Shop(client))
