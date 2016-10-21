from MapReduce import Log
l = Log('My log')
print "Total number of connections = %d" %l.getTotalConnections()
print "All the IP's = %r" %l.getAll_IPs()
print "All the Unique IP's = %r" %l.getAll_unique_ips()