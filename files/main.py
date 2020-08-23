#!/usr/bin/python

import os
import json
import argparse
import subprocess
from .vars import *
from .metricsClass import *

parser = argparse.ArgumentParser()

parser.add_argument('--option1', help='finding memory usage by this app')
parser.add_argument('--option2', help='description for option2')
parser.add_argument('--option3', help='description for option3')
parser.add_argument('--option4', help='description for option4')
parser.add_argument('--option5', help='description for option5')
parser.add_argument('--option6', help='description for option6')
parser.add_argument('--option7', help='description for option7')
parser.add_argument('--option8', help='description for option8')
parser.add_argument('--option9', help='description for option9')


args = parser.parse_args()

if args.option1:
    print(Metrics.v3xml0(v3_xml0))


if args.option2:
    print(Metrics.v3xml0(v3_xml1))


if args.option3:
    print(Metrics.v3xml('v3xmlBrowserNTB', 'v3xml0', 'kbmemusedv3xml0browser'))

if args.option4:
    print(Metrics.v3xml('v3xmlBrowserNTB', 'v3xml1', 'kbmemusedv3xml1browser')) 

if args.option5:
    print(Metrics.v3xml('audioCapture.cfg', '', 'kbmemusedaudioCapture'))

if args.option6:
    print(Metrics.audioCap('audioCapture', ' ', 'perCPUaudioCapture', 'top'))

if args.option7:
    print(Metrics.v3xml0(v3_ccxml))

if args.option8:
    print(Metrics.v3xml0(nb_audio))

if args.option9:
    print(Metrics.v3xml0(nb_confsrv))
