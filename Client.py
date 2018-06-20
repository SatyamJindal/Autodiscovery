import socket
import platform as pt
import re,uuid
from collections import namedtuple
from ctypes import byref, create_unicode_buffer, windll
from ctypes.wintypes import DWORD
from itertools import count
from winreg import *


aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
aKey = OpenKey(aReg, r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall")
final_soft=[]
for i in range(1024):
    try:
        asubkey_name=EnumKey(aKey,i)
        asubkey=OpenKey(aKey,asubkey_name)
        val=QueryValueEx(asubkey, "DisplayName")
        final_soft.append(val)
    except EnvironmentError:
        continue

aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")


for i in range(1024):
    try:
        asubkey_name=EnumKey(aKey,i)
        asubkey=OpenKey(aKey,asubkey_name)
        val=QueryValueEx(asubkey, "DisplayName")
        final_soft.append(val)
    except EnvironmentError:
        continue





'''UID_BUFFER_SIZE = 39
PROPERTY_BUFFER_SIZE = 256 
ERROR_MORE_DATA = 234
ERROR_INVALID_PARAMETER = 87
ERROR_SUCCESS = 0
ERROR_NO_MORE_ITEMS = 259 
ERROR_UNKNOWN_PRODUCT = 1605

# diff propoerties of a product, not all products have all properties
PRODUCT_PROPERTIES = [u'Language',
                      u'ProductName',
                      u'PackageCode',
                      u'Transforms',
                      u'AssignmentType',
                      u'PackageName',
                      u'InstalledProductName',
                      u'VersionString',
                      u'RegCompany',
                      u'RegOwner',
                      u'ProductID',
                      u'ProductIcon',
                      u'InstallLocation',
                      u'InstallSource',
                      u'InstallDate',
                      u'Publisher',
                      ]

conver = ['Language','ProductName','PackageCode','Transforms','AssignmentType',
          'PackageName','InstalledProductName','VersionString','RegCompany',
          'RegOwner','ProductID','ProductIcon','InstallLocation','InstallSource',
          'InstallDate','Publisher','LocalPackage']


# class to be used for python users :)
Product = namedtuple('Product', PRODUCT_PROPERTIES)

softwares_list = []

def get_property_for_product(product, property, buf_size=PROPERTY_BUFFER_SIZE):
    """Retruns the value of a fiven property from a product."""
    property_buffer = create_unicode_buffer(buf_size)
    size = DWORD(buf_size)
    result = windll.msi.MsiGetProductInfoW(product, property, property_buffer,
                                           byref(size))
    if result == ERROR_MORE_DATA:
        return get_property_for_product(product, property,
                2 * buf_size)
    elif result == ERROR_SUCCESS:
        return property_buffer.value
    else:
        return None

def get_string(final):
    fin=''
    for i in range(len(final)):
        #print(len(final[i]))
        for j in range(len(final[i])):
            if(final[i][j]!=None and len(final[i][j])!=0):
                #print(final[i][j])
                fin+=conver[j]+':  '
                fin+=final[i][j]
                fin+='\n'
            else:
                fin+=conver[j]+':  '
                fin+='NIL'
                fin+='\n'
        fin+='\n'
    return fin
final=[]

def populate_product(uid):
    """Return a Product with the different present data."""
    properties = []
    for property in PRODUCT_PROPERTIES:
        properties.append(get_property_for_product(uid, property))
    softwares_list.append(properties)
    final.append(properties)
    return Product(*properties)

def get_installed_products():
    """Returns a collection of products that are installed in the system."""
    products = []
    for puid in  get_installed_products_uids():
        products.append(populate_product(puid))
    return products 


def is_product_installed_uid(uid):
    """Return if a product with the given id is installed.
 
    uid Most be a unicode object with the uid of the product using
    the following format {uid}
    """
    # we try to get the VersisonString for the uid, if we get an error it means
    # that the product is not installed in the system.
    buf_size = 256
    uid_buffer = create_unicode_buffer(uid)
    property = u'VersionString'
    property_buffer = create_unicode_buffer(buf_size)
    size = DWORD(buf_size)
    result = windll.msi.MsiGetProductInfoW(uid_buffer, property, property_buffer,
                                           byref(size))
    if result == ERROR_UNKNOWN_PRODUCT:
        return False
    else:
        return True



def get_installed_products_uids():
    """Returns a list with all the different uid of the installed apps."""
    # enum will return an error code according to the result of the app
    products = []
    for i in count(0):
        uid_buffer = create_unicode_buffer(UID_BUFFER_SIZE)
        result = windll.msi.MsiEnumProductsW(i, uid_buffer)
        if result == ERROR_NO_MORE_ITEMS:
            # done interating over the collection
            break
        products.append(uid_buffer.value)
    return products

apps = get_installed_products()'''


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number
    #print(host)
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    mac_add = str(':'.join(re.findall('..','%012x'%uuid.getnode())))
    #message = input(" -> ")  # take input
    message = 'System: '+str(pt.system())+'\n'+'Name: '+str(pt.node())+'\n'
    message+='release: '+str(pt.release())+'\n'+'version: '+str(pt.version())+'\n'
    message+='machine: '+str(pt.machine())+'\n'+'processor: '+str(pt.processor())+'\n'
    message+='Mac Address: '+mac_add +'\n\n'
    message+='\nLIST OF SOFTWARES WITH PROPERTIES \n\n'
    for i in final_soft:
        message+=i[0]+' '
        #message+=str(i[1])+' '
        message+='\n'
    message+='\n'
    client_socket.send(message.encode())  # send message
        #data = client_socket.recv(1024).decode()  # receive response

        #print('Received from server: ' + data)  # show in terminal

        #message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
