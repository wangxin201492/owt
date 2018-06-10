import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f','--foo')

parser.add_argument('bar')
args = parser.parse_args()
print args
