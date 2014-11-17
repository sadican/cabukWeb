#!/usr/bin/env python
# -*- coding: utf-8 -*-

from CWFile import CWFile

class Textbox:
	COMMAND = "textbox"
	PREFIX = "tb_"

	ARG_OBJ_ID = "id"
	ARG_CSS_CLASS = "cssClass"
	ARG_IS_REQUIRED = "isRequired"
	ARG_INPUT_SIZE = "inputSize"
	ARG_PLACEHOLDER = "placeholder"

	def __init__ (self, args):
		self.setDefaults()
		for arg in args:
			# split arg key - value
			tempArg = arg.split(CWFile.DELIMITER_ARG)
			argName = tempArg[0]
			argValue = tempArg[1]

			if argName == self.ARG_OBJ_ID:
				self.objID = self.PREFIX + argValue
			elif argName == self.ARG_CSS_CLASS:
				self.cssClass = argValue
			elif argName == self.ARG_IS_REQUIRED:
				self.isRequired = argValue
			elif argName == self.ARG_INPUT_SIZE:
				self.inputSize = argValue
			elif argName == self.ARG_PLACEHOLDER:
				self.placeholder = argValue

	def setDefaults(self):
		self.objID = self.PREFIX
		self.cssClass = "form-control"
		self.isRequired = False
		self.inputSize = 128
		self.placeholder = ""

	def getHTML(self):
		code = "<input "
		code += "id=" + "\"" + self.objID + "\" "
		code += "class=" + "\"" + self.cssClass + "\" "
		if self.placeholder != "":
			code += "placeholder=" + "\"" + self.placeholder + "\" "
		code +=">"
		return code

	def getASP(self):
		code = "<asp:TextBox "
		code += "id=" + "\"" + self.objID + "\" "
		code += "CssClass=" + "\"" + self.cssClass + "\" "
		if self.placeholder != "":
			code += "placeholder=" + "\"" + self.placeholder + "\" "
		code += "runat=\"server\" "
		code += "></asp:TextBox>"
		return code 