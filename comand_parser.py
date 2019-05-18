#! /usr/bin/env python
# -*- coding: utf-8 -*-
from message_text import *
import os

def start_menu(user,text):
	print(user,text)
	#print("len",len(text))
	try:
		if text[0] == "!":
			if text[1:7] == u"помошь":
				return HELP_MESSAGE
			elif text[1:5] == u"цены":
				return PRICE_MESSAGE
			elif text[1:6] == u"оботе":
				return ABOUT_MESSAGE
#			elif text[1:6] == "whois":
#				print(os.execv("/usr/bin/whois",text[7:len(text)]))
	#			return "help_msg"
			elif text[1:8] == u"справка":
				return INFO_MESSAGE
	#		elif text[1:6] == "about":
	#			return "help_msg"
			else :
				return EROR_MESSAGE
		else :
			return text
	except:
		print(user,text)


if __name__ == '__main__':
	while 1==1:
		text = input("ввод: ")
		print(parse_cmd(text))