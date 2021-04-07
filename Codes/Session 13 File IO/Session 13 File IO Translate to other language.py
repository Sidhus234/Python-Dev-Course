# read data from a text file, and convert it to Japanese

from translate import Translator

import os

os.chdir('C:/Users/sidhu/OneDrive/Desktop')

with open('test.txt', mode='r+') as my_file:
    data = my_file.readlines()

print(data)

translator= Translator(to_lang="zh")
translation = translator.translate(data[0])
print(translation)