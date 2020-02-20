Q3MasterServer v 2 (PtitBigorneau www.ptitbigorneau.fr)
##############################################################
Python 3
##############################################################
Exemple Urban Terror Master Server
##############################################################

from q3masterserver import Q3masterServer

host = "master.urbanterror.info"
port = 27900

m = Q3masterServer(host, port)
listservers = m.ListServers()

n = 0

for server in listservers:
    print(server)
    n = n + 1
print("-------------------"=
print(n)

##############################################################