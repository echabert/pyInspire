from core.pyInspire import *
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-c','--command',  metavar='COMMAND', help='request following inspire cammands')
args = parser.parse_args()
print(args)
print(args.command)

insp = pyInspire()

titles = insp.request(args.command)
for i in titles:
    print(i)


