#! /usr/bin/python3

#mapit.py -reads address from command line and open that address in google map

import webbrowser, sys

if len(sys.argv)>1:
    address = ' '.join(sys.argv[1:])
    webbrowser.open('https://avinashbharti97.github.io/{}'.format(address))
