#!/usr/bin/env python
# -*- coding: utf-8 -*-

from CabukWeb import CabukWeb


def main():
    try:
        cw_filename = "page.cw"
        cw_parser = CabukWeb(cw_filename)
        cw_parser.show_asp()

    except Exception:
        print("Arrrggh... exception!")

if __name__ == "__main__":
    main()