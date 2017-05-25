#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tornado.template import *
from tornado.ioloop import *
from tornado.web import *
import random
import string
import sqlite3
import json


class Api(RequestHandler):
	def get(self):
		c = con.cursor()
		c.execute("SELECT * FROM info ORDER BY id DESC LIMIT 1")
		idd, date, temperature, light, water = c.fetchone()
		if water <= 200:
			nw = 'нужно'
		else:
			nw = 'не нужно'
		self.write(json.dumps({'temperature': temperature, 'light': light, 'water': water, 'date': date[11:], 'need_water': nw}))

	def post(self):
		try:
			#~ passwd = self.get_argument('passwd')
			#~ if passwd != str(totp.now()):
				#~ self.write('Invalid one-time password')
			#~ elif passwd == str(totp.now()):
			temperature = self.get_argument('t')
			light = self.get_argument('l')
			water = self.get_argument('w')
			print(temperature,light,water)
			con = sqlite3.connect('growing-flower.db')
			c = con.cursor()
			c.execute("INSERT INTO info(temperature,light,water) VALUES(%s,%s,%s)"%(temperature,light,water))
			con.commit()
		except:
			self.write('Error')


application = Application([
	(r"/flower/info", Api),
])


if __name__ == "__main__":
	con = sqlite3.connect('growing-flower.db')
	application.listen(1025)
	IOLoop.current().start()
	con.close()
