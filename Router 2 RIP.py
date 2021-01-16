#!/usr/bin/python
import pexpect

# Variables
ip_address = "192.168.122.187"# IP address
user_name = "admin" # Username 
pass_word = "cisco" # Password
password_enable = "cisco" # Enable Password
firstint = "network 10.0.0.0"  # FIRST NETOWRK
secondint = "network 10.0.0.4"  # SECOND NETWORK
thirdint = "network 192.168.122.187"  # THIRD NETOWRK
ripcommand = "Router rip" # rip Command


def enablemode():
    # Enter enable mode
    session.sendline('enable')
    result=session.expect(['Password:', pexpect.TIMEOUT])

    # Check for error, if so then print error and exit
    if result !=0:
        print('Failure! There has been a problem with entering enable mode please look at your code and try again')
    else:
        print("Username is correct")
    # Send enable password
    session.sendline(password_enable)
    result = session.expect(['#', pexpect.TIMEOUT])

    # Check for error, if so then print error and exit
    if result != 0:
        print('Failure! There has been a problem with the enable password please look at your code and try again')
    else:
        print("Password is correct")
        print("User is now in priviledged mode")

def configmode():
    # Issue config t command.
    session.sendline("config t")
    result = session.expect(['#', pexpect.TIMEOUT])
    # Check for error, if so then print error and exit
    if result != 0:
        print('Failure! entering config mode')
    else:
        print('Entering global configuration mode')

def ripconfigone():
    session.sendline(ripcommand)
	# Check for error, if so then print error and exit
    result = session.expect(['#', pexpect.TIMEOUT])
    if result !=0:
        print('Failure! entering rip config mode')   
    else:
        session.sendline(version 2)
    else:
        session.sendline(firstint)
		# Check for error, if so then print error and exit
        result = session.expect(['#', pexpect.TIMEOUT])
    if result != 0:
        print('Failure! entering network mode')
    else:
        session.sendline(secondint)
		# Check for error, if so then print error and exit
        result = session.expect(['#', pexpect.TIMEOUT])
    if result != 0:
        print('Failure! entering network mode')
    else:
        session.sendline(thirdint)
		# Check for error, if so then print error and exit
        result = session.expect(['#', pexpect.TIMEOUT])
    if result != 0:
        print('Failure! entering network advertisement')
    else:
        print("All of R2 Networks have been advertised using rip")

# Initiate the pexpect session
print("You are logging into " + ip_address)
session = pexpect.spawn('ssh ' + user_name + '@' + ip_address, timeout=20)
result = session.expect(['Password:', pexpect.TIMEOUT])
#    Check for error, if so then print error and exit
if result != 0:
        print('Failure! There has been a problem with creating a session for this ip address please look at your code and try again', ip_address)
else:
        print('Username connected is ' + user_name)

    # Session expecting password, enter it here
session.sendline(pass_word)
result = session.expect(['>', pexpect.TIMEOUT])
# Check for error, if so then print error and exit
if result != 0:
        print('Failure! There has been a problem with the password please look at your code and try again', pass_word)
else:
        # Output the results of the login
        print('---Success! connecting to: ', ip_address)
        print('--- With username: ', user_name)
        print('------------------------------------------------------\n')
# Functions to execute		
enablemode()
configmode()
ripconfigone()
