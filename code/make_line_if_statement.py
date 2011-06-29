#!/usr/bin/env python

"""
A textmate command to wrap the current line in an if statment.

Input: selected text or line
Output: insert as snippet
Key equiv: ctrl-i (or what you like!)
Scope selector: source

"""

import sys
import re

line = sys.stdin.read()

indent_pattern = r'^(\s*)(.*)$'
indent = ''
if re.match(indent_pattern, line):
	match = re.match(indent_pattern, line)
	indent = match.group(1)
	line = match.group(2)

sys.stdout.write("%sif (${1:condition}){ ${2:%s} }" % (indent, line))