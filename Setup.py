from cx_Freeze import setup, Executable

setup(name='try',
      version='0.1',
      description='Parse stuff',
      executables = [Executable("chat_client.py")])
