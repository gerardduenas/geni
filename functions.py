#!/usr/local/bin/python

import socket
import ssl
import time

def new_socket(server, port)
    irc_C = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket
    irc = ssl.wrap_socket(irc_C) #wraps the socket in ssl
    irc.connect((server, port))
    irc.setblocking(False)
    #Connect to server
    if server_password: #optional
        irc.send("PASS %s\r\n" % (server_password))
    irc.send("USER " + botnick + " " + botnick + " " + botnick + " :meLon-Test\r\n")
    irc.send("NICK "+ botnick +"\n")
    irc.send("PRIVMSG nickserv :identify %s %s\r\n" % (botnick, password))
    irc.send("JOIN "+ channel +"\n")


for i, tail in enumerate(tail_files):
    tail_line.append('')


while True:
    time.sleep(2)

    # Tail Files
    for i, tail in enumerate(tail_files):
        try:
            f = open(tail, 'r')
            line = f.readlines()[-1]
            f.close()
            if tail_line[i] != line:
                tail_line[i] = line
                irc.send("PRIVMSG %s :%s" % (channel, line))
        except Exception as e:
            print "Error with file %s" % (tail)
            print e

    try:
        text=irc.recv(2040)
        print text

        # Prevent Timeout
        if text.find('PING') != -1:
            irc.send('PONG ' + text.split() [1] + '\r\n')
    except Exception:
        continue
