import discord
import os
import random
import asyncio
import roles
import channels
import members
import json
import io
import Function
from discord.ext import commands
from discord.utils import get
from io import BytesIO, StringIO
from discord.ext.commands import has_permissions
from discord.ext.commands import CheckFailure
from host import host
from replit import db
from PIL import Image, ImageChops, ImageDraw, ImageFont


def circle(pfp,size = (215,215)):
    
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp


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

        with open("./bank.json","r") as f:
          users = json.load(f)

        if not str(member.id) in users:
          users[str(member.id)] = {}
          users[str(member.id)]['wallet'] = 0
          users[str(member.id)]['totalbet'] = 0

        wallet = users[str(member.id)]['wallet']
        rank = f'''{Function.rankfilter(users[str(member.id)]['totalbet'])}  - {users[str(member.id)]['totalbet']}'''
        wallet = str(wallet)
        role = Function.rolefilter(ctx,member)

        name = str(member)
        joined = member.joined_at.strftime("%b %Y")
        base = Function.basefilter(member)
        background = Function.bgfilter(member).resize((1105,691))

        draw = ImageDraw.Draw(base)
        font = ImageFont.truetype("./font/SVN-Nexa_Light.ttf",44)

        pfp = member.avatar_url_as(size=256)
        data = BytesIO(await pfp.read())
        pfp = Image.open(data).convert("RGBA")
        name = f"{name[:20]}.." if len(name)>20 else name

        pfp = circle(pfp,(215,215))

        draw.text((340,200),name,font = font)
        draw.text((564,314),role,font = font)
        draw.text((503,395),rank,font = font)
        draw.text((546,482),wallet,font = font)
        draw.text((544,561),joined,font = font)

        base.paste(pfp,(56,158),pfp)
        background.paste(base,(0,0),base)

        with BytesIO() as a:
          background.save(a,"PNG")
          a.seek(0)
          await ctx.send(file = discord.File(a,"profile.png"))

        with open("./bank.json","w") as f:
          json.dump(users, f)


def setup(client):
    client.add_cog(Info(client))