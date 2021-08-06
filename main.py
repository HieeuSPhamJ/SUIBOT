import discord
import os
import random
import asyncio
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions
from discord.ext.commands import CheckFailure
from host import host
from replit import db

client = commands.Bot(command_prefix='s+')
client.remove_command('help')

#PERSONAL ID
HieeuSPhamJ = 480729328175415296
NightForce = 414264661567864843
k = 762685268892712981
mavuong = 453353710186135582
makato = 561496357722914834
iaman = 457836892587687946
hoangkun = 764711096216977428
rias = 792048455001702421

#ROLE VARIABLE
tunhan = 762694968930074644
checkrole = 856054757855461406
phophong = 751335254249439243
truongphong = 863332814526349312
bonker = 861118048739393546
bonkerpp = 863333286328008704
kp = 766200283839332393
suimem = 763763288856068166
viprole = 766498339612655617
godofsui = 800242595472080897
suixuyenvutru = 768896739037413437
suidividoichophep = 768895709449289738
suitrieunam = 766499889852448779
vanvatdieusui = 755978723185917983
canbosui = 751337663281233981
botrole = 751339239395950594

#CHANNEL
chung = 764510929500373023
mutechannel = 784235323781152769


#Check BOT in run
@client.event
async def on_ready():
    print("Bot is ready.")


#s+verify
@client.command()
async def verify(ctx):
    guild = ctx.guild
    role = discord.utils.get(guild.roles, id=checkrole)
    await ctx.author.add_roles(role)
    channel = client.get_channel(chung)
    await channel.send(
        f'''Rạp xiếc trung ương Sủiteam xin chào đón bạn {ctx.author.mention}
Ở SỦiteam bạn có thể:
+ 1p mới vô, bạn sẽ biến thành gay (?)
+ BẠn sẽ gặp đội ngũ dịch giả kiến thức thì ít mà tấu hài bằng gg dịch là nhiều
+ Nơi trú ẩn của các teito, winner ẩn danh.
+ Giao lưu cùng Sủi trúa, người tiên phong trong việc truyền đạo sủi tới tận nửa kia trái đất.
+Sv nhiều tài lẻ: làm game, hát hò, hoạ sĩ, buckfoi, vvvv...
+ Lâu lâu nó dảk vãi lone.
+ Cướp waifu như cướp kẹo con nít!
+ Bot nhạc Đường tôi chở em về độc quyền: Hoàngkun!
+ Gái không nhiều nhưng chăm online.
+ Gặp gỡ các idol giới trẻ.
+ Tôm chúa, tôm hùm, tôm sông, nói chung là lắm tôm vcl!
https://cdn.discordapp.com/attachments/764510929500373023/862976888531320852/video0.mov
''')


#s+help
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title='HƯỚNG DẪN CỦA S.U.I',
                          description='',
                          colour=discord.Colour.blue())
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.add_field(name='s+ping', value='Gọi cho tôi', inline=False)
    embed.add_field(name='s+kick <đối tượng>',
                    value='Đá ai đó ra khỏi server',
                    inline=False)
    embed.add_field(name='s+ban <đối tượng>',
                    value='Đá ai đó ra khỏi server nhưng là vĩnh viễn',
                    inline=False)
    embed.add_field(
        name='s+mute <đối tượng> <thời gian> <lý do>',
        value='Nhốt ai đó vào tù (nếu không có thời gian sẽ là vĩnh viễn)',
        inline=False)
    embed.add_field(name='s+unmute <đối tượng>',
                    value='Ân xá cho tù nhân',
                    inline=False)
    embed.add_field(
        name='s+info <đối tượng>',
        value=
        'Kiểm tra thẻ nhân viên của tổ chức Secret Universe Investigation Organization',
        inline=False)

    await ctx.send(embed=embed)


#s+test
@client.command()
async def test(ctx):
    pass


