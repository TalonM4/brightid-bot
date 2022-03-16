import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

m = None
channel = None

@client.event
async def on_ready():
    global channel
    global m
    print("Ready")
    guild = discord.utils.get(client.guilds, id=596752664906432522)
    channel = discord.utils.get(guild.channels, id=759136917668364308)
    messages = await channel.history(limit=50).flatten()
    for message in messages:
        if message.content == "Using the verify command does not verify you. Check <#759203398213566506> to learn how to get verified":
            await message.delete()
    m = await channel.send(
        "Using the verify command does not verify you. Check <#759203398213566506> to learn how to get verified")

@client.event
async def on_message(message):
    global m
    global channel
    if message.channel.id == 759136917668364308:
        if message.content !=  "Using the verify command does not verify you. Check <#759203398213566506> to learn how to get verified":
            if message.author.id != 933478527469236234:   # this might need to change based on the bot token
                await m.delete()
                m = await channel.send(
                "Using the verify command does not verify you. Check <#759203398213566506> to learn how to get verified")


client.run(os.environ["bot"])
