import discord
from discord.ext import commands
import random
from discord.ext.commands.cooldowns import BucketType


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
async def RBM(ctx):
    await ctx.send("""RBM AI module is compatible with ROT. Do NOT use the combat module with ROT
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
1. Installed the mod as presented in this video with the correct load order https://youtube.com/watch?v=v9cXaniwaqI&feature=share
2. Disabled ANY other mods apart from the ones related to ROT as seen in the video above
3. Make sure you are using the correct version of the game and the mod
If you are still having problems, feel free to let us know in one of the help channels under the support category""") 

# Gives a welcome message when a new user joins

@bot.event
async def on_member_join(member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'''Welcome {member.mention} to the {guild.name} discord server!
We're glad to have you here, if you want to get started with the mod check out this video to install it:
https://youtube.com/watch?v=v9cXaniwaqI&feature=share. To see what commands the bot has available you can use ?help.
The prefix for commands is a "?". ex: ?diplomacy to find out more about the diplomacy mod with ROT'''
            await guild.system_channel.send(to_send)


bot.run('TOKEN')
