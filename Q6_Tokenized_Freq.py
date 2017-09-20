import re
from collections import OrderedDict

final_dict = {}
text = input("Enter the string: ")
text = text.replace("'"," '")
tokens = re.split(r'[\s?||!|:|;]|,\s|," |.\s', text)
for token in tokens:
        if token not in final_dict:
          final_dict[token] = 1
        else:
          final_dict[token] += 1

if ("" in final_dict.keys()):
  del final_dict['']

for key in final_dict:
  print (key, final_dict[key])
print (len(tokens))
print (len(final_dict))