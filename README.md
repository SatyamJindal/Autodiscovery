# Autodiscovery :sunglasses:


**A project made for KC consultancy.**

**Autodiscovery** is a server-client based software created in Python which is divided into two segments. 
The first segment consists of a script for the client side which when executed extracts the information given below and sends it to the server side which is then sent to a database which is created using WampServer.

**The information gathered from the client side includes:-**

+ Extensive list of all Software’s installed (32bit + 64bit)
+ System
+	Name
+	Release
+	Version
+	Machine
+	Processor
+	Mac Address

**Two registries which were used to get the list of software’s are:**

+	SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall
+	SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall

The **second segment** gets the server all the devices that are connected to the network. It may a printer, a mobile phone, a laptop or any other device. It uses an ethical hacking tool called “Nmap” to get the respective information. 

**How is it useful for any organisation?**

It can used to verify if all the employees are not using any outdated product or a product which they should not be using. This will allow the organisation to take immediate action if some wrong doing is found.

## Set-Up Instructions :exclamation:


**Technologies needed –**
+ Python

**Python Modules needed –**
+ socket
+ platform
+ uuid
+ ctypes
+ itertools
+ winreg
+ subprocess
+ MySQLdb
+ Cx_Freeze

**_Tip:_** - The easiest way to get the above modules is to use pip. :thumbsup:

**Instructions For setup of the database** 

-----------------------------------------

1. Go to "http://www.wampserver.com/en/" and download the version that will suit your system requirements (32 or 64bit).
2. If you do not have Microsoft Visual Studio : - 
Get it from -  "http://www.microsoft.com/en-us/download/details.aspx?id=30679" and finish the setup.
3. During the installation of the wamp server you need to choose your default browser (Google Chrome preffered)
Go to "C:\Program Files (x86)\Google\Chrome\Application" directory and choose "Chrome".
4. Open "phpmyadmin" and this is where we create our Database (Name of the database -> **python**).
5. Two tables need to be created:

--------
Text
--------

**ATTRIBUTES**

+ id (int(11)) - Primary Key - Auto Increment
+ ip (varchar(255))
+ system (varchar(255))
+ name (varchar(255))
+ release (varchar(255))
+ version (varchar(255))
+ machine (varchar(255))
+ processor (varchar(255))
+ Mac Address (varchar(255))
+ list (text)

--------
Devices
--------

**ATTRIBUTES**
+ id (int(11)) - Primary Key - Auto Increment
+ IP (varchar(255))
+ Latency (varchar(255))
+ Mac Address (varchar(255))
+ Iter (int(11))

The structure of both the tables should look like:-









