import socket

def server_program():
   # get the hostname
   host = socket.gethostname()
   port = 5000  # initiate port no above 1024

   server_socket = socket.socket()  # get instance
   # look closely. The bind() function takes tuple as argument
   server_socket.bind((host, port))  # bind host address and port together

   # configure how many client the server can listen simultaneously
   server_socket.listen(5)
   s=input('Willing to accept more connections?')
   while(s!='no'):
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
      print("from connected user: \n" + str(data))
   #s=input('Do you want more requests?')
   #conn, address = server_socket.accept()
   #data = input(' -> ')
   #conn.send(data.encode())  # send data to the client
      s=input('Willing to accept more connections?')
   conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
