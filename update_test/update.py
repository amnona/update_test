#!/usr/bin/env python

# amnonscript

import argparse
import sys
import time
import subprocess

__version__ = "0.1"


def generic(name):
	print('ooga')
	subprocess.run('ls')
	subprocess.run(['pip','install','--upgrade','git+git://github.com/amnona/update_test.gut'])
	while True:
		print('pita')
		time.sleep(1)
	print('done')


def main(argv):
	parser = argparse.ArgumentParser(description='generic version %s.' % __version__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-i', '--input', help='name of input fasta file')
	parser.add_argument('-k', '--keep_primers', help="Don't remove the primer sequences", action='store_true')

	args = parser.parse_args(argv)
	generic(args.input)


if __name__ == "__main__":
	main(sys.argv[1:])
