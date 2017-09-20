import re
 
text = input("Enter the string: ")
text = text.replace("'"," '")
tokens = re.split(r'[\s?||!|:|;\"]|,\s|,"', text)
for token in tokens:
    	print(token)