#!/usr/bin/env python

"""
Reverse selected lines (or document lines)

A simple bundle command to reverse the selected lines in
a document.

Input: Selected Text or Document
Ouput: Replace Selected Text

"""

import sys

lines = sys.stdin.readlines()
lines.reverse()
for line in lines:
	print line.strip()
