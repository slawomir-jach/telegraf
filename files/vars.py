#!/usr/bin/python

import os
import json
import argparse
import subprocess


v3_ccxml = '/usr/bin/cxiSHMDump -d /ccxml0 | grep "CXI|" | sed -e "s/CXI|/ccxml/g"'
v3_xml0 = '/usr/bin/v3xmlSHMDump -d /v3xml0 -f etc/ipc.shm  | grep mic5 | sed -e "s/VXML|mic5|/v3xml0./g"'
v3_xml1 = '/usr/bin/v3xmlSHMDump -d /v3xml1 -f etc/ipc.shm  | grep mic5 | sed -e "s/VXML|mic5|/v3xml1./g"'
nb_audio = 'echo  `/usr/bin/audioCaptureSurv -cfg /etc/audioCapture/audioCapture.cfg -b | cut -d ";" -f1|/usr/bin/tr -d " "` "nbaudiocapture"  ' 
nb_confsrv = 'echo `/usr/bin/ConfSrvSurv -cfg /etc/ConferenceServer/ConfSrv.cfg  -conf|/bin/grep "Nb conference used"|/bin/cut -d":" -f2|/usr/bin/tr -d " "` "nbconfsrv" '
