import re
import os

text = 'Name=clara, Nationality=German, Payments=123'

searchresult = re.match('Name=([A-Z)][a-z]*), Nationality=([A-Z][a-z]*), Payments=(\d*)', text, re.I | re.U)

print(searchresult.groups())
----------------------------------------------------------------

stream = os.popen('/usr/bin/v3xmlSHMDump -d /v3xml0 -f etc/ipc.shm  | grep mic0 | sed -e "s/VXML|mic0|/v3xml0./g"')
output = stream.readlines()

for i in output:
    print (i.strip())