import discord
import asyncio
import datetime
import random



client = discord.Client()


choice = ['어', '아니']
maid = ['네 주인님', '알겠습니다 주인님']

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("-------------------------")
    await client.change_presence(game=discord.Game(name='League of Legend', type=1))


@client.event
async def on_message(message):
    now = datetime.datetime.now()



    if message.author.bot:
        return None


    if message.content == "도움":
        embed = discord.Embed(title="민성 봇 명령어", description="󠀀󠀀====================================================", color=0xff00ff)
        embed.add_field(name="훈민정음", value="󠀀󠀀󠀀루트파이", inline=True)
        embed.add_field(name="별이는~", value="󠀀󠀀 󠀀별인~", inline=True)
        embed.set_footer(text = str(now.year) + "년" + str(now.month) + "월" + str(now.day) + "일 | " +str(now.hour) + ":" + str(now.minute) + ":" +str(now.second))
        await client.send_message(message.channel, embed=embed)


    if message.content == "프로필":
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.display_name, inline=False)
        embed.set_thumbnail(url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embed)


    if "시발" in message.content or "씨발" in message.content or "병신" in message.content or "엿" in message.content or "발람" in message.content or "개같" in message.content or "ㅆㅂ" in message.content or "ㅅㅂ" in message.content:
        await client.send_message(message.channel, message.author.display_name)
        await client.send_message(message.channel, "욕하지마 새끼야")
        
        
    if "섹스" in message.content or "sex" in message.content:
        await client.send_message(message.channel, "넌 그냥 닥쳐 " + message.author.display_name)


    if message.content == "루트파이":
        await client.send_message(message.channel, "1.7724538509055160279816748334114518279754945")


    if message.content == "야":
        await client.send_message(message.channel, "왜")


    if message.content == "훈민정음":
        await client.send_message(message.channel, "나랃말싸미 듕궉에 달아 문짜와르 서르 사맏띠 아니할쌔 이런 젼차로 어린 백셩이 니르고져 홀뺴이셔도 마참나 뜨들 시러펴지 몯할노미 하니라내 이랄 위하야 어엳삐 너겨 새로 스믈여듭짜랄 맹가노니 사람마다 해여 수비 니겨 날로 쑤메 뼌안킈 하고져 할 따라미니라")


    if "할까?" in message.content or "일까?" in message.content or "말까?" in message.content or "릴까?" in message.content or "인가?" in message.content:
        await client.send_message(message.channel, random.choice(choice))


    if "민성이" in message.content:
        await client.send_message(message.channel, "이새끼가?")


    if message.author.display_name == '승호' and message.content.startswith("민성아"):
        await client.send_message(message.channel, random.choice(maid))
        
        
    if message.author.display_name == '김태균' and message.content.startswith("민성아"):
        await client.send_message(message.channel, random.choice(maid))


    if message.author.display_name == '김한성' and message.content.startswith("민성아"):
        await client.send_message(message.channel, random.choice(maid))


client.run('NTQ4ODA2MDU0MzgxNzQ4MjQ0.D1MNuQ.qebTzMK8kxfpLkzRFW4rXxaEocQ')
