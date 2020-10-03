import sys
import argparse

parser = argparse.ArgumentParser(description ='Command line BU Utility')
parser.add_argument('-r', '--root',
                    required = True,  
                    metavar = '',
                    help = 'Root Directory of Backup - Required!')

parser.add_argument('-s', '--source',
                    metavar = '',
                    help = 'Base Directory to be backed up')
parser.add_argument('-d', '--dest',
                    metavar = '',
                    help = 'Destination Directory for Backup')

args = parser.parse_args()


print(args.root)
print(args.source)
print(args.dest)



