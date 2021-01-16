#!/usr/bin/python
import getpass
import sys
import telnetlib

HOST = "192.168.5.1"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
  tn.read_until("Password: ")
  tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n") #enable password
tn.write("conf t\n")
tn.write("int loop 0\n")
tn.write("ip address 1.1.1.1 255.255.255.255\n")
print 'sucussfully added a loop back address'
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
