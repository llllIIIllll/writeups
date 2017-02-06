#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-14 09:50:57
# @Last Modified by:   john
# @Last Modified time: 2016-05-14 14:10:18

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


def stage1():
	for i in players:
		print Fore.BLUE + players[i].say()

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

level = 0
while True:
	'''
	# GET ALL PLAYERS DEVICES
	'''
	for i in players:
		# if level == 0:
		if ( i == 0 and level == 0):
			print Fore.YELLOW + players[i].say()
			print Fore.CYAN + players[i].get_devices()	
			time.sleep(4)
		else:
			print Fore.CYAN + players[i].get_devices()
		# else:
		# 	print players[i].get_recent_devices()


	'''
	# GET ALL PLAYERS COMMANDS
	'''
	for i in players:
		if i == 0:
			print players[i].s.recv()
		players[i].get_command()

	'''
	# DO EACH PLAYER'S COMMANDS
	'''

	stage = 0
	while stage == 0:
		if stage == 0:
			for i in players:
				if stage == 0:
					their_command = players[i].command
					for k in players:
						if stage == 0:
							each_player = players[k]
							for device in each_player.devices:
								if stage == 0:
									if device in their_command:
										print "player %d has the device %s to '%s'" % (k, device, their_command)
										response = each_player.do_command(their_command)
										if response == -1:
											stage = 1
											level += 1
											break
			if stage == 0:
				for i in players:
					new_command = players[i].s.recv().split('\n')[0].rstrip()
					print new_command
					if new_command == '\n':
						pass
						# no new command
						# print "NO NEW COMMAND", new_command
					else:
						print Fore.YELLOW + "new_command", new_command
						players[i].command = new_command

	print "WE ARE NOW AT A NEW STAGE"
	
master.close()