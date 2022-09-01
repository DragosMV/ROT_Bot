import discord
from discord.ext import commands
import random
from discord.ext.commands.cooldowns import BucketType
import datetime


description = '''A discord bot used in the Realm of Thrones Bannerlord mod community.
                 Contact Solomon#2518 on discord for help/feedback related to the bot.
                 Feel free to let me know if any of the information in the commands is
                 outdated or if there is anything else you would like me to add!'''

# Set up the bot with intents. Intents need to be activated on the developer portal
intents = discord.Intents.default()        
intents.members = True
intents.message_content = True


# Create a subclass of the MinimalHelpCommand to overwrite the default value for no_category so that commands without a category will be displayed as commands
class MyHelp(commands.MinimalHelpCommand):
    def __init__(self):
        super().__init__() 
        self.no_category = "Commands"

# Initialise bot
bot = commands.Bot(command_prefix='?', description=description, help_command = MyHelp(), intents=intents)

# async and await make it so the bot can perform multiple actions at the same time (don't want it to freeze while sending a command/message)

# Confirm startup of bot with a message
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

# Diplomacy info text command
@commands.cooldown(1,6,BucketType.user) 
@bot.command()
async def diplomacy(ctx):
    await ctx.send("""Diplomacy is compatible with ROT but you will have to download it from the following link for it to work:
https://github.com/bennyz/Bannerlord.Diplomacy/releases/tag/v1.1.11.4""") 

# RBM info text command
@commands.cooldown(1,6,BucketType.user)
@bot.command()
async def rbm(ctx):
    await ctx.send("""RBM AI module is compatible with ROT. Do NOT use the combat module with ROT (disable it in main menu after loading up the game)
https://www.nexusmods.com/mountandblade2bannerlord/mods/791""") 

# ServeAsSoldier info text command
@commands.cooldown(1,6,BucketType.user)
@bot.command()
async def serve(ctx):
    await ctx.send("""Serve as soldier is compatible with ROT BUT you will have to follow these steps before launching:
1. open the settings.xml in Modules\ServeAsSoldier with a text editor
2. change the <AIRecruitWanders>true</AIRecruitWanders> to false
https://www.nexusmods.com/mountandblade2bannerlord/mods/3242?tab=description""")

# If you can't decide what culture to choose
@commands.cooldown(1,6,BucketType.user)
@bot.command(description='For when you want to pick a culture randomly')
async def culture(ctx, *choices: str):
    """Chooses between multiple cultures. Add each choice separated by a space:  
       ?culture crownlands stormlands ghiscari.
       Will pick from all cultures if no choice given."""
    if choices:                                   # Choose from choices if they have been given
        await ctx.send(random.choice(choices))
    else:
        choices = ["Westerman", "Ironborn", "Essosi", "Dornish", "Dothraki", "Northman", "Ghiscari", "Dragonstone", "Valeman", 
        "Reachman", "Riverman", "Stormlander", "Crownlander", "Sarnori", "Night's Watch", "Free Houses", "Freefolk", "Norvoshi"]      # Choose from a default list instead
        await ctx.send(random.choice(choices))

# Issues with installing info text command
@commands.cooldown(1,6,BucketType.user)
@bot.command()
async def issues(ctx):
    await ctx.send("""If you are having issues with running the mod please make sure you have followed these steps:
1. Installed the mod as presented in this video with the correct load order https://youtu.be/3EceOVpsg84
2. Make sure you are using the correct version of the game and the mod
If you are still having problems, you can perform a clean reinstall of everything and follow the video provided""") 

# Gives a welcome message when a new user joins


# Command about launcher
@commands.cooldown(1,6,BucketType.user)
@bot.command()
async def launcher(ctx):
    await ctx.send("""If you are using more mods try using the BUTRLoader Launcher. Details in link below:
https://www.nexusmods.com/mountandblade2bannerlord/mods/2513""") 


# Command about launcher
@commands.cooldown(1,6,BucketType.user)
@bot.command()
async def exception(ctx):
    await ctx.send("""Better exception window provides more detailed error reports:
https://www.nexusmods.com/mountandblade2bannerlord/mods/404""") 

# Command about launcher
@commands.cooldown(1,6,BucketType.user)
@bot.command()
async def giantbug(ctx):
    await ctx.send("""Unusual, giant characters are usually caused by the hot butter mod""") 


@bot.event
async def on_member_join(member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'''Welcome {member.mention} to the {guild.name} discord server!
We're glad to have you here, if you want to get started with the mod check out this video from Jackie on how to install it together with other mods:
***To see what commands the bot has available you can use ?help***
The prefix for commands is a "?". ex: ?diplomacy to find out more about the diplomacy mod with ROT
https://youtu.be/3EceOVpsg84'''
            await guild.system_channel.send(to_send)

# logs edited messages
@bot.event
async def on_message_edit(message_before,message_after):
    if message_before.author.bot:
        return
    embed = discord.Embed(colour=0xe74c3c, timestamp=datetime.datetime.now())
    embed.set_author(name=f"{message_before.author} edited a message",icon_url=message_before.author.display_avatar)
    embed.add_field(name="Before:",value=f"{message_before.content}",inline=False)
    embed.add_field(name="After:",value=f"{message_after.content}")
    channel = bot.get_channel(1014587687287656468)
    await channel.send(embed=embed)

# logs deleted messages
@bot.event
async def on_message_delete(message):
    if message.author.bot:
        return
    embed = discord.Embed(colour=0xe74c3c, timestamp=datetime.datetime.now())
    embed.set_author(name=f"{message.author} deleted a message",icon_url=message.author.display_avatar)
    embed.add_field(name="Deleted message",value=f"{message.content}",inline=False)
    channel = bot.get_channel(1014587687287656468)
    await channel.send(embed=embed)


bot.run('TOKEN')
