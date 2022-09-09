import os, time, asyncio, json, discord
from discord.ext import commands

#config
TOKEN = "PASTE_HERE" #Your Bot Token
WELCOME_CHANNEL = PASTE_HERE #ID of the channel for welcome message
LEAVE_CHANNEL = PASTE_HERE #ID of channel for leave message
VERIFY_ROLE_ID = PASTE_HERE #ID of role for verified users

#prefix-settings
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#online-statement & bot-presence/status
@bot.event
async def on_ready():
    print("Bot is now Online")
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game("!static"))

#bot-command-test
@bot.command()
async def static(ctx):
  await ctx.send(":wave:")

#welcome-message
@bot.event
async def on_member_join(member):
    channel=bot.get_channel(WELCOME_CHANNEL)
    embed=discord.Embed(title=":wave: | Welcome", description=f"Hello {member.mention}, thanks for joining!", color=0xcbceff)
    embed.add_field(name="Verify to access all channels!", value=f"```Your position in the server: {len(set(bot.users))}```")
    embed.set_image(url="https://cdn.discordapp.com/attachments/883805723807588423/901580387950686259/zerotwo_ist_scheie.gif")
    await channel.send(embed=embed)

#leave-message
@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(LEAVE_CHANNEL)
    embed=discord.Embed(title=":thumbsdown: | Bye", description=f"{member.mention} just left...", color=0xcbceff)
    embed.add_field(name="Won't miss you", value=f"```We are now {len(set(bot.users))} members...```")
    embed.set_image(url="https://cdn.discordapp.com/attachments/883805723807588423/901580387950686259/zerotwo_ist_scheie.gif")
    await channel.send(embed=embed)

@bot.command()
async def verify(ctx):
    role = ctx.guild.get_role(VERIFY_ROLE_ID)
    await ctx.author.add_roles(role)
    await ctx.send(f"The <@&{VERIFY_ROLE_ID}> role has successfully been added to you. Congrats! :tada:")

#userinfo-embed
@bot.command()
async def userinfo(ctx, member:discord.Member=None):
     if member:
       embed=discord.Embed(title=f"Userinfo for {member.display_name}", color=0xcbceff)
       embed.add_field(name="Name:", value=f"```{member}```")
       embed.add_field(name="Status:", value=f"```{member.status}```")
       embed.add_field(name="Joined Server:", value= f"<t:{int(member.joined_at.timestamp())}:R>")
       embed.add_field(name="Joined Discord:", value= f"<t:{int(member.created_at.timestamp())}:R>")
       await ctx.send(embed=embed)
     else:
       embed=discord.Embed(title=f"Userinfo for {ctx.author.display_name}", color=0xcbceff)
       embed.add_field(name="Name:", value=f"```{ctx.author}```")
       embed.add_field(name="Status:", value=f"```{ctx.author.status}```")
       embed.add_field(name="Joined Server:", value=f"<t:{int(ctx.author.joined_at.timestamp())}:R>")
       embed.add_field(name="Joined Discord:", value=f"<t:{int(ctx.author.created_at.timestamp())}:R>")
       await ctx.send(embed=embed)


bot.run(TOKEN)
