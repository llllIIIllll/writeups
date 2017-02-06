#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-14 09:50:57
# @Last Modified by:   john
# @Last Modified time: 2016-05-14 14:47:32

from pwnlib import *
from colorama import *
import time

host='104.196.3.198'
port=45429

init(autoreset=True)

master = tubes.remote.remote(host, port)

print master.recv()
# exit()
assignments = master.recv()
ports = [ line.split(' ')[-1] for line in assignments.split('\n')]
ports.pop()
ports = [ int(x) for x in ports ]

class Player:
	def __init__( self, number, port ):
		self.number = number
		self.s = tubes.remote.remote(host, port)
		self.devices = []
	def __del__(self):
		self.s.close()

	def say(self):
		return "PLAYER %d: %s" % (self.number, self.s.recv())

	def get_recent_devices(self):
		print self.recent

	def get_devices(self):
		original = self.s.recvuntil('!!!!!')
		devices = original
		devices = ''.join(devices.split("Your devices:")[1:])
		devices = ''.join(devices.split("-----")[0])
		self.devices = devices.split('\n')[1:-1]
		# print Fore.CYAN + ','.join(original.split('\n')[-5:])
		print "player %d devices:" % self.number
		print self.devices
		if self.number == 0:
			pass
		return ""

	def get_command(self):
		got = self.s.recv()
		print Fore.CYAN + got
		self.command = got.split('\n')[-2]
		print "player %d command: %s" % (self.number, self.command)

	def do_command(self, command):
		self.s.sendline(command.rstrip())
		response = self.s.recvuntil('km')
		responses = response.split('\n')
		
		if ('==== STAGE' in response):
			print Fore.RED + "WE HIT STAGE ONE"
			self.recent = response
			return -1

		for one in responses:
			if one != '\n' and one != '' and not one.startswith('FWOOSH') and not one.startswith('BRRR'):
				print Fore.YELLOW + "new command '%s'" % one
				# print Fore.MAGENTA + one
				self.command = one

		print Fore.GREEN + response

'''
# CREATE ALL PLAYERS
'''
players = {}
i = 0
for port in ports:
	players[i] = Player(i, port)
	# players[i].get_devices()
	print players[i].say()
	i += 1




# Start a level...

# get devices
for i in players:
	players[i].get_devices()
	
# get commands
for i in players:
	players[i].s.recvuntil('\n')
	players[i].command = players[i].s.recvuntil('\n').rstrip()
	print players[i].command

response = ""
while ( "COMPLETE" not in response ):
	# do commands
	for i in players:
		their_command = players[i].command
		for k in players:
			for device in players[k].devices:
				if device in their_command:
					print Fore.CYAN + "command sent for ", k
					players[k].s.sendline(their_command)
					# players[i].

	# After a command seen..
	for i in players:
		# if (players[i].s.can_recv(200)):
		response = players[i].s.recvuntil('\n').rstrip()
		responses = response.split('\n')
		print Fore.BLUE + response, i
		print ""
		for response in responses:
			if ( not response.startswith('FWOOSH') ):
				players[i].command = response
				print Fore.RED + "new command", response
				# print Fore.CYAN + players[i].s.recvuntil('\n')
			else:
				print Fore.GREEN + response

for i in players:
	print players[i].s.recvuntil('\n')