#!/usr/bin/env ruby

#
# Textmate item to increment all numbers in a selection
#
# If you have:
#
#   line1
#   line1
#   line1
#
# You can run this to get:
#
#   line1
#   line2
#   line3
#
# Input: Selected Text or Document
# Output: Replace Selected Text
#
text = ENV['TM_SELECTED_TEXT']

starting_num = nil
current_num = nil
text.each do |line|
	numbers = line.scan(/\d+/)
	if starting_num == nil
		starting_num = numbers[0].to_i
		current_num = numbers[0].to_i
	else
		current_num = current_num + 1
		line = line.gsub(starting_num.to_s, current_num.to_s)
	end
	puts line
end