#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# @Author: caleb
# @Date:   2016-05-14 13:58:29
# @Last Modified by:   caleb
# @Last Modified time: 2016-05-14 14:49:11
import sys
from pwn import *
import threading
import queue

REMOTE_ADDRESS = '104.196.3.198'

class CosmoPlayer(threading.Thread):

	queue = None
	conn = None
	player = -1
	devices = []
	players = []

	def __init__(self, player, port, queue):
		super(CosmoPlayer, self).__init__()
		self.queue = queue
		self.conn = remote(REMOTE_ADDRESS, port)
		self.player = player

	def message(self, message):
		if len(message.split('the')) != 2:
			return
		device = message.split('the')[1].strip()
		if device in self.devices:
			print 'Player {0}: sending message "{1}"'.format(self.player, message)
			self.conn.send(message + '\n')

	def run(self):
		while True:
			line = self.conn.recvuntil('\n').rstrip()
			if line == "GO!!!!!":
				while True:
					message = self.conn.recvuntil('\n').rstrip()
					if message.startswith('FWOOSH'):
						continue
					if message.startswith('==== STAGE '):
						break
					print 'Player {0}: recieved message "{1}"'.format(self.player, message)
					for player in players:
						player.message(message)
			elif line.startswith('STAGE '):
				self.conn.recvuntil('Your devices:\n')
				self.devices = []
				line = self.conn.recvuntil('\n').rstrip()
				while line != '-----':
					self.devices.append(line)
					line = self.conn.recvuntil('\n').rstrip()
			else:
				print 'Player {0}: recieved message "{1}"'.format(self.player, line)
				pass
		# while True:
		# 	message = self.queue.get()
		# 	process_message(message)
		# 	q.task_done()

main = remote(REMOTE_ADDRESS,45429)
trash = main.recvuntil('cybernauts!\n')
ports = []
players = []
for i in range(8):
	port = int(main.recvuntil('\n').split(' ')[5])
	player = CosmoPlayer(i, port, None)
	players.append(player)
	ports.append(port)

for player in players:
	player.players = players
	player.start()

while True:
	print 'Main Thread: {0}'.format(main.recvuntil('\n'))