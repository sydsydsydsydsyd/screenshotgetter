#!/usr/local/bin/python3


from os import system
from random import randint

# initial url
url = "https://prnt.sc/"

#add random character to the url r number of times
for i in range(2):
    url += chr(randint(
        ord('a'), ord('z') + 1
    ))

for j in range(4):
    url += str(randint(0, 10))

system(f"open {url}")
system(f"xdg-open {url}")
