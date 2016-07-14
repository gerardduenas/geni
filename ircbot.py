#!/usr/bin/python

from functions import *
from config import *

def main():
    check_config()
    irc = connect()
    while(True):
        text = irc.recv(4096)
        if text.len() <= 1:
            continue
        if text.find('PING') != -1:
            irc.send('PONG ' + text.split() [1] + '\r\n')
        for mark in cfg['marks']:
            if mark in text:
                parse_cmd(text)
    

if __name__ == "__main__":
    main()