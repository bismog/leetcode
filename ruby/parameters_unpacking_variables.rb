# http://stackoverflow.com/questions/27453569/using-gets-gives-no-such-file-or-directory-error-when-i-pass-arguments-to-my/27453657
# you want to the user to type some input by reading a line from STDIN, the 
# best way to do this is by calling STDIN.gets and not gets. 

first, second, third = ARGV

puts "The script is called: #{$0}"
puts "Your first variable is: #{first}"
puts "Your second variable is: #{second}"
puts "Your third variable is: #{third}"

print "More input:"
more_input = STDIN.gets.chomp()
puts "Okay, your input is: #{more_input}"
