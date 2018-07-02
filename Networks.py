import subprocess
import MySQLdb

try:
    db = MySQLdb.connect('localhost','root','','python')
except Exception as e:
    print('Cant get into the database')

cursor = db.cursor()
my = subprocess.run(['nmap',' ','-sn',' ','192.168.0.1/24',' ','-n'],stdout = subprocess.PIPE)
my=str(my)
#myprocess = myprocess.replace('\\r\\n','\n')
my = my[my.index('Time')+8:]
my = my.replace('\\r\\n','\\')
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
            final_list.append(s[21:])
        elif(c==2):
            final_list.append(s)
        elif(c==3):
            final_list.append(s[13:30])
        c%=3
        s=''
    else:
        s+=my[i]
curr=1
cursor.execute('DELETE FROM devices')
for i in range(0,len(final_list)-3,3):
    cursor.execute('INSERT INTO devices VALUES(%s,%s,%s,%s)',(curr,final_list[i],final_list[i+1],final_list[i+2]))
    curr+=1

    
    


