import getpass
import telnetlib


#Configuration of Switch 

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
tn.write(b"hostname SW1\n")
tn.write(b"vlan 2\n")
tn.write(b"name Python_VLAN2\n")
tn.write(b"vlan 3\n")
tn.write(b"name Python_VLAN3\n")
tn.write(b"vlan 4\n")
tn.write(b"name Python_VLAN4\n")
tn.write(b"vlan 5\n")
tn.write(b"name Python_VLAN5\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))


#Configuration of Router

HOST = "172.16.0.1"
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
tn.write(b"hostname R1\n")
tn.write(b"int lo1\n")
tn.write(b"ip add 1.1.1.1 255.255.255.255\n")
tn.write(b"int lo2\n")
tn.write(b"ip add 2.2.2.2 255.255.255.255\n")
tn.write(b"int lo3\n")
tn.write(b"ip add 3.3.3.3 255.255.255.255\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
