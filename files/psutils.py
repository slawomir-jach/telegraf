import argparse
import psutil

def find_procs_by_name(name, val=None):


    "Return a list of processes matching 'name'."
    ls = []
    dct = {}
    for p in psutil.process_iter(['name']):
        if p.info['name'] == name:
            ls.append(p)
            dct = {name: 0}
    metric = ls[0].memory_info().vms

    dct[name] = metric
    print dct
    return dct

def test_arg2():
    print "test_arg2"

#find_procs_by_name('firefox')

parser = argparse.ArgumentParser()

parser.add_argument('--memory', help='finding memory usage by this app')
parser.add_argument('--option2', help='description for option2')
parser.add_argument('--option3', help='description for option3')

args = parser.parse_args()

if args.memory:
    find_procs_by_name('firefox')


if args.option2:
    test_arg2()

#if args.option3:
#    test_arg3()
