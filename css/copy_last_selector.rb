#!/usr/bin/env ruby

# Textmate snippet for creating a dynamic snippet of the last selector on the current line
# of CSS.
#
# == Examples of selection
#
#     .something { ... }
#     # =>
#     .something, .${1:something} { ... }
#     
#     a:link { ... }
#     # =>
#     a:link, a:${1:link} { ... }
#     
#     div a { ... }
#     # =>
#     div a, div ${1:a} { ... }
#
# Input: selected text or line
# Output: Insert as Snippet

# try to guess what the part of the selector we should "select" in the snippet
def guess_selection(selector)
	if selector =~ / /
		# the selector has "words" so select the last piece
		selector = selector.split
		selector[selector.length - 1] = guess_selection(selector.last)
		return selector.join(" ")
	elsif selector =~ /(.+)?([.:#])([A-Za-z0-9]+)$/
		# the selector is just a class selector
		return "#$1#$2${1:#$3}"
	end
	return selector
end

# read the current line
current_line = STDIN.read

# some regexs for later
re_selectors = /^([^{]+)\{/
re_everything_else = /\{(.+)$/

# using the regex spilt the line into selectors and properties
selectors = re_selectors.match current_line
properties = re_everything_else.match current_line

# pull the existing selectors, and then pull the last selector from the last
existing_selectors = selectors[1]
last_selector = guess_selection(existing_selectors.split(',').last.strip)

print "#{existing_selectors.strip}, #{last_selector}$0 {#{properties[1]}"