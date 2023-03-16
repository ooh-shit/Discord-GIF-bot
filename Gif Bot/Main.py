import discord
import random
import discord.ext.commands
from discord.ext.commands import Bot
from discord import colour
from discord.embeds import Embed

Token = "MTA0Nzk1NjYyMDY5MDMyNTU4NQ.GrMcmg.-fy6r7owNp2KG_K7ZYoqgRttJJi402-G_nRdD8"

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

bot  = Bot(command_prefix="!",intents=intents)


punch_gif = ["https://media.tenor.com/2VDSIhwM2uUAAAAM/hasbulla-hasbik.gif","https://media.tenor.com/2VDSIhwM2uUAAAAM/hasbulla-hasbik.gif","https://media.tenor.com/f3J-yZcZfU0AAAAM/cat-punch.gif","https://media.tenor.com/6Cp5tiRwh-YAAAAM/meme-memes.gif" , "https://media.tenor.com/kw5lYGbw8oAAAAAM/one-punch-man.gif"]
kick_gif = ["https://media.tenor.com/qE3sYVzhFH8AAAAM/kick.gif"]
slap_gif = ["https://media.tenor.com/ad-6mXRUMJwAAAAM/slap.gif"]
salute_gif = ["https://media.tenor.com/QRYQfe7hIpcAAAAM/salute-point.gif","https://media.tenor.com/LdAr7ZnMsaMAAAAM/yes-sir-yes-boss.gif"]
hello_gif = ["https://media2.giphy.com/media/3pZipqyo1sqHDfJGtz/200.webp?cid=ecf05e47880xcex3ndxka2jseskas03zijrqkwllqoy00s5w&rid=200.webp&ct=g","https://media2.giphy.com/media/Vbtc9VG51NtzT1Qnv1/200.webp?cid=ecf05e47880xcex3ndxka2jseskas03zijrqkwllqoy00s5w&rid=200.webp&ct=g","https://media2.giphy.com/media/G3Hu8RMcnHZA2JK6x1/200w.webp?cid=ecf05e47880xcex3ndxka2jseskas03zijrqkwllqoy00s5w&rid=200w.webp&ct=g"]

@bot.command()
async def hello(ctx):
  embed = discord.Embed()
  embed.set_image(url = (random.choice(hello_gif)))
  await ctx.send(embed=embed)




@bot.command()
async def punch(ctx):
  embed = discord.Embed()
  embed.set_image(url = (random.choice(punch_gif)))

  await ctx.send(embed = embed)

@bot.command()
async def kick(ctx):
  embed = discord.Embed()
  embed.set_image(url = (random.choice(kick_gif)))

  await ctx.send(embed = embed)

@bot.command()
async def slap(ctx):
  embed = discord.Embed()
  embed.set_image(url = (random.choice(slap_gif)))

  await ctx.send(embed = embed)

@bot.command()
async def salute(ctx):
  embed = discord.Embed()
  embed.set_image(url = (random.choice(salute_gif)))

  await ctx.send(embed = embed)




bot.run(Token)
