# Q3MasterServer  (PYTHON 3)
# Copyright (C) 2015-2020 PtitBigorneau
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
__version__ = '2'
#########################################################################################################
import sys

if sys.version_info < (3,):
    raise SystemExit("Sorry, requires Python 3, not Python 2.")
#########################################################################################################
import socket
    
class Q3masterServer:

    def __init__(self, host, port, opt):

        packet_prefix = bytes([0xff] * 4)
        responses = []
        self.serverslist = []

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((host, port))
        s.settimeout(2)

        option = "getservers  68 %s"%opt

        cmd = packet_prefix + option.encode()
        s.send(cmd)

        while True:

            try:
                response = s.recv(2048)
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

                ip = socket.inet_ntop(socket.AF_INET, packet[index+1:index+5])
                port = 256*packet[index+5] + packet[index+6]
                index+=7
                server =  ip+':'+str(port)
                self.serverslist.append(server)

            s.close()

        self.ListServers()

    def ListServers(self):

        return self.serverslist

if __name__ == '__main__':

    m = Q3masterServer("master.urbanterror.info", 27900, "full empty")
    listservers = m.ListServers()
    for server in listservers:
        print(server)

    print(len(listservers))
