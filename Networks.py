'''

Made by:-
-----------------
SATYAM JINDAL
04-07-2018
-----------------


'''

# Getting all the Devices connected to the Router (For Windows only)
# Get Nmap on your device before running this code

import subprocess                                                                                                   # Importing libraries
import MySQLdb

try:
    db = MySQLdb.connect('localhost','root','','python')                                                            # Connecting to the database
except Exception as e:
    print('Cant get into the database')

cursor = db.cursor()
my = subprocess.run(['nmap',' ','-sn',' ','192.168.0.1/24',' ','-n'],stdout = subprocess.PIPE)                      # Gets all devices connected to the router
my=str(my)
my = my[my.index('Time')+8:]
my = my.replace('\\r\\n','\\')                                                                                      # String formatting
final_list=[]
s=''
c=0
till = my.index('IP addresses')
for i in range(till-2):
    if(my[i]=='\\'):
        c+=1
        if(c%3==0):
            s+='\n'
        if(c==1):
            final_list.append(s[21:])                                                                               # Data Cleaning
        elif(c==2):
            final_list.append(s)
        elif(c==3):
            final_list.append(s[13:30])
        c%=3
        s=''
    else:
        s+=my[i]
#curr=1

cursor.execute('SELECT MAX(id) from devices;')                                                     # Gets the precious maximum Id so a duplicate key is not created
                                                                                                      # Done to avoid the unique primary key law
num = cursor.fetchall()                                                          
num=str(num[0])
curr = num[1:num.index(',')]
if(curr[0]=='N'):
    curr=1                                                                                       #Increments the current Maximum Id by one
else:
     curr = int(curr)+1

cursor.execute('SELECT MAX(iter) from devices;')                                                     # Gets the precious maximum Id so a duplicate key is not created
                                                                                                      # Done to avoid the unique primary key law
ite = cursor.fetchall()                                                          
ite=str(ite[0])
ite = ite[1:ite.index(',')]
if(ite[0]=='N'):
    ite=1                                                                                       #Increments the current Maximum Id by one
else:
     ite = int(ite)+1
     
                                                                               # Deleting the previously existing List
for i in range(0,len(final_list)-3,3):
    cursor.execute('INSERT INTO devices VALUES(%s,%s,%s,%s,%s)',(curr,final_list[i],final_list[i+1],final_list[i+2],ite))  # Inseting into the Database
    curr+=1

    
    


