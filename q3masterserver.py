# Q3MasterServer
# Copyright (C) 2015 PtitBigorneau
#
# PtitBigorneau - www.ptitbigorneau.fr
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#

__author__  = 'PtitBigorneau'
__version__ = '1.0'

import socket

try:
    from socket import inet_ntop as inet_ntop
except ImportError:
    from dns.inet import inet_ntop as inet_ntop

class Q3masterServer:

    def __init__(self, host, port):

        packet_prefix = '\xff' * 4
        responses = []
        self.serverslist = []
	
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((host, port)) 
        s.settimeout(2)

        cmd = packet_prefix+'getservers  68 full empty demo'
        
        s.send(cmd)

        while True:
    
            try:
                response = s.recv(1395)
            except:
                break
            
            if not response :
                break
            else:
                responses.append(response)

        for packet in responses:
    
            index = 22

            while True:

                if index+7>=len(packet):
                    break
            
                ip = inet_ntop(socket.AF_INET, packet[index+1:index+5])
                port = 256*ord(packet[index+5]) + ord(packet[index+6])
                index+=7
                server =  ip+':'+str(port) 
                self.serverslist.append(server)
         
            s.close()
        
        self.ListServers()

    def ListServers(self):

        return self.serverslist

if __name__ == '__main__':

    m = Q3masterServer("master.urbanterror.info", 27900)
    listservers = m.ListServers()
    for server in listservers:
        print server