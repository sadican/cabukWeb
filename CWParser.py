#!/usr/bin/env python
# -*- coding: utf-8 -*-

from CWFile import CWFile
from Textbox import Textbox


class CWParser:
    def __init__(self):
        self.cwFile = CWFile()
        self.commands = []
        self.uiObjs = []

    def parse(self):
        for command in self.commands:
            args = command.split(self.cwFile.DELIMITER_COMMAND)

            if args[0].strip() == Textbox.COMMAND:
                self.uiObjs.append(Textbox(args[1:len(args)]))

        for obj in self.uiObjs:
            print
            obj.getASP()
            print
            obj.getHTML()

    def read_cw_script(self, file_name):
        cw_file = open(file_name, "r")

        self.commands = []
        for line in cw_file:
            if line[0] != self.cwFile.COMMENT and line != "" and line != "\n":
                self.commands.append(line.strip())

        cw_file.close()
        return self.commands

    def show_cw_script(self, file_name = ""):
        if self.commands == []:
            self.read_cw_script()
        else:
            for command in self.commands:
                print
                command