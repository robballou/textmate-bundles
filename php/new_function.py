#!/usr/bin/env python

"""
Create a new function based on the current line

Input: Selected Text or Line
Output: Insert as Snippet

Examples:

Line: myFunction
Output: a function with the name myFunction

Line: myFunction($param)
Output: a function with the name myFunction and $param in the function comment

Line: isSomething
Output: a function that returns false by default and has "@return bool" in the function comment

Line: getSomething
Output: a function that returns a variable and has "@return" in the function comment
"""

from os import environ as env
import re

name = env['TM_CURRENT_WORD']
line = env['TM_CURRENT_LINE']

# snippet pieces
comment_mixed = """/**\n * @return ${3:mixed}\n */\n"""
function = """${1:public} function """

# regexs
line_with_params = re.compile(r'^(\s*)([\w\d]+)\((.+)?\)$')
var = '\$[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*'
variable = re.compile(var)

# figure out starting whitespace for the line
groups = re.match(r'^(\s*).*$', line)
whitespace = groups.group(1)

def indent(snippet, whitespace):
	lines = snippet.splitlines()
	lines = ["%s%s" % (whitespace, line) for line in lines]
	return "\n".join(lines)

# match the lines
line = line.replace('$', '\$')
if line_with_params.match(line):
	# the line seems to define a function with params
	matched = line_with_params.search(line)
	name = matched.group(2)
	params = matched.group(3)
	params_comment = " * \n"
	if params:
		# parse params
		all_params = variable.findall(params)
		params_comment = "".join([" * @param %s\n" % param.replace('$', '\$') for param in all_params])
	print indent("/**\n%s * @return ${4:mixed}\n */\n%s${2:%s}(${3:%s}){\n\t$0\n}" % (params_comment, function, name, params), whitespace)
else:
    # guess something about the function based on the word (the function has no params)
	if name.startswith("is"):
		print indent("/**\n * @return bool\n */\n%s${2:%s}(){\n\t$0return false;\n}" % (function, name), whitespace)
	elif name.startswith("get"):
		print indent("%s%s${2:%s}(){\n\t$0return ${4:\$${5:var}};\n}" % (comment_mixed, function, name), whitespace)
	else:
		print indent("%s%s${2:%s}(){\n\t$0\n}" % (comment_mixed, function, name), whitespace)