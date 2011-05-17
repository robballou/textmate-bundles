#!/usr/bin/env ruby

#
# Textmate command for inserting a random set of numbers
#
# Input: none
# Output: Insert as text

# based on: http://stackoverflow.com/questions/88311/how-best-to-generate-a-random-string-in-ruby
o = [(0..9)].map{|i| i.to_a}.flatten;  
string = (0..50).map{ o[rand(o.length)]  }.join;
print string.strip