#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Documentation of the markdown to html module"""

import sys
import os.path

args = sys.argv[1:]

if (len(args) < 2):
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    sys.exit(1)
elif (len(args) >= 3):
    sys.stderr.write("Too many arguments\n")
    sys.exit(1)
else:
    # for arg in args:
    #     if os.path.isfile(arg) != True:
    #         sys.stderr.write("Missing {}\n".format(arg))
    #         sys.exit(1)
    first_file = args[0]
    if first_file.endswith('.md') is True:
        if os.path.isfile(first_file) is not True:
            sys.stderr.write("Missing {}\n".format(first_file))
            sys.exit(1)
    sys.exit(0)
