## whereami.py #################################################################
## define stuff based on where I ams ###########################################
################################################################################
import os, platform

if(platform.system() == "Linux"):
	def spam():
		print "spam selecting a spam linux"
else:
	def spam():
		print "spam selecting a spam not linux"
