# Autodiscovery :sunglasses:


**A project made for KC consultancy.**

**Autodiscovery** is a server-client based software created in Python which is divided into two segments. 
The first segment consists of a script for the client side which when executed extracts the information given below and sends it to the server side which is then sent to a database which is created using WampServer.

**The information gathered from the cline side includes:-**

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



