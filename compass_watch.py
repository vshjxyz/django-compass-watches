#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import settings
from django.core.management  import setup_environ
setup_environ(settings)

if not hasattr(settings, 'COMPASS_DIRS'):
	print "There's no COMPASS_DIRS tuple defined in your settings.py"
	exit()

print "%s directories to watch..." % (len(settings.COMPASS_DIRS),)
for compass_folder in settings.COMPASS_DIRS:
	if ('config.rb' in os.listdir(compass_folder)):
 		command = "compass watch %s &" % (compass_folder,)
		subprocess.Popen(command, shell=True)
		if True:
			print "watching directory %s ..." % (compass_folder,)
		else:
			print "error when trying to watch directory %s: %s" % (compass_folder, output)

