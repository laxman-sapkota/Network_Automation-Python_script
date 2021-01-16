#!/bin/usr/python
import pexpect

# Variables
ip_address = "192.168.122.187 # The Default ip Address for router 
user_name = "admin"
pass_word = "cisco123"
password_enable = "cisco123"  #This is a Password for enable mode
enable = "enable" # Entering Enable command
firstint = "10.0.0.2"  # First interface
secondint = "10.0.0.5"  # Second interface
submask = "255.255.255.252"  # Subnet Mask
clockrate = "64000" # Clock Rate

def enablemode():
    # Enter enable mode
    session.sendline(enable)
    result=session.expect(['Password:', pexpect.TIMEOUT])

    # Check for error, if so then print error and exit
    if result !=0:
        print ('Failure! There is a problem with entering enable mode please try again')
    else:
        print('Entering Enable Password')
    # Send enable password
    session.sendline(password_enable)
    result=session.expect(['#', pexpect.TIMEOUT])

    # Check for error, if so then print error and exit
    if result != 0:
        print ('Failure! There is a problem with the enable password please try again')
    else:
        print('User now in privileged mode ')

def configmode():
    # Issue config t command.
    session.sendline('config t')
    result = session.expect(['R1\(config\)#', pexpect.TIMEOUT])
    # Check for error, if so then print error and exit
    if result != 0:
        print ('Failure! entering config mode')
    else:
        print('Entering global configuration mode')

def changinghostname():
    # Change the hostname to R2
    session.sendline('hostname R2')
    result = session.expect(['R2\(config\)#', pexpect.TIMEOUT])

    # Check for error, if so then print error and exit the program
    if result != 0:
        print ('Failure! There is a problem with setting the hostname please  try again')

def staticinterfaceone():
    # R2 Setting up interface one
    session.sendline('interface g0/1')
    result = session.expect(['R2\(config-if\)#', pexpect.TIMEOUT])

    if result != 0:
        print ('Failure! There is a problem with setting the hostname please try again')
    else:
        print('Entering IP')
    # First interface ip addressing sign command
    session = pexpect.spawn('ip address ' + firstint, submask)
    result = session.expect(['R2\(config-if\)#', pexpect.TIMEOUT])
    if result != 0:
                print('Failure! There is a problem with setting the hostname please try again')
    else:
                print ('Completed the first interface with ' + firstint, submask)
    session.sendline('exit')


def noshutdown():
    print('No shutdown command initialised')
    session.sendline('no shut')
    result = session.expect(['R2\(config-if\)#', pexpect.TIMEOUT])
    #       Check for error, if so then print error and exit the program
    if result != 0:
        print (
            'Failure! There is a problem with setting the no shutdown command please try again')
    else:
        print("No Shutdown Entered, Inserted Static IP Address")

def staticinterfacetwo():
        # R2 Setting up interface two
                session.sendline("interface g0/2")
                result = session.expect(['R2\(config-if\)#', pexpect.TIMEOUT])

                if result != 0:
                        print('Failure! There is a problem with setting the hostname please  try again')
                else:
                        print('Entering in the ip address ' + secondint)

    # First interface ip addressing sign command
                session.sendline('ip address ' + secondint, submask)
                result = session.expect(['R2\(config-if\)#', pexpect.TIMEOUT])
                if result != 0:
                        print('Failure! There is a problem with setting the hostname please try again')
                else:
                        print ('Completed the first interface with ' + secondint, submask)
                session.sendline('exit')

    # Initialising the no shutdown command
                print('No shutdown command initialised')
                session.sendline('no shut')
                result = session.expect(['R2\(config-if\)#', pexpect.TIMEOUT])
#    Check for error, if so then print error and exit the program
                if result != 0:
                    print ('Failure! There is a problem with setting the no shutdown command please try again')
                else:
                    session.sendline('exit')

def clockrate():
# Call the clockrate
    session.sendline(clockrate)
    result = session.expect(['R2\(config-if\)#', pexpect.TIMEOUT])
    if result !=0:
        print('Failure! There is a problem with setting the hostname please try again')
    else:
        print('Clock rate has been set to 64000 for interface gig0/2 as it is a DCE Connection')
        session.sendline('exit')

# ================SSH LOGIN=====================================

#   Logging into the network device
#   Initiate the pexpect session and enter the ssh command
    print("You are logging into " + ip_address)

session = pexpect.spawn("ssh " + user_name + "@" + ip_address, timeout=20)
result = session.expect(["Password:", pexpect.TIMEOUT])

#   Check for error, if so then print error and exit
if result != 0:
        print('Failure! There is a problem with creating a session for this ip address please  try again', ip_address)
else:
        print('Username is correct')

#   Session expecting password, enter it here
session.sendline(pass_word)
result = session.expect(['>', pexpect.TIMEOUT])
#   Check for error, if so then print error and exit
if result != 0:
  print('Failure! There is a problem with the password please try again', pass_word)
else:
        print("Password is correct")
        # Output the results of the login
        print('---Success! connecting to: ', ip_address)
        print('--- With username: ', user_name)
        print('------------------------------------------------------\n')

enablemode()
configmode()
staticinterfaceone()
noshutdown()
staticinterfacetwo()
clockrate()
noshutdown()
