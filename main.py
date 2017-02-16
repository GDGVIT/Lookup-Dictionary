import pyperclip
import json

dic = open("dictionary.json", 'r')
parsed = json.loads(dic.read())

print parsed[pyperclip.paste().upper()]

