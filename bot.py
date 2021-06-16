import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from random import randint, choice, SystemRandom
import sqlite3
import logging
import re
import os
import nationsgetter

Client = discord.Client(command_prefix="")
client = commands.Bot(command_prefix="")

# Public key = 3211516692bd81737602d0b32f65a2c063c6521bbe6e9725d90b3611c4528db1
# Applicatin = 854468746236526622
# Token = 
@client.event
async def on_message(message):
	if (client.user.id == message.author.id):
		return
	if (message.content.startswith("#getstats")):
		await message.channel.send("Récupération des informations en cours")
		text = nationsgetter.get_all_nations()
		await message.channel.send("```" + text + "```")

if __name__ == '__main__':
	import sys
	try:
		TOKEN = "ODU0NDY4NzQ2MjM2NTI2NjIy.YMkYCA.dhaIqVKU9Pycwl12rfw7owTjLAY"
	except:
		print('USAGE: python3 bot.py TOKENBOT')
		sys.exit(1)
	while (True):
		try:
			client.run(TOKEN)
		except:
			pass
		