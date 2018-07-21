'''

Made by:-
-----------------
SATYAM JINDAL
04-07-2018
-----------------


'''

# **cx_Freeze** used to create the Executable File for the client side.

from cx_Freeze import setup, Executable                                                     

setup(name='try',
      version='0.1',
      description='Parse stuff',
      executables = [Executable("client.py")])
