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

![alt text](https://github.com/SatyamJindal/Autodiscovery/blob/master/table_devices.PNG "Devices")
-------------
-------------

![alt text](https://github.com/SatyamJindal/Autodiscovery/blob/master/table_text.PNG "Text")


**Instructions to install NMAP on your PC**

-----------------------------------------

1. Go to "https://nmap.org/download.html"
2. Under Microsoft Windows binaries click on : - 
Latest stable command-line zipfile: (Click here)
3. Extract the files and move the folder to "Program Files".
4. Rename the folder to "Nmap"
5. Right click on "My computer Icon/This PC" > "Properties" > "Advanced System Settings" > "Environment Variables"
6. Select "TMP" and cick on "New"
7. Variable Name: - "path"
    variable value: - "path of the Nmap directory"
                       eg: - C:\Program Files\Nmap
    And click "ok"
8 Go to Command Prompt and type "nmap"
(If it doesn't show an error it means you have installed it successfuly)

![alt text](https://github.com/SatyamJindal/Autodiscovery/blob/master/Images/Nmap.gif "Namp")

9. Now you also need to get "WinPcap".
10. Go to "https://www.winpcap.org/install/" and click on "Installer for Windows".
11. Complete the setup.

As it is not possible for every company to install python on every client's computer and ask them to run this code everytime, there is a way to create an executable file which does not require any installation of Python or its libraries.

**Instructions for creating an Executable File using cx_Freeze**

-------------------------------------------------------------

1. Create a new folder.
2. Create a copy of "client.py" and "setup.py" and move both of them to this folder.
3. Hold "Shift" > "Right Click" on the folder created > "Open PowerShell Window here".
4. Now write: - 

        "python setup.py build"
                    OR
        "python3 setup.py build"
	                OR
        "py setup.py build"  and hit enter.
5. A folder named **"build"** is created which contains the executable file which can be put into any system.

**Up and Running**

+ Now that everything is set run the server code along with the client. For now I created a localhost using Wamp Server to test it on my own system.
+ The changes that need to be made for it to run on multiple systems are clearly commented in the code itself.

The first segment when run on the same system will look something like: - 

**_Note:-_** - Make sure that the WampServer is running as the information received will be directly stored in the database.

Below is how it will look like initially when the database has no entry and after the client runs the script there is an update made to the databse with all his details. The client code is run on the local server created on my PC for now just to show a basic working of this segment.

![alt text](https://github.com/SatyamJindal/Autodiscovery/blob/master/Images/Server.gif "Implementation")















