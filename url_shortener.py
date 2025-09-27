# %%
# pip install pyshorteners
# pip install pyperclip

import pyshorteners

url = input("Enter your URL: ")

def shorten_url(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shorten_url(url)