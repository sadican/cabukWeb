#!/usr/bin/env python
# -*- coding: utf-8 -*-

class CWParser:
	""" CabukWeb script parser """
	CW_FILE_COMMENT = "#"
	
	def __init__(self):
		print('hobarey!')
	
	def readCWContent(self, cwFileName):
		cwFile = open(cwFileName, "r", encoding="utf8")
		
		commands = []
		for line in cwFile:
			if (line[0] != self.CW_FILE_COMMENT):
				commands.append(line)
		
		cwFile.close()
		return commands
		
if __name__ == '__main__':
	cwparser = CWParser()
	cwFileName = "page.cw"
	
	print("processing...")
	cwparser.readCWContent(cwFileName)
	print("\n")
