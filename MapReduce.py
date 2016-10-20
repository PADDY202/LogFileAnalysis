#!/usr/bin/python

class Log:
    'Log file, its components and actions'
    def __init__(self, fname):
        with open('My log') as file:
            totalConnections = sum(1 for _ in file)
        print 'class'

    """totalConnections = 0

    def number_of_connections?(self, file_name): #run on creation
        self.totalConnections = 0"""


 #input a file that only has connections-> delete welcome text, closing text and blank lines
    totalConnections = sum(1 for _ in file)
'print ("the total number of connections is: %d" % totalConnections)'
l = Log()

