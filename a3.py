import netmiko 
import getpass
from netmiko import ConnectHandler
import telnetlib
import os 
import difflib
import ipaddress

router_connection = {
    'device_type': '',
    'host': '192.168.56.101',
    'username': '', # Username = cisco
    'password': '', # Password = cisco123
    'secret': '' # Secret password = class123!
}

def ssh():
    output = {}
    router_connection['device_type'] = 'cisco_ios'
    ssh_session = netmiko.ConnectHandler(**router_connection)
    ssh_session.enable()
    # ssh_session.send_command('terminal length 0')
    display_session = ssh_session.send_command('Show running-config')
    output = display_session
    print(output)
    configFile_Path = ("ssh.txt")
    if not os.file_path("ssh.txt"):
    # Added content of the ssh and router connection to the .txt file
        configFile_Path = open("ssh.txt", "w")
        configFile_Path.write(output)
        configFile_Path.close()
        configFile_Path.read(configFile_Path)option = input("interface loopback(1), result(2), RIP(3), OSPF(4) configure vlans and interfaces(5)?")

    if option = "1":
        loopback = ssh.send_command('int loopback 0', 'ip_address 10.10.1.1 255.255.255.255')
        print(loopback)
    elif option = "2":
        output = ssh.send_command('Show IP brief')
    elif option = "3":
        RIP = ssh.send_command('router rip','version 2','Network 10.10.1.1')
        print(RIP)
    elif option = "4":
        OSPF = ssh.send_command('router ospf','version1','int loopback 0','ip_address 192.168.14.4 255.255.255.255')
        print(OSPF)
    elif option = "5":
    #This part is to configure the switch
    #The first line cross creates an Vlan and gives it an ip address
        ssh.send_config_set('interface vlan07' 'vlan07', 'ip_address 192.168.100.21')
        ssh.send_config_set('interface g0/0/1', 'switchport mode access', 'switchport access vlans07')
    else:
        exit(login)
        