#s+ping
@client.command()
async def ping(ctx):
    if ctx.author.id == k:
        answer = [
            'Chào sếp K', 'Sếp cần gì ở tôi?',
            'Tôi, đặc vụ toàn quyền của Tổ Chức Điều Tra Vũ Trụ Bí Mật, xin nghe lệnh'
        ]
    elif ctx.author.id == mavuong:
        answer = [
            'Ma Vương cần gì ạ!', 'Chào ngài, Ma vương!',
            'Tôi, đặc vụ toàn quyền của Tổ Chức Điều Tra Vũ Trụ Bí Mật, xin nghe lệnh'
        ]
    elif ctx.author.id == hoangkun:
        answer = [
            'Hát đi ngài!', 'Sếp cần đấm thằng nào vậy?',
            'Tôi, đặc vụ toàn quyền của Tổ Chức Điều Tra Vũ Trụ Bí Mật, xin nghe lệnh'
        ]
    elif ctx.author.id == NightForce:
        answer = [
            'Anh Quý ơi?', 'Sếp cần khử thằng nào vậy?',
            'Tôi, đặc vụ toàn quyền của Tổ Chức Điều Tra Vũ Trụ Bí Mật, xin nghe lệnh',
            'Thưa ngài đã đến giờ rồi!',
            'Bọn Edit đi làm việc đi. Lời của sếp là tuyệt đối.',
            'Thưa ngài, đến giờ Trans rồi.',
            'Dạ thưa, phát hiện vài kẻ lười biếng không làm việc. Tôi nên xử trí như nào?',
            'Tôi có nên tống hết bọn Edit vô tù không ạ?'
        ]
    elif ctx.author.id == makato:
        answer = [
            'Tôi, đặc vụ toàn quyền của Tổ Chức Điều Tra Vũ Trụ Bí Mật, xin nghe lệnh',
            'H-187, Code của ngài đây ạ', 'Xin chào Makato, cậu cần gì ở tôi?',
            'Makato à, đến giờ đi ngủ rồi đấy',
            'Edit chưa mà còn ở đây thế Makato?'
        ]
    elif ctx.author.id == iaman:
        answer = [
            'Tôi, đặc vụ toàn quyền của Tổ Chức Điều Tra Vũ Trụ Bí Mật, xin nghe lệnh',
            'Ngài tham mưu trưởng cần gì ở tôi?', 'Đến giờ đi ỉa rồi ngài!'
        ]
    elif ctx.author.id == HieeuSPhamJ:
        answer = [
            'Tôi, đặc vụ toàn quyền của Tổ Chức Điều Tra Vũ Trụ Bí Mật, xin nghe lệnh',
            'Ngài cần trảm đứa nào vậy?'
        ]
    elif ctx.author.id == rias:
        answer = ['Ping nữa tôi đấm!!', 'Câm mẹ mồm vào!!']
    else:
        answer = [
            'Đồng chí cần gì vậy?', 'Đồng chí ping tôi làm gì?',
            'Tôi đang bận, xin đồng chí đừng làm phiền', 'Cút!!',
            'Biến đi, bố mày đang bận!',
            ' không liên quan nhưng đồng chí đã like Fanpage SUITEAM chưa? https://www.facebook.com/mgk.transteam'
        ]
    await ctx.send(random.choice(answer))


#s+svinfo
@client.command()
async def svinfo(ctx):
    pass


#s+info
@client.command()
async def info(ctx, member: discord.Member):
    guild = ctx.guild
    if discord.utils.get(guild.roles, id=kp) in member.roles:
        role = 'Cố vấn'
    elif discord.utils.get(guild.roles, id=bonkerpp) in member.roles:
        role = 'Thẩm phán tối cao'
    elif discord.utils.get(guild.roles, id=bonker) in member.roles:
        role = 'Thẩm phán'
    elif discord.utils.get(guild.roles, id=truongphong) in member.roles:
        role = 'Tham mưu trưởng'
    elif discord.utils.get(guild.roles, id=phophong) in member.roles:
        role = 'Phó tham mưu trưởng'
    elif discord.utils.get(guild.roles, id=botrole) in member.roles:
        role = 'Đặc vụ toàn quyền'
    elif discord.utils.get(guild.roles, id=suimem) in member.roles:
        role = 'Thanh tra đặc biệt'
    elif discord.utils.get(guild.roles, id=viprole) in member.roles:
        role = 'Thanh tra'
    elif discord.utils.get(guild.roles, id=godofsui) in member.roles:
        role = 'Điều tra viên cấp cao'
    elif discord.utils.get(guild.roles, id=suixuyenvutru) in member.roles:
        role = 'Điều tra viên cấp cao'
    elif discord.utils.get(guild.roles, id=suidividoichophep) in member.roles:
        role = 'Điều tra viên'
    elif discord.utils.get(guild.roles, id=suitrieunam) in member.roles:
        role = 'Điều tra viên'
    elif discord.utils.get(guild.roles, id=vanvatdieusui) in member.roles:
        role = 'Đặc vụ'
    elif discord.utils.get(guild.roles, id=canbosui) in member.roles:
        role = 'Đặc vụ'
    else:
        role = 'Nhân viên thường'

    embed = discord.Embed(title='Tên nhân viên:',
                          description=member.mention,
                          colour=discord.Colour.blue())
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name='Chức vụ:', value=role, inline=False)
    await ctx.send(embed=embed)


