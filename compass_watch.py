#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import settings
from subprocess import Popen, PIPE, STDOUT
from django.core.management  import setup_environ
setup_environ(settings)

if not hasattr(settings, 'COMPASS_DIRS'):
	print "There's no COMPASS_DIRS tuple defined in your settings.py"
	exit()

print "%s directories to watch..." % (len(settings.COMPASS_DIRS),)
for compass_folder in settings.COMPASS_DIRS:
	if ('config.rb' in os.listdir(compass_folder)):
 		command = "compass watch %s &" % (compass_folder,)
		compass_process = Popen(command, shell=True, executable=None, stdin=None, stdout=None, stderr=PIPE)
		error_list = ""
		for line in compass_process.stderr:
			error_list += line.rstrip("\n")
		if error_list == "":
			print "watching directory %s ..." % (compass_folder,)
		else:
			print "error(s) when trying to watch directory %s:\n %s" % (compass_folder, error_list)