#!/usr/bin/env python
# -*- coding: utf-8 -*-

from CWFile import CWFile
from Textbox import Textbox


class CabukWeb:
    def __init__(self, file_name):
        self.cwFile = CWFile()
        self.commands = []
        self.ui_objects = []
        # read script file
        if file_name != "":
            self.read_script(file_name)
        # parse script file
        self.parse()

    def parse(self):
        for command in self.commands:
            args = command.split(self.cwFile.DELIMITER_COMMAND)

            if args[0].strip() == Textbox.COMMAND:
                self.ui_objects.append(Textbox(args[1:len(args)]))

    def read_script(self, file_name):
        cw_file = open(file_name, "r")

        self.commands = []
        for line in cw_file:
            if line[0] != self.cwFile.COMMENT and line != "" and line != "\n":
                self.commands.append(line.strip())

        cw_file.close()
        return self.commands

    def get_html(self):
        code = ""
        for ui_object in self.ui_objects:
            code += ui_object.get_html() + "\n"

    def get_asp(self):
        code = ""
        for ui_object in self.ui_objects:
            code += ui_object.get_asp() + "\n"

    def show_script(self):
        if not self.commands:
            return "empty command list"
        else:
            for command in self.commands:
                print(command)

    def show_html(self):
        for obj in self.ui_objects:
            print(obj.get_html())

    def show_asp(self):
        for obj in self.ui_objects:
            print(obj.get_asp())