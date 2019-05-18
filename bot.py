#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmpp
from jaber_bot import JabberBot
from message_text import *
from comand_parser import *
import os

config = { #имя пользователя и пароль для подключения
'jid': 'job-rdp-shop@xmpp.jp',
'pass': 'M0de$t201809@'
}

#def start_menu(user,text):
#	if text == "!help":
#		return "\n Добрый день: {}\n {}".format(user, HELP_MESSAGE)
#	elif text == "!about" :
#		return "\n{}".format(ABOUT_MESSAGE)
#	elif text == "!price" :
#		return "\n{}".format(PRICE_MESSAGE)
#	elif text == "!whois" :
#		#return os.execl("/usr/bin/whois ","{}".format(text))
#		print(text)
#	else:
		#print(text)
#		return EROR_MESSAGE

def message_handler(conn, mess): #вызывается при входящем сообщении,
	text = mess.getBody() #получаем текст сообщения, отправителя
	user = mess.getFrom() #получаем  отправителя
	#reply = text 
	reply = start_menu(user,text)
	conn.send(xmpp.Message(mess.getFrom(), reply)) # отправляем
	#conn.send(xmpp.Message('admin-rdp-shop@xmpp.jp','text to spamm')) # отправляем для спама
bot = JabberBot(config['jid'], config['pass'])
bot.register_handler('message', message_handler)
bot.start()