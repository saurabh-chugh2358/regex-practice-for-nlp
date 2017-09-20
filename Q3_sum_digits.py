import re
 
regex = r"^\d{1,}$"
input_str = input("Enter a variable length number: ")
 
def digit_sum(n):
  total = 0
  while n>0:
	total += n%10
	n = n//10
  return total
 
matches = re.search(regex, input_str)
if matches:
	print ("Match was found at {start}-{end}: {match}".format(start = matches.start(), end = matches.end(), match = matches.group()))
	print (digit_sum(int(input_str)))
else:
  print ("Input is not a valid variable length number")
 
