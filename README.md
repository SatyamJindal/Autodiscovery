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
