import socket
import re

class IRCBot:
    #A simple IRC Bot that pongs et all
    #Requires a call to 'run' to start
    lastline = ''
    def __init__( self, host = 'irc.freenode.net', channel = '#bmslug', nick = 'bmsbot', port = 6667, symbol = '$'):
        self.host = host
        self.channel = channel
        self.nick = nick
        self.port = port
        self.symbol = symbol
        self.socket = socket.socket()
        self.maxlength = 2048
        
        self.initConnection()
    
    
    def initConnection( self ):
        self.socket.connect( ( self.host, self.port ) )
        self.socket.send( "USER " + self.nick + " " + self.nick + " " + self.nick + " :bmsbot\n" )
        self.socket.send( "self.nick " + self.nick + "\r\n" )
        self.socket.send( "JOIN " + self.channel + "\r\n" )
        
        
    def nicklist( self ):
        self.socket.send( "NAMES " + self.channel + "\r\n" )
        #Implement parsing this
        
    def readlines( self ):
        lines = self.lastline + self.socket.recv( self.maxlength ).split( "\r\n" )
        self.lastline = lines.pop()
        return lines

    def run( self ):
        while True:
            lines = self.readlines()
            for line in lines:
                print line
        
    
    def pongToServer( self, msg ):
        #Check if "PING :" is in 'line' and call pongToServer
        pingcmd = msg.split( ":", 1 )
        pingmsg = pingcmd[ 1 ]
        self.socket.send( "PONG :" + pingmsg + "\r\n" )
    
    
    def privmsg( self, msg ):
        self.socket.send( "PRIVMSG " + self.channel + " :" + msg + "\r\n" )
        
        

if __name__ == "__main___":
    bot = IRCBot()
    bot.run()