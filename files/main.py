#!/usr/bin/python

import os
import json
import argparse
import subprocess
import xml.etree.ElementTree as ET

v3_ccxml = '/usr/bin/cxiSHMDump -d /ccxml0 | grep "CXI|" | sed -e "s/CXI|/ccxml/g"'
v3_xml0 = '/usr/bin/v3xmlSHMDump -d /v3xml0 -f etc/ipc.shm  | grep mic5 | sed -e "s/VXML|mic5|/v3xml0./g"'
v3_xml1 = '/usr/bin/v3xmlSHMDump -d /v3xml1 -f etc/ipc.shm  | grep mic5 | sed -e "s/VXML|mic5|/v3xml1./g"'
nb_audio = 'echo  `/usr/bin/audioCaptureSurv -cfg /etc/audioCapture/audioCapture.cfg -b | cut -d ";" -f1|/usr/bin/tr -d " "` "nbaudiocapture"  ' 
nb_confsrv = 'echo `/usr/bin/ConfSrvSurv -cfg /etc/ConferenceServer/ConfSrv.cfg  -conf|/bin/grep "Nb conference used"|/bin/cut -d":" -f2|/usr/bin/tr -d " "` "nbconfsrv" '

class Metrics:

    @staticmethod
    def v3xml0(value=None):
        dict_lo0 = {}
        stream = os.popen(value).readlines()

        for line in stream:
            try:

                value, metricsName = line.strip().split(None, 1)
            except ValueError:
                pass
            dict_lo0[metricsName] = int(value)
        return json.dumps(dict_lo0, indent=1)



    @staticmethod
    def v3xml(app, value, kbName):
        dct = {}
        ps = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE).communicate()[0]
        processes = ps.split('\n')
        nfields = len(processes[0].split()) - 1
        for row in processes[1:]:
            if app in row and value in row:
                 dct[kbName] = int(row.split(None, nfields)[4])
                 return json.dumps(dct, indent=1)



    @staticmethod
    def audioCap(appSearch, value=None, kbName=None, sysapp=None):
        dct = {}
        ps = subprocess.Popen([sysapp, 'b', 'n 1'], stdout=subprocess.PIPE).communicate()[0]
        processes = ps.split('\n')
        nfields = len(processes[0].split()) - 1
        for row in processes[1:]:
            if appSearch in row and value in row:
                dct[kbName] = int(round(float(row.split(None, nfields)[8])))
                return json.dumps(dct, indent=1)

    @staticmethod
    def app_list(txt=''):

        root = ET.parse('/etc/v3xml/applist.xml').getroot()
        app = []
        for type_tag in root.findall('apps/app'):
            value = type_tag.get('id') + txt
            app.append(value)
        return app

    @staticmethod
    def loopadapt(direction=""):
        dict = {}

        for i in Metrics.app_list(direction):
            if i in Metrics.v3xml0(v3_xml0) and i in Metrics.v3xml0(v3_xml1):

                pass
            else:
                dict[i] = 0
        return json.dumps(dict, indent=0)
    







parser = argparse.ArgumentParser()

parser.add_argument('--option1', help='description for option1')
parser.add_argument('--option2', help='description for option2')
parser.add_argument('--option3', help='description for option3')
parser.add_argument('--option4', help='description for option4')
parser.add_argument('--option5', help='description for option5')
parser.add_argument('--option6', help='description for option6')
parser.add_argument('--option7', help='description for option7')
parser.add_argument('--option8', help='description for option8')
parser.add_argument('--option9', help='description for option9')


args = parser.parse_args()

# vxml*_incoming  if not found  in Install directory : [/v3xml0] and [/v3xml1] == olways 0
if args.option1:
    print(Metrics.loopadapt("_incoming"))

# vxml*_outgoing  if not found  in Install directory : [/v3xml0] and [/v3xml1] == olways 0
if args.option2:
    print(Metrics.loopadapt("_outgoing"))

# vxml*_bridge  if not found  in Install directory : [/v3xml0] and [/v3xml1] == olways 0
if args.option3:
    print(Metrics.loopadapt("_bridge"))

#kbmemusedv3xml1browser memory use
if args.option4:
    print(Metrics.v3xml('v3xmlBrowserNTB', 'v3xml1', 'kbmemusedv3xml1browser'))

#kbmemusedaudioCapture memory use
if args.option5:
    print(Metrics.v3xml('audioCapture.cfg', '', 'kbmemusedaudioCapture'))

#kbmemusedv3xml0browser" memory use
if args.option6:
    print(Metrics.v3xml('v3xmlBrowserNTB', 'v3xml0', 'kbmemusedv3xml0browser'))
#CXI_totalsessions
if args.option7:
    print(Metrics.v3xml0(v3_ccxml))

#nbaudiocapture
if args.option8:
    print(Metrics.v3xml0(nb_audio))

#nbconfsrv
if args.option9:
    print(Metrics.v3xml0(nb_confsrv))
