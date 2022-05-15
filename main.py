import discord
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

client = discord.Client()
load_dotenv()
pfp = './barry.png'
fp = open(pfp, 'rb')
pic = fp.read()


@client.event
async def on_ready():
    await client.user.edit(avatar=pic)
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$gang'):
        await message.channel.send('Hi everyone, gang gang here again, if yall having a bad day just remember that <@536596722680463402> invested in csgo keys')

    if message.content.startswith('$senor'):
        await message.channel.send('Hi everyone, gang gang here again, lets have a round of applause for Señor nangu <@304619196925607938>')


keep_alive()
client.run(os.getenv('TOKEN'))
