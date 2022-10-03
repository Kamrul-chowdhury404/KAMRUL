import os, platform

try:

        import requests

except:

        os.system('pip2 install requests')

import requests

bit = platform.architecture()[0]

if bit == "64bit":

        from c32(2) import login

        login()
if b == '32bit':
    from c32 import login

