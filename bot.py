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
		TOKEN = ""
	except:
		print('USAGE: python3 bot.py TOKENBOT')
		sys.exit(1)
	while (True):
		try:
			client.run(TOKEN)
		except:
			pass
		