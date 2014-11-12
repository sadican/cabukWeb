#!/usr/bin/env python
# -*- coding: utf-8 -*-

class CWParser:
	""" CabukWeb script parser """
	
	def __init__(self):
		print('hobarey!')
	
	def readFile(self, cwFileName, cwFileExtension):
		cwFile = open(cwFileName + "." + cwFileExtension, "r", encoding="utf8")
		
		commands = []
		for line in cwFile:
			commands.append(line)
			print(line)		
		
		cwFile.close()
		
if __name__ == '__main__':
	cwparser = CWParser()
	cwFileName = "page"
	cwFileExtension = "cw"
	
	print("processing...")
	cwparser.readFile(cwFileName, cwFileExtension)
	print("\n")
