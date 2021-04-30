import getpass
import telnetlib

#Configuration of Switch, improve Vlans config with loop  

HOST = "172.16.0.2"
user = input("Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")


for i in range(2, 31) :

    tn.write(b"vlan "+str(i).encode('ascii')+b"\n")
    tn.write(b"name Python_VLAN"+str(i).encode('ascii')+b"\n")


tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
