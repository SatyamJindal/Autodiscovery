import subprocess
myprocess = subprocess.run(['nmap',' ','-sn',' ','192.168.0.1/24',' ','-n'],stdout = subprocess.PIPE)
myprocess=str(myprocess)
myprocess = myprocess.replace('\\r\\n','\n\n')
print(myprocess)

