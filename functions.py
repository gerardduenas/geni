#!/usr/local/bin/python

import socket
import time
import exceptions as e
from config import * 

def change_nick(irc)
    irc.send("NICK " + cfg['botnick'] + "\r\n")
    x = "_"
    while("Nickname is already in use" in irc.recv(4096)):
        irc.send("NICK " + nick + x + "\r\n")
        x += "_"
        time.sleep(1)

def check_config():
    for x,y in cfg.iteritems():
        if not y:
            if x not in cfg['optional_cfg']:
                raise e.ConfigError("Found an error in config.py file")
                         
def connect():
    '''Connects to the server through a socket,
    identifies the bot to the server and to NickServ'''
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket
    irc.connect((cfg['server'],cfg['port']))
    irc.send("USER " + cfg['botnick']  + " 8 * :" + cfg['realname'] + "\r\n")
    name_bot(cfg)
    irc.send("JOIN "+ cfg['channels'] +"\r\n")

def name_bot(irc):
    nick = change_nick(irc)
    irc.send("PRIVMSG nickserv :identify %s %s\r\n" % (cfg['botnick'], cfg['password']))
    
def parse_cmd(text):
    resp = text.split()