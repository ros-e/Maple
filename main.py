import discord
import toml
import pyfiglet 
import datetime  
config = toml.load("config.toml")
bot_token = config["discord"]["token"]
bot = discord.Bot()

@bot.event
async def on_ready():
    ascii_art = pyfiglet.figlet_format(bot.user.name)
    print("=========================================")
    print(ascii_art.strip()) 
    print("=========================================")
    print(f"INFO  Bot started at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=========================================")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name="F*CK SWAG"
        )
    )

bot.run(bot_token)
