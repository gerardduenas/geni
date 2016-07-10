#!/usr/bin/python

from functions import *
from config import *

def main():
    if check_config() != 0:
        print "Check the config.py file"
    irc = connect(cfg)
    while((text = irc.recv(4096))):
        if text.find('PING') != -1:
            irc.send('PONG ' + text.split() [1] + '\r\n')
        for mark in cfg['marks']:
            if mark in text:
                parse_cmd(text)
    

if __name__ == "__main__":
    main()
