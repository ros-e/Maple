import discord
import toml
config = toml.load("config.toml")
bot_token = config["discord"]["token"]
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")
bot.run(bot_token)
