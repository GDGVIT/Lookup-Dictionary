import pyperclip
import json

dic = open("dictionary.json", 'r')
parsed = json.loads(dic.read())

x = pyperclip.paste().upper()
print 'Parsed : '
print parsed[x]
