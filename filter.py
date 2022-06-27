import argparse
import csv

def openfile(file):
    try:
        with open(file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter='.')
            return list(spamreader)
    except FileNotFoundError:
        print("Oops!  That was no valid number.  Try again...")


spamreader = openfile()
if(spamreader):
    for row in spamreader:
        print(row)

'''
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
'''