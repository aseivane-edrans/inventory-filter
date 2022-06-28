import argparse
import csv

def openfile(file):
    try:
        with open(file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter='.')
            return list(spamreader)
    except FileNotFoundError:
        print("Oops!  That was no valid number.  Try again...")

def parse_arguments(parser):
    parser.add_argument('-f', type=str, dest='file')
    parser.add_argument('-i', type=str, nargs='+', dest='id')
    parser.add_argument('-k', type=str, nargs='+', dest='task')
    parser.add_argument('-e', type=str, nargs='+', dest='env')
    parser.add_argument('-l', type=str, nargs='+', dest='loc')
    parser.add_argument('-t', type=str, nargs='+', dest='team')
    return parser.parse_args()



# hold all the information necessary to parse the command line into Python data types.
parser = argparse.ArgumentParser(description='Inventory Filter.')
args = parse_arguments(parser)

list = openfile(args.file)


for line in list:
    print(*line)
'''
for row in list:
    if args.id:
        if args.id not in row:



if(list):
    printTable(list)
    '''