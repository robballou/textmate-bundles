#!/usr/bin/env ruby

#
# Textmate command for inserting a random string
#
# Input: none
# Output: Insert as text

# based on: http://stackoverflow.com/questions/88311/how-best-to-generate-a-random-string-in-ruby
o = [('a'..'z'),('A'..'Z')].map{|i| i.to_a}.flatten;  
string = (0..50).map{ o[rand(o.length)]  }.join;
print string.strip