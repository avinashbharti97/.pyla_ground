#! /usr/bin/python3

#mapit.py -reads address from command line and open that address in google map

import webbrowser, sys, pyperclip

if len(sys.argv)>1:
    address = ' '.join(sys.argv[1:])

else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/{}'.format(address))
