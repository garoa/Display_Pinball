import sys
import socket
import string
import os #not necassary but later on I am going to use a few features from this

HOST='irc.freenode.net' #The server we want to connect to
PORT=6667 #The connection port which is usually 6667
NICK='dmdbot' #The bot's nickname
IDENT='pybot'
REALNAME='dotmatrix'
OWNER='JucaBlues' #The bot owner's nick
CHANNELINIT='#hackerspace-sp' #The default channel for the bot
readbuffer='' #Here we store all the messages from server

import serial
ser = serial.Serial(port="/dev/ttyUSB0")

ser.setBaudrate(19200)
ser.write("M")
ser.write(28*" ")
ser.write(28*" ")

msg1 = ""
msg2 = ""

def dmdcmd(commandline,channel):
	print commandline
	global msg1,msg2,ser
	msg1 = msg2
	msg2 = commandline
	ser.write("M")
	ser.write("%28s" % msg1.upper().strip()[:28])
	ser.write("%28s" % msg2.upper().strip()[:28])
	return 0 

def dmd_enablescroll():
	global ser
	ser.write("S")

def dmd_disablescroll():
	global ser
	ser.write("s")

def parsemsg(msg):
	complete=msg[1:].split(':',1) #Parse the message into useful data
	info=complete[0].split(' ')
	msgpart=complete[1]
	sender=info[0].split('!')

	if msgpart.startswith("dmdbot:-S") or msgpart.startswith("dmdbot:--enable-scroll"):
		dmd_enablescroll()
		return

	if msgpart.startswith("dmdbot:-s") or msgpart.startswith("dmdbot:--disable-scroll"):
		dmd_disablescroll()
		return

	if msgpart.startswith("dmdbot:"):
		dmdcmd(msgpart.replace("dmdbot:",""),info[2])

#Connecting to the server:

s=socket.socket( ) #Create the socket
s.connect((HOST, PORT)) #Connect to server
s.send('NICK '+NICK+'\n') #Send the nick to server
s.send('USER '+IDENT+' '+HOST+' bla :'+REALNAME+'\n') #Identify to server

while 1:
	line=s.recv(500) #recieve server messages
	print line #server message is output
	if line.find('Welcome to the')!=-1:
		s.send('JOIN '+CHANNELINIT+'\n') #Join a channel
	if line.find('PRIVMSG')!=-1:
		parsemsg(line)
		line=line.rstrip() #remove trailing 'rn'
		line=line.split()
		if(line[0]=='PING'): #If server pings then pong
		  s.send('PONG '+line[1]+'\n')

