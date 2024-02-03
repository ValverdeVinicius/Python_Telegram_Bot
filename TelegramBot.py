''''Para utilizar o script, é necessário instalar a biblioteca:
			pip install pyTelegramBotAPI
		Para rodar o script no Linux, rode o comando:
			python3 ./TelegramBot.py
'''

import requests
import re, random
import telebot

BOT_TOKEN = ''

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
	bot.reply_to(message, """Welcome to Dark Web OSINT 
	/darkweb (search)
	Example: /darkweb credit cards
	Created by VV
								""")

@bot.message_handler(commands=['darkweb', 'getonions'])
def send_welcome(message):
	bot.reply_to(message,"[+] Getting Links")
	data = message.text
	newData = data.replace('/darkweb', '')
	bot.reply_to(message, scrape(newData))
	bot.reply_to(message,"[!] You Need TOR To Access Onion Links")

def scrape(newData):
	yourQuery = newData
	#yourQuery = "Croatia Index Of"

	if " " in yourQuery:
		yourQuery = yourQuery.replace(" ","+")
	url = "https://ahmia.fi/search/?g={}".format(yourQuery)
	request = requests.get(url)
	content = request.text
	regexQuery = "\w+\.onion"
	mineData = re.findall(regexQuery, content)
	
	n = random.randint(1,9999)
	
	fileName = "sites{}.txt".format(str(n))
	print("Saving to...", fileName)
	mineData = list(dict.fromkeys(mineData))
	
	with open(fileName, "w+") as _:
		print("")
	for k in mineData:
		with open(fileName, "a") as newFIle:
			k = k + "\n"
			newFIle.write(k)
	print("All the files written to a text file: ", fileName)

	with open(fileName) as input_file:
		head = [next(input_file) for _ in range(7)]
		contents = '\n'.join(map(str, head))
		print(contents)
		
	return contents

bot.infinity_polling()

