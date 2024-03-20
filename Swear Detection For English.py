import discord
from discord.ext import commands
import asyncio
import re

# Define the list of swear words and phrases
swear_words = [
    "2 girls 1 cup", "2g1c", "4r5e", "5h1t", "5hit", "a$$", "a$$hole", "a_s_s", "a2m", "a54", "a55", "a55hole",
    "aeolus", "ahole", "alabama hot pocket", "alaskan pipeline", "anal", "anal impaler", "anal leakage",
    "analannie", "analprobe", "analsex", "anilingus", "anus", "apeshit", "ar5e", "areola", "areole", "arian",
    "arrse", "arse", "arsehole", "aryan", "ass", "ass fuck", "ass hole", "assault", "assbag", "assbagger",
    "assbandit", "assbang", "assbanged", "assbanger", "assbangs", "assbite", "assblaster", "assclown",
    "asscock", "asscracker", "asses", "assface", "assfaces", "assfuck", "assfucker", "ass-fucker", "assfukka",
    "assgoblin", "assh0le", "asshat", "ass-hat", "asshead", "assho1e", "asshole", "assholes", "asshopper",
    "asshore", "ass-jabber", "assjacker", "assjockey", "asskiss", "asskisser", "assklown", "asslick",
    "asslicker", "asslover", "assman", "assmaster", "assmonkey", "assmucus", "assmunch", "assmuncher",
    "assnigger", "asspacker", "asspirate", "ass-pirate", "asspuppies", "assranger", "assshit", "assshole",
    "asssucker", "asswad", "asswhole", "asswhore", "asswipe", "asswipes", "auto erotic", "autoerotic",
    "axwound", "azazel", "azz", "b!tch", "b00bs", "b17ch", "b1tch", "babe", "babeland", "babes", "baby batter",
    "baby juice", "badfuck", "ball gag", "ball gravy", "ball kicking", "ball licking", "ball sack", "ball sucking",
    "ballbag", "balllicker", "balls", "ballsack", "bampot", "bang", "bang (one's) box", "bangbros", "banger",
    "banging", "bareback", "barely legal", "barenaked", "barf", "barface", "barfface", "bastard", "bastardo",
    "bastards", "bastinado", "batty boy", "bawdy", "bazongas", "bazooms", "bbw", "bdsm", "beaner", "beaners",
    "beardedclam", "beastial", "beastiality", "beatch", "beater", "beatyourmeat", "beaver", "beaver cleaver",
    "beaver lips", "beef curtain", "beef curtains", "beer", "beeyotch", "bellend", "bender", "beotch", "bestial",
    "bestiality", "bi+ch", "biatch", "bicurious", "big black", "big breasts", "big knockers", "big tits",
    "bigbastard", "bigbutt", "bigger", "bigtits", "bimbo", "bimbos", "bint", "birdlock", "bisexual", "bi-sexual",
    "bitch", "bitch tit", "bitchass", "bitched", "bitcher", "bitchers", "bitches", "bitchez", "bitchin", "bitching",
    "bitchtits", "bitchy", "black cock", "blonde action", "blonde on blonde action", "bloodclaat", "bloody",
    "bloody hell", "blow", "blow job", "blow me", "blow mud", "blow your load", "blowjob", "blowjobs", "blue waffle",
    "blumpkin", "boang", "bod", "bodily", "bogan", "bohunk", "boink", "boiolas", "bollick", "bollock", "bollocks",
    "bollok", "bollox", "bomd", "bondage", "bone", "boned", "boner", "boners", "bong", "boob", "boobies", "boobs",
    "booby", "booger", "bookie", "boong", "boonga", "booobs", "boooobs", "booooobs", "booooooobs", "bootee", "bootie",
    "booty", "booty call", "booze", "boozer", "boozy", "bosom", "bosomy", "bowel", "bowels", "bra", "brassiere",
    "breast", "breastjob", "breastlover", "breastman", "breasts", "breeder", "brotherfucker", "brown showers",
    "brunette action", "buceta", "bugger", "buggered", "buggery", "bukkake", "bull shit", "bullcrap", "bulldike",
    "bulldyke", "bullet vibe", "bullshit", "bullshits", "bullshitted", "bullturds", "bum", "bum boy", "bumblefuck",
    "bumclat", "bumfuck", "bummer", "bung", "bung hole", "bunga", "bunghole", "bunny fucker", "bust a load", "busty",
    "butchdike", "butchdyke", "butt", "butt fuck", "butt plug", "buttbang", "butt-bang", "buttcheeks", "buttface",
    "buttfuck", "butt-fuck", "buttfucka", "buttfucker", "butt-fucker", "butthead", "butthole", "buttman", "buttmuch",
    "buttmunch", "buttmuncher", "butt-pirate", "buttplug", "mother fucker", "fuck", "fuck it",
]

# Initialize the bot
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)

# Event for when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(activity=discord.Game(name="Your personal assistant for Discord"))
    while True:
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name="ready to answer your questions"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name="Here to improve your Discord experience"))

# Event for when a message is sent
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Check if the message contains any swear words or phrases
    for word in swear_words:
        if word.lower() in message.content.lower():
            error_message = await message.channel.send(f"{message.author.mention}, a message contains inappropriate language. Please do not use such words.")
            await message.delete()
            await asyncio.sleep(10)
            await error_message.delete()
            return

    # Check for more subtle swear words and phrases using regular expressions
    pattern = r'\b(?:' + '|'.join(swear_words) + r')\b'
    if re.search(pattern, message.content.lower()):
        error_message = await message.channel.send(f"{message.author.mention}, Your message contains inappropriate language. Please do not use such words.")
        await message.delete()
        await asyncio.sleep(10)
        await error_message.delete()
        return

    await bot.process_commands(message)

bot.run('Your-Discord-Token')