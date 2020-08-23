#!/usr/bin/python

import os
import json
import argparse
import subprocess
from vars import *


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

