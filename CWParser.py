#!/usr/bin/env python
# -*- coding: utf-8 -*-

from CWFile import CWFile
from Textbox import Textbox


class CWParser:
    def __init__(self):
        self.cwFile = CWFile()
        self.commands = []
        self.ui_objects = []

    def parse(self):
        for command in self.commands:
            args = command.split(self.cwFile.DELIMITER_COMMAND)

            if args[0].strip() == Textbox.COMMAND:
                self.ui_objects.append(Textbox(args[1:len(args)]))

        for obj in self.ui_objects:
            print(obj.get_asp())
            print(obj.get_html())

    def read_cw_script(self, file_name):
        cw_file = open(file_name, "r")

        self.commands = []
        for line in cw_file:
            if line[0] != self.cwFile.COMMENT and line != "" and line != "\n":
                self.commands.append(line.strip())

        cw_file.close()
        return self.commands

    def show_cw_script(self):
        if not self.commands:
            return "empty command list"
        else:
            for command in self.commands:
                print(command)