#s+mute
@client.command()
@has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, time='___', reason='___'):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, id=tunhan)
    time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    if time == '___':
        await member.add_roles(mutedRole, reason=reason)
        embed = discord.Embed(title='TÒA ÁN TỐI CAO',
                              description='Lệnh bắt giữ',
                              colour=discord.Colour.blue())
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name='Người kết án',
                        value=ctx.author.mention,
                        inline=False)
        embed.add_field(name='Tội phạm', value=member.mention, inline=False)
        embed.add_field(name='Thời gian thi hành án', value=time, inline=False)
        embed.add_field(name='Lý do', value=reason, inline=False)
        channel = client.get_channel(mutechannel)
        await ctx.send(embed=embed)
        await channel.send(embed=embed)
    else:
        tempmute = int(time[0]) * time_convert[time[-1]]
        await member.add_roles(mutedRole, reason=reason)
        embed = discord.Embed(title='TÒA ÁN TỐI CAO',
                              description='Lệnh bắt giữ',
                              colour=discord.Colour.blue())
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name='Người kết án',
                        value=ctx.author.mention,
                        inline=False)
        embed.add_field(name='Tội phạm', value=member.mention, inline=False)
        embed.add_field(name='Thời gian thi hành án', value=time, inline=False)
        embed.add_field(name='Lý do', value=reason, inline=False)
        channel = client.get_channel(mutechannel)
        await ctx.send(embed=embed)
        await channel.send(embed=embed)
        await asyncio.sleep(tempmute)
        await member.remove_roles(mutedRole)


@mute.error
async def mute_error(ctx, error):
    if isinstance(error, CheckFailure):
        await ctx.send("Tôi chỉ nghe lệnh từ cấp trên!")


#s+unmute
@client.command()
@has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member, *, reason='____'):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, id=tunhan)
    await member.remove_roles(mutedRole, reason=reason)
    embed = discord.Embed(title='TÒA ÁN TỐI CAO',
                          description='Lệnh ân xá',
                          colour=discord.Colour.blue())
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name='Người ra lệnh',
                    value=ctx.author.mention,
                    inline=False)
    embed.add_field(name='Đối tượng', value=member.mention, inline=False)
    embed.add_field(name='Lý do', value=reason, inline=False)
    channel = client.get_channel(mutechannel)
    await ctx.send(embed=embed)
    await channel.send(embed=embed)


@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, CheckFailure):
        await ctx.send("Tôi chỉ nghe lệnh từ cấp trên!")


#s+kick
@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason='None'):
    await ctx.send(f"{member.mention}, Bạn đã bị trục xuất!!!")
    await member.kick(reason=reason)


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, CheckFailure):
        await ctx.send("Tôi chỉ nghe lệnh từ cấp trên!")


#s+ban
@client.command()
@has_permissions(kick_members=True)
async def ban(ctx, member: discord.Member, *, reason='None'):
    await ctx.send(f"{member.mention}, Bạn đã bị loại bỏ khỏi đa vũ trụ!!!")
    await member.ban(reason=reason)


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, CheckFailure):
        await ctx.send("Tôi chỉ nghe lệnh từ cấp trên!")


host()
client.run(os.environ['token'])
