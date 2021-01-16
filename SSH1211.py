import paramiko
import time
import pexpect


time.sleep(1)

ip = "192.168.122.xxx"
host = ip
username = "admin"
password = "cisco"

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
print("SSH connection established to " + host)
    
remote_conn = remote_conn_pre.invoke_shell()
print("Interactive SSH session established")

output = remote_conn.recv(1000)
print(output)   

remote_conn.send("\n")
remote_conn.send("utils system restart\n")
time.sleep(5)

output = remote_conn.recv(5000)
print(output)
