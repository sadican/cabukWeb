#!/usr/bin/env python
# -*- coding: utf-8 -*-

from CWParser import CWParser

CW_FILENAME = "page.cw"

cwParser = CWParser()
cwParser.readCWContent(CW_FILENAME)
cwParser.showCWContent()
cwParser.parse()