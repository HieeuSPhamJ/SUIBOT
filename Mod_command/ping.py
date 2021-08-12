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

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('Ping is working.')

    
    @commands.command()
    async def ping(self,ctx):
        if ctx.author.id == members.k:
            answer = [
                'Chào sếp K', 'Sếp cần gì ở tôi?',
                'Tôi, đặc vụ toàn quyền của Tổ Chức Điều Tra Vũ Trụ Bí Mật, xin nghe lệnh'
            ]
        elif ctx.author.id == members.mavuong:
            answer = [
                'Ma Vương cần gì ạ!', 'Chào ngài, Ma vương!',
                'Tôi, đặc vụ toàn quyền của Tổ Chức Điều Tra Vũ Trụ Bí Mật, xin nghe lệnh'
            ]
        elif ctx.author.id == members.hoangkun:
            answer = [
                'Hát đi ngài!', 'Sếp cần đấm thằng nào vậy?',
                'Tôi, đặc vụ toàn quyền của Tổ Chức Điều Tra Vũ Trụ Bí Mật, xin nghe lệnh'
            ]
        elif ctx.author.id == members.NightForce:
            answer = [
                'Anh Quý ơi?', 'Sếp cần khử thằng nào vậy?',
                'Tôi, đặc vụ toàn quyền của Tổ Chức Điều Tra Vũ Trụ Bí Mật, xin nghe lệnh',
                'Thưa ngài đã đến giờ rồi!',
                'Bọn Edit đi làm việc đi. Lời của sếp là tuyệt đối.',
                'Thưa ngài, đến giờ Trans rồi.',
                'Dạ thưa, phát hiện vài kẻ lười biếng không làm việc. Tôi nên xử trí như nào?',
                'Tôi có nên tống hết bọn Edit vô tù không ạ?'
            ]
        elif ctx.author.id == members.makato:
            answer = [
                'Tôi, đặc vụ toàn quyền của Tổ Chức Điều Tra Vũ Trụ Bí Mật, xin nghe lệnh',
                'H-187, Code của ngài đây ạ', 'Xin chào Makato, cậu cần gì ở tôi?',
                'Makato à, đến giờ đi ngủ rồi đấy',
                'Edit chưa mà còn ở đây thế Makato?',
                'Triệu Tử Ma, mừng ngài trở về'
            ]
        elif ctx.author.id == members.iaman:
            answer = [
                'Tôi, đặc vụ toàn quyền của Tổ Chức Điều Tra Vũ Trụ Bí Mật, xin nghe lệnh',
                'Ngài tham mưu trưởng cần gì ở tôi?', 'Đến giờ đi ỉa rồi ngài!',
                '''Anh bạn à...
    Anh bạn có muốn BÚn CUa giảng hòa không?''',
                'Xách đjt lên mà làm việc đi cái thằng Ỉa Vương này.'
            ]
        elif ctx.author.id == members.HieeuSPhamJ:
            answer = [
                'Tôi, đặc vụ toàn quyền của Tổ Chức Điều Tra Vũ Trụ Bí Mật, xin nghe lệnh',
                'Ngài cần trảm đứa nào vậy?', 'Tôi có thể bún cua ngài được không?'
            ]
        elif ctx.author.id == members.rias:
            answer = ['Welcome hắc diệt simplỏd', 'Câm mẹ mồm vào!!']
        else:
            answer = [
                'Đồng chí cần gì vậy?', 'Đồng chí ping tôi làm gì?',
                'Tôi đang bận, xin đồng chí đừng làm phiền', 'Cút!!',
                'Biến đi, bố mày đang bận!',
                'Không liên quan nhưng đồng chí đã like Fanpage SUITEAM chưa? https://www.facebook.com/mgk.transteam'
            ]
        await ctx.send(random.choice(answer))

def setup(client):
    client.add_cog(Ping(client))