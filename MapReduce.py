#!/usr/bin/python
class Log:
    'Log file, its components and actions'
    def __init__(self, fname):
        with open(fname) as file:
            self.totalConnections = sum(1 for _ in file)

    def getTotalConnections(self):
        return self.totalConnections



