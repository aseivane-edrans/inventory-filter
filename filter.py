import argparse
import csv
from prettytable import PrettyTable

def printTable(table):
    new_table = PrettyTable()
    new_table.field_names = ["id", "task", "environment", "location", "team"]
    new_table.add_rows( table )
    print (new_table)
    
def openfile(server_file):
    try:
        with open(server_file, newline='') as csvfile:
            opened_csv = csv.reader(csvfile, delimiter='.')
            return list(opened_csv)
    except FileNotFoundError:
        print("File doesn't exist")
        exit()


class argFilter(argparse.ArgumentParser):

    def __init__(self,**kwarg) -> None:
        argparse.ArgumentParser.__init__(self,**kwarg)
        
    def parse_arguments(self):
        self.add_argument('-f', type=str, dest='file')
        self.add_argument('-i', type=str, dest='id')
        self.add_argument('-k', type=str, dest='task')
        self.add_argument('-e', type=str, dest='env')
        self.add_argument('-l', type=str, dest='loc')
        self.add_argument('-t', type=str, dest='team')
        
        self.args = self.parse_args()

    def list_filter(self, clean_list):
        self.argument_set()
        filtered_list = filter( self.is_in_subset, clean_list)
        return filtered_list

    def is_in_subset(self, server):
        return self.arg_set.issubset( set(server) )


    def argument_set(self):
        # append every argument list
        self.arg_list = []
        if self.args.id:
            self.arg_list.append(self.args.id)
        
        if self.args.task:
            self.arg_list.append(self.args.task)

        if self.args.env:
            self.arg_list.append(self.args.env)

        if self.args.loc:
            self.arg_list.append(self.args.loc)

        if self.args.team:
            self.arg_list.append(self.args.team)
        
        self.arg_set = set(self.arg_list)
    
    
        

# hold all the information necessary to parse the command line into Python data types.
parser = argFilter(description='Inventory Filter.')
# parse the arguments
parser.parse_arguments()

#opens the file and returns a list with server parameters
server_list = openfile(parser.args.file)

# filters the server_list passed to the filter. Returns a filtered list
filtered_list = list( parser.list_filter(server_list) )

# if filtered_list has data, prints it
if(filtered_list):
    printTable(filtered_list)
else:
    print ( "No match for the input")
    exit()
