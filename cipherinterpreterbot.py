import discord
import logging
from complexciphercore import convert

logging.basicConfig(level=logging.INFO)

import discord

token = 'NDkxOTMxNTg1MzIzNTk3ODM1.DoPERA.mgg0RKedZH_oHpzs0FgXxRy2X3M'
channel = '491938711693426688' #secret-codes

client = discord.Client()

@client.event
async def on_message(message):
    content = message.content

    if message.author == client.user:
        return

    print("\nChecking message by %s in %s..." % (message.author,message.channel))

    if int(content[0:(int(content[0]) + 1)]) in range(11,99999):
        msg = ('{0.author.mention} said in %s:\n```%s```' % (message.channel, convert(content,'decode'))).format(message)
        await client.send_message(client.get_channel(channel),msg)
        print("Succesfully decoded.")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(token)
