'''

Made by:-
-----------------
SATYAM JINDAL
04-07-2018
-----------------


'''

# Code for Server Side  (FOR 32bit or 64bit)


import MySQLdb
import sys                                                                                            # Importing Libraries
import socket


try:
   db = MySQLdb.connect('localhost','root','','python')                                               # Connecting to the database
except Exception as e:
   print('Cant get into the database')

cursor = db.cursor()
mine=''

def getinds(s,inds):                                                                                                     
   s1=''                                                                                                                
   indi=-1
   for i in range(len(s)-5):
      if(s[i]=='L' and s[i+1]=='I' and s[i+2]=='S' and s[i+3]=='T'):
         indi=i+3
         break
      else:
         s1+=s[i]
   system = s1.index('System')
   name = s1.index('Name')
   release = s1.index('release')                                                                      # Function for String formatting and getting different aspects                                                                              
   version = s1.index('version')                                                                      # of the system
   machine = s1.index('machine')                                                                                     
   processor = s1.index('processor')
   mac = s1.index('Mac')
   inds.append(s1[8:name])
   inds.append(s1[name+6:release])
   inds.append(s1[release+9:version])
   inds.append(s1[version+9:machine])
   inds.append(s1[machine+9:processor])
   inds.append(s1[processor+11:mac])
   inds.append(s1[mac+13:indi])
   return indi


def server_program():
   global mine, cursor
   host = socket.gethostname()                                                                        # Gets Hostname of the current(Server) system
   port = 5000  

   server_socket = socket.socket()                                                                    # Get instance
   
   server_socket.bind((host, port))                                                                   # Bind host address and port together in a tuple

   
   server_socket.listen(5)                                                                            # Configure how many client the server can listen simultaneously
                                                                                                      # To be set as per the company's requirements

   
   #s=input('Willing to accept connections?')
   #curr=1
   while(1):                                                                                                            
      mine=''
      
      conn, address = server_socket.accept()                                                          # accept new connection

      
      print("Connection from: " + str(address))                                                       # Connection from the respective IP 

      data = conn.recv(209800).decode()                                                               # receive data stream. it won't accept data packet greater than 209800 bytes
                                                                                                      # No. of bytes to be set as pe the company's requirements
 
      mine+=str(data)
      indi=-1
      inds=[]
      indi=-1
      s=mine[:]
      for i in range(len(s)-5):
         if(s[i]=='L' and s[i+1]=='I' and s[i+2]=='S' and s[i+3]=='T'):
            indi=i
            break
      getinds(mine,inds)   
      softs = mine[indi:]                                                                             # Contains the List of all softwares
      
      cursor.execute('SELECT MAX(id) from text;')                                                     # Gets the precious maximum Id so a duplicate key is not created
                                                                                                      # Done to avoid the unique primary key law
      num = cursor.fetchall()                                                          
      num=str(num[0])
      curr = num[1:num.index(',')]
      if(curr[0]=='N'):
         curr=1                                                                                       #Increments the current Maximum Id by one
      else:
         curr = int(curr)+1
         
      cursor.execute('INSERT INTO text VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(curr,str(address),inds[0],inds[1],inds[2],inds[3],inds[4],inds[5],inds[6],softs))     #Inserting into the database
      curr+=1

   conn.close()                                                                                       # close the connection


if __name__ == '__main__':
    server_program()
