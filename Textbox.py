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

    def __init__(self, args):
        self.obj_id = self.PREFIX
        self.css_class = "form-control"
        self.is_required = False
        self.input_size = 128
        self.placeholder = ""
        # create object
        self.create(args)

    def create(self, args):
        if len(args) < 1:
            return
        else:
            for arg in args:
                # split arg key - value
                temp_arg = arg.split(CWFile.DELIMITER_ARG)
                arg_name = temp_arg[0]
                arg_value = temp_arg[1]

                if arg_name == self.ARG_OBJ_ID:
                    self.obj_id = self.PREFIX + arg_value
                elif arg_name == self.ARG_CSS_CLASS:
                    self.css_class = arg_value
                elif arg_name == self.ARG_IS_REQUIRED:
                    self.is_required = arg_value
                elif arg_name == self.ARG_INPUT_SIZE:
                    self.input_size = arg_value
                elif arg_name == self.ARG_PLACEHOLDER:
                    self.placeholder = arg_value

    def get_html(self):
        code = "<input "
        code += "id=" + "\"" + self.obj_id + "\" "
        code += "class=" + "\"" + self.css_class + "\" "
        if self.placeholder != "":
            code += "placeholder=" + "\"" + self.placeholder + "\" "
        code += "maxlength=" + "\"" + self.input_size + "\" "
        code += ">"
        return code

    def get_asp(self):
        code = "<asp:TextBox "
        code += "id=" + "\"" + self.obj_id + "\" "
        code += "CssClass=" + "\"" + self.css_class + "\" "
        if self.placeholder != "":
            code += "placeholder=" + "\"" + self.placeholder + "\" "
        code += "MaxLength=" + "\"" + self.input_size + "\" "
        code += "runat=\"server\" "
        code += "></asp:TextBox>"
        return code