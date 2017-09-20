import re
from collections import OrderedDict

final_dict = {}
text = input("Enter the string: ")
text = text.replace("'"," '")
tokens = re.split(r'[\s]', text)
for token in tokens:
        if token not in final_dict:
          final_dict[token] = 1
        else:
          final_dict[token] += 1

if ("" in final_dict.keys()):
  del final_dict['']

sorted_dict = OrderedDict(sorted(final_dict.items()))

for key in sorted_dict:
  print (key, sorted_dict[key])
print (len(tokens))
print (len(sorted_dict))
 
