# -*- coding: utf-8 -*-
from machine import *
from time import *
from onewire import *
from ds18x20 import *
import socket


#~ light = Pin(12, Pin.IN)

ds = DS18X20(OneWire(Pin(4)))
roms = ds.scan()

moisture = ADC(0)
water = Pin(5, Pin.OUT)

water.low()

while True:
	if moisture.read() <= 200:
		water.high()
		sleep(1)
		water.low()
	try:
		ds.convert_temp()
		temperature = ds.read_temp(roms[0])
	except:
		temperature = 0
	param = 'l=%i&t=%i&w=%i'%(0, int(temperature), moisture.read())#light.value()
	print(param)

	s = socket.socket()
	addr = socket.getaddrinfo('iot.gabbler.ru', 80)[0][-1]
	s.connect(addr)
	s.send(bytes('POST /iot/flower HTTP/1.1\r\nHost: iot.gabbler.ru\r\nContent-Type: application/x-www-form-urlencoded\nContent-Length: %s\r\n\r\n%s\r\n'%(len(param), param), 'utf8'))
	s.recv(1024)
	s.close()

	try:
		s = socket.socket()
		addr = socket.getaddrinfo('bastax.me', 80)[0][-1]
		s.connect(addr)
		s.send(bytes('POST /flower/info HTTP/1.1\r\nHost: bastax.me\r\nContent-Type: application/x-www-form-urlencoded\nContent-Length: %s\r\n\r\n%s\r\n'%(len(param), param), 'utf8'))
		s.recv(1024)
		s.close()
	except:
		print('Bixnel error')


	sleep(4.83)
