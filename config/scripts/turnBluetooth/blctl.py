#!/usr/bin/env python3
import sys
import subprocess

ARGS = sys.argv

USAGE ='''
USAGE: sudo blctl [start/stop/restart] 
'''

if len(ARGS) < 2 or len(ARGS) > 2:
	print(USAGE) 
else:
	if ARGS[1] not in ['start', 'stop', 'restart']:
		print(USAGE)
	else:
		subprocess.run(['systemctl', ARGS[1], 'bluetooth'])
		if ARGS[1] in ['start', 'restart']:
			subprocess.run('blueman-manager')
