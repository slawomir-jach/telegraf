#!/usr/bin/python

import os
import json
import argparse
import subprocess
from vars import *
from metricsClass import *

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
