#!/usr/bin/env python
#coding=utf8

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f','--foo')

parser.add_argument('bar1', choices=['a', 'b'])
parser.add_argument('bar2')
parser.add_argument('bar', nargs=argparse.REMAINDER)
parser.add_argument('-t','--text')
args = parser.parse_args()
print args
