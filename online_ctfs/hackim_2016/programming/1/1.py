#!/usr/bin/env python

from twython import Twython

twitter = Twython(  '1h9UJyNZEaS0vP7LNx7hOlBm5',
					'Pa4X8jay4Cw71WWtRP3bho3rZCKTcuMCwzyMsDDnZs4KBuoch6',
					'3122875095-sqYpWKiFEqnJIaOgllZtIcbCSNyNaIaQM06DnBN',
					'GPNNZ0Z7w3QfcVyeSo9K3bwmOZ87FpyBV5MrjsstqDoPN',
				 )

responses = twitter.search(q='Tandoori Chicken never', count =900)['statuses']

for response in responses:

	print response['user']['name'] + "(" + response['user']['screen_name'] + ") tweeted:  " + response['text']
	print "="*80
	

# The answer was @anyahotels... the last tweet we saw when we ran our script