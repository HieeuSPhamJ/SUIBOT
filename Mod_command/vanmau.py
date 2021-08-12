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


class Vanmau(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Van Mau is working.')

    @commands.command()
    async def vanmau(self, ctx, member: discord.Member = 'None'):
        if str(member) == 'None':
            member = ctx.author
        if str(member) == 'Mudae#0807':
            answer = '''Tôi có thằng bạn là nạn nhân của bệnh Mudae, nó năm nay 15 tuổi tức là nó sinh năm 2006, trước khi nghiện nó làm ăn lương thiện lắm. Hằng ngày nó chỉ ăn và ngủ sau đó đi edit, tháng lương cũng phải 200k đến 300k. Nhưng mà từ ngày tôi thấy nó chơi Mudae thì nó trầm hẳn, không còn vui vẻ như trước. Lúc mà nó tâm sự với tôi rằng "Tao mất waifu rồi mày ạ!" thì tôi mới nhận ra rằng nó đã bị cơn nghiện Mudae hoành hành. Thế nên tôi yêu cầu mọi người đừng chơi Mudae nữa, nghiện quá rút ra không kịp đâu.'''
        elif str(member) == 'Tôm 1':
            answer = '''Tôi có thằng em sinh năm 96 học Bách Khoa, học được một thời gian thì nó chán, thế là bắt đầu đi simp gái. Không ngờ từ khi nó simp xong thì nó tốt hơn hẳn.
Ngày trước nó học hành nhiều nên người gầy rạc lắm. Nhưng kể từ khi đi simp gái, nó biết ăn uống, tập tành đầy đủ hơn. Nó bảo với tôi "Đi simp gái cũng cần body đẹp để gái chú ý đến mình nữa chứ anh". Đấy, ai bảo đi simp gái là xấu đâu?
Thằng em mình còn simp gái tới mức xin vào làm dọn vệ sinh trong công ty chỉ để... nhìn gái mỗi ngày. Nhưng vì nó chăm tập tành nên body đẹp, thế là con ông giám đốc để ý tới. Không ngờ rằng mới có một nháy thôi là con kia có thai luôn rồi, thế là phải cưới gấp với thằng có đính hôn kia. Nhìn ảnh cưới mặt chú rể tươi rói, còn nó thì đứng cạnh bên cười đểu đểu.
Phốt simp gái của thằng em mình còn nhiều lắm, nhưng giờ thì nó biết nghĩ về gia đình hơn rồi. Hồi trước nó được công ty gì bên Mỹ lớn lắm mời về làm, lương hơn chục nghìn đô mà nó không nhận do không có gái. Thế là hôm sau bên đấy phải mời cả hot girl tiktok với hoa hậu về mời nó mới đồng ý. Nghe được xong công ty mở tiệc ăn mừng mấy ngày mấy đêm mới thôi.
Giờ một ngày nó chỉ lên diu túp bật livestream kể về quá trình simp gái vài chục phút cũng kiếm được vài nghìn đô. Thêm vài post chia sẽ kinh nghiệm simp gái trong group nữa là tròn chục. Ngày làm có 2-3 tiếng mà đã giàu như thế rồi, mới hai mấy tuổi đầu mà nhà xe biệt thự đều có đủ, nghĩ mà thèm.'''
        elif member.id == members.hoangkun:
            answer = '''Tôi có ông anh tên Trần Huy Hoàng nay năm nay lên đại học, ngày đi chơi game tối mày mò tìm raw JP rồi đi dịch mấy bộ romcom. Mỗi tối cứ làm 3-4h gì đấy là xong việc. Lương tháng 3k6$ nhưng chủ yếu thu nhập chính là từ các project bên ngoài. Tuần 2-3 cái thôi lương cứ chảy như nước vào ví ngân hàng điện tử của ổng. Đà này ổng lên đại học năm 3 cũng mua được căn biệt thự ở Nha Trang ngay sát biển với vài con Vinfast.
  Cơ mà drama của ông anh tôi nhiều vô kể, từ khi còn nhỏ đã tập tành hát liveshow nên fan nữ khá đông đúc. Khi mà ổng giả mạo làm nhân viên ngân hàng Vietcombank thì quen được bà chị kia. Cơ mà con em bà chị đó thì cứng đầu không chịu chấp nhận thân phận của anh Hoàng. Nhưng từ hồi biết được anh xưa làm ca sĩ với làm dịch giả thì về bắt bố mẹ giục cưới, cơ mà do tình hình dịch này căng thẳng chứ đáng lẽ cưới từ đầu năm nay rồi.'''
        elif member.id == members.NightForce:
            answer = '''Tôi có ông anh tên Nguyễn Duy Quý nay năm nay lên đại học, ngày đi dịch truyện tối đi mày mò code rồi đi code mấy cái game cơ bản. Mỗi tối cứ làm 3-4h gì đấy là xong việc. Lương tháng 3k6$ nhưng chủ yếu thu nhập chính là từ các project bên ngoài. Tuần 2-3 cái thôi lương cứ chảy như nước vào ví ngân hàng điện tử của ổng. Đà này ổng lên đại học năm 3 cũng mua được căn biệt thự ở Nha Trang ngay sát biển với vài con Vinfast.
  Cơ mà drama của ông anh tôi nhiều vô kể, từ khi còn nhỏ đã tập tành hát liveshow nên fan nữ khá đông đúc. Khi mà ổng giả mạo làm nhân viên ngân hàng Vietcombank thì quen được bà chị kia. Cơ mà con em bà chị đó thì cứng đầu không chịu chấp nhận thân phận của anh Hoàng. Nhưng từ hồi biết được anh xưa làm ca sĩ với làm IT thì về bắt bố mẹ giục cưới, cơ mà do tình hình dịch này căng thẳng chứ đáng lẽ cưới từ đầu năm nay rồi.'''
        elif member.id == members.makato:
            answer = '''Tôi có thằng em tên Thành Trung nay năm nay vào lớp 10, ngày đi dịch truyện tối đi edit mấy bộ truyện. Mỗi tối cứ làm 3-4h gì đấy là xong việc. Lương tháng 3k6$ nhưng chủ yếu thu nhập chính là từ các project bên ngoài. Tuần 2-3 cái thôi lương cứ chảy như nước vào ví ngân hàng điện tử của nó. Đà này nó lên năm 3 trung học phổ thông cũng mua được căn biệt thự ở Nha Trang ngay sát biển với vài con Vinfast.
  Cơ mà drama của thằng em tôi nhiều vô kể, từ khi còn nhỏ đã tập tành hát liveshow nên fan nữ khá đông đúc. Khi mà nó giả mạo làm nhân viên ngân hàng Vietcombank thì quen được bà chị kia. Cơ mà con em bà chị đó thì cứng đầu không chịu chấp nhận thân phận của em Trung. Nhưng từ hồi biết được anh xưa làm ca sĩ với làm editor thì về bắt bố mẹ giục cưới, cơ mà do tình hình dịch này căng thẳng chứ đáng lẽ cưới từ đầu năm nay rồi.'''
        elif member.id == members.mavuong:
            answer = '''Mùa dịch này ở nhà không có gì làm mình cũng tự mày mò vận chuyển rồi lang thang store nước ngoài nhận ship dạo. Cũng có đồng ra đồng vô. Hết dịch đi làm có thêm nghề tay trái không lo đói.
  Giao xe hiện nay ở đầu của sự phát triển. Có thể nói giao xe là vua của các nghề. Vừa có tiền, có quyền. Vừa kiếm được nhiều $ lại được xã hội trọng vọng.
  Thằng trên Discord cùng sv với mình học con cak gì đấy bên Mẽo, sinh năm 2k5. Tự mày mò lái xe rồi đi làm lủng cho bố nó 2 năm nay. Mỗi ngày đi 3-4 giờ là xong việc. Lương tháng 1-2k. Nhưng thu nhập chính vẫn là từ nhận các store bên ngoài làm thêm. Tuần làm 2,3 cái nhẹ nhàng 9,10k tiền tươi thóc thật không phải đóng thuế. Làm gần được 2 năm mà nhà xe nó đã mua đủ cả. Nghĩ mà thèm.
  Gái gú thì cứ nghe nó bảo làm Car shipper thì chảy nước. Có bé kia vừa đi học về được cô chị giới thiệu làm ngân hàng .Thế nào thằng ấy đi nghỉ xuân gặp phải thế là hốt được cả chị lẫn em. 3 đứa nó sống chung một căn hộ cao cấp. Nhà con bé vừa giàu vừa gia giáo (cha là tiến sĩ giảng viên đại học, mẹ nó là phó chánh án) biết chuyện ban đầu phản đối sau biết thằng đấy hay đi ship xe thì đổi thái độ, cách ba bữa hỏi thăm, năm bữa tặng quà cho ba mẹ nó giục cưới kẻo lỡ kèo. Định tháng này cưới con chị và tiêp tục sống với con em nhưng dính dịch dời đám cưới lại rồi.'''
        elif member.id == members.plasma:
            answer = ''' Nagato/長門 là một trong những top waifu của game, với design của 1 cô cáo nhỏ dựa trên câu đùa Miko Miko no Miko. Thiết kế loli của Nagato vừa dễ thương, vừa ý nghĩa vì nó nhắc đến 1 trường Tiểu học đã quyên góp tiền để tạo ra em ấy. Mái tóc đen dài và cắt kiểu Hime khiến Nagato toát ra vẻ quý phái của quý tộc và cũng rất hợp lý vì công việc của cô ấy là Flagship đứng đầu cả một hạm đội lớn. Thường thường, khi những người khác mang theo vũ khí và riggings bên mình sẽ khiến những người xung quanh lo lắng và bất an vì họ hơi đáng sợ, tuy nhiên đối với Nagato, thân hình nhỏ nhắn cùng với bộ áo Miko màu đỏ lại khiến em khi đeo riggings trở nên cute một cách đáng sợ. Ngoài ra, Nagato còn có rất nhiều trang phục trong kho của mình, Kimono? Có, đồ ngủ? Có. Dù em ấy đã gần bị tiêu diệt bởi 2 quả bom nguyên tử? Tôi đã cứu em ấy và để em trong harem cảng của tôi, một nơi đầy ắp tiếng cười và cuối cùng, em cũng đã có thể hoà nhập với mọi người, đã có thể cười và không còn quá lo lắng về vai trò của mình nữa.


Dù em là ảo nhưng tôi vẫn luôn yêu thương em, Imperial Japanese Navy Flagship Nagato 

Bài văn của 1 tôm chúa Nagato '''
        elif member.id == members.hoangem:
            answer = ''' Hòn em, 1 nhân vật nổi tiếng trong SuiTeam với những câu nói thấm thía lòng người cùng những lần cố gắng Cosplay thành ‘Ngôi sao Giải Trí’ đẳng cấp. Hơn nữa, Hòn em đã tôi luyện, mài dũa khả năng tự hủy đẳng cấp, giúp anh ấy trở thành một trong những nhân vật ảnh hưởng nhất Sủi World. Tuy nhiên, liệu đây có phải là tác dụng phụ của việc tập luyện hay không mà các fetish của anh ấy luôn vượt xa tầm hiểu biết của con người, cùng trình độ Liên Minh đẳng cấp khi anh ấy có khả năng Convert mọi tướng thành Role ‘Đỡ Đòn’. Tuy vậy, anh ấy vẫn là một trong những người mạnh nhất khi luôn luôn làm đại ca trong tù và quả não của Monsieur Tuna khi đ*o biết đặt tên gì cho ngầu. Tôi xin tóm lại Hòn em trong 3 từ:
"Gay vãi loz"'''
        else:
            answer = 'Đồng chí này chưa có văn mẫu!'
        await ctx.send(answer)


def setup(client):
    client.add_cog(Vanmau(client))
