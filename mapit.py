#! /usr/bin/python3

#mapit.py -reads address from command line and open that address in google map

# -------install dependencies-------------
# $ pip install pyperclip
# $ sudo apt-get install xsel
# $ sudo apt-get install xclip

#--------how to use----------
#Method1
# -copy the desired address
# run the script

#method2
# pass the address in command line after the file name

import webbrowser, sys, pyperclip

if len(sys.argv)>1:
    address = ' '.join(sys.argv[1:])

else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/{}'.format(address))
