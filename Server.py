import MySQLdb
import sys
import socket


try:
   db = MySQLdb.connect('localhost','root','','python')
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
   release = s1.index('release')
   version = s1.index('version')
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
   # get the hostname
   host = socket.gethostname()
   port = 5000  # initiate port no above 1024

   server_socket = socket.socket()  # get instance
   # look closely. The bind() function takes tuple as argument
   server_socket.bind((host, port))  # bind host address and port together

   # configure how many client the server can listen simultaneously
   server_socket.listen(5)
   s=input('Willing to accept more connections?')
   curr=1
   while(s!='no'):
      mine=''
      conn, address = server_socket.accept()  # accept new connection
      print("Connection from: " + str(address))
   #s=input('Do you want more requests?')
   #while(s!='No'):
   #while True:
   # receive data stream. it won't accept data packet greater than 1024 bytes
      data = conn.recv(209800).decode()
   #if not data:
      # if data is not received break
   #break
      #value='1'
      print("from connected user: \n" + str(data))
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
      #print(inds)
      #print(indi)
      #print(inds)
      softs = mine[indi:]
      #print(softs)
      cursor.execute('INSERT INTO text VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(curr,str(address),inds[0],inds[1],inds[2],inds[3],inds[4],inds[5],inds[6],softs))
      curr+=1
   #s=input('Do you want more requests?')
   #conn, address = server_socket.accept()
   #data = input(' -> ')
   #conn.send(data.encode())  # send data to the client
      s=input('Willing to accept more connections?')
   conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
