import argparse
import csv
#from prettytable import PrettyTable
'''
def printTable(list):
    table = PrettyTable()
    table.field_names = ["id", "task", "environment", "location", "team"]
    table.add_rows( list )
    print (table)'''
    
def openfile(file):
    try:
        with open(file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter='.')
            return list(spamreader)
    except FileNotFoundError:
        print("Oops!  That was no valid number.  Try again...")


class argFilter(argparse.ArgumentParser):
    def __init__(self,**kwarg) -> None:
        argparse.ArgumentParser.__init__(self,**kwarg)
    def parse_arguments(self):
        self.add_argument('-f', type=str, dest='file')
        self.add_argument('-i', type=str, nargs='+', dest='id')
        self.add_argument('-k', type=str, nargs='+', dest='task')
        self.add_argument('-e', type=str, nargs='+', dest='env')
        self.add_argument('-l', type=str, nargs='+', dest='loc')
        self.add_argument('-t', type=str, nargs='+', dest='team')
        
        self.args = self.parse_args()

    def list_filter(self, list):
        #new_set = set(list)
        filtered_list = filter( self.is_in_subset, list)
        return filtered_list

    def is_in_subset(self, server):
        return self.arg_set.issubset( set(server) )


    def argument_set(self):
        # append every argument list
        self.arg_list = []
        if self.args.id:
            self.arg_list = self.arg_list + self.args.id
        
        if self.args.task:
            self.arg_list = self.arg_list + self.args.task

        if self.args.env:
            self.arg_list = self.arg_list + self.args.env

        if self.args.loc:
            self.arg_list = self.arg_list + self.args.loc

        if self.args.team:
            self.arg_list = self.arg_list + self.args.team
        
        self.arg_set = set(self.arg_list)
    
    
        

# hold all the information necessary to parse the command line into Python data types.
parser = argFilter(description='Inventory Filter.')
parser.parse_arguments()
parser.argument_set()

lista = openfile(parser.args.file)

filtered_list = list( parser.list_filter(lista) )

for line in filtered_list:
    print(*line)

'''
for row in list:
    if args.id:
        if args.id not in row:



if(list):
    printTable(list)
    '''