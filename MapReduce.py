#!/usr/bin/python
class Log:
    'Log file, its components and actions'
    def __init__(self, fname):
        self.ips =[]
        self.sumEntries(fname)
        self.storeIPs(fname)


    def sumEntries(self, fname):
        with open(fname) as file:
            self.totalConnections = sum(1 for _ in file)

    def storeIPs(self, fname):
        with open(fname) as file:
            for line in file:
                w = 0
                for word in line.split():
                    if w == 3:
                        self.ips.append(word)
                    w = w + 1

    def getTotalConnections(self):
        return self.totalConnections

    def getAll_IPs (self):
        return self.ips

    def getAll_unique_ips (self):
        self.uniqueIPS = list(set(self.ips))
        return self.uniqueIPS


