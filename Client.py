'''

Made by:-
-----------------
SATYAM JINDAL
04-07-2018
-----------------


'''

# Code for Client Side  (64bit only)



import socket
import platform as pt
import re,uuid
from collections import namedtuple
from ctypes import byref, create_unicode_buffer, windll                                                     # Importing libraries
from ctypes.wintypes import DWORD
from itertools import count
from winreg import *


aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
aKey = OpenKey(aReg, r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall")                    # Accessing registry containing list of 32 Bit Softwares
final_soft=[]
for i in range(1024):
    try:
        asubkey_name=EnumKey(aKey,i)                                                                    
        asubkey=OpenKey(aKey,asubkey_name)
        val=QueryValueEx(asubkey, "DisplayName")                                                            # Querying for Display Name of the software
        final_soft.append(val)
    except EnvironmentError:
        continue

aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")                                # Accessing registry containing list of 62 Bit Softwares


for i in range(1024):
    try:
        asubkey_name=EnumKey(aKey,i)
        asubkey=OpenKey(aKey,asubkey_name)
        val=QueryValueEx(asubkey, "DisplayName")                                                            # Querying for Display Name of the software
        final_soft.append(val)
    except EnvironmentError:
        continue



def client_program():
    host = socket.gethostname()                                                                             # Use the Host Name of the server Machine
    port = 5000                                                                                             # Socket Server port number

    client_socket = socket.socket()                                                                         
    client_socket.connect((host, port))                                                                     # Connecting to the server
    
    mac_add = str(':'.join(re.findall('..','%012x'%uuid.getnode())))                                        # Finding the Mac Address


    message = 'System: '+str(pt.system())+'\n'+'Name: '+str(pt.node())+'\n'
    message+='release: '+str(pt.release())+'\n'+'version: '+str(pt.version())+'\n'                          #Getting diffreent aspects of the machine
    message+='machine: '+str(pt.machine())+'\n'+'processor: '+str(pt.processor())+'\n'
    message+='Mac Address: '+mac_add +'\n\n'
    message+='\nLIST OF SOFTWARES WITH PROPERTIES \n\n'
    list_of_soft=[]
    for i in final_soft:
        list_of_soft.append(i[0])                                                                           #**list_of_soft** consists of all the names of the softwares in the system

    list_of_soft.sort()
    for i in list_of_soft:
        message+=i
        message+='\n'                                                                                       #Variable **message** stores the entire list of softwares and aspects
    message+='\n'

    client_socket.send(message.encode())                                                                    # Send message to the Server


    client_socket.close()                                                                                   # Close the connection


if __name__ == '__main__':
    client_program()
