#!/usr/bin/env python
# -*- coding: utf-8 -*-

# String in python is stored as unicode, by default utf-8
# To use a different kind of encoding, type # -*- coding: <encoding name> -*-

# Encode is to show the byte representation, e.g translate human character to bytes
# Decode is the opposite
# Python 3 no longer needs the u'text' expression

import sys

def InputToBytes():
	text = input("Please enter your text here: \n")
	binary = text.encode(sys.getdefaultencoding())
	return binary