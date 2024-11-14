import cmd
from createcsv import create_csv
import csv
import pandas as pd
import yaml
import sys
import logging



# Define the class RecordManagerCLI which inherits from cmd.Cmd 
class RecordManagerCLI(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = 'RecordManager>>'
        self.intro = 'Welcome to RecordManager CLI. Type "help" to see available commands'


    # Sort csv file by division and points
    def do_sort_records(self,line):
        logging.basicConfig(filename="error.log", level=logging.ERROR)
        try:
            # Read csv file using Pandas
            csvdata = pd.read_csv("records.csv")
            print("\n records before sorting:\n")
            print(csvdata)

        except Exception as e:
            print("Error",e)
            print("Something went wrong")
            logging.error("Exception occured:%s",str(e),exc_info=True)

        # Sort csv file data by columns using Pandas sort_values()
        csvdata.sort_values(["Division","Points"],
                                      axis=0,
                                      ascending=[True,True],
                                      inplace=True)
        
        print("\n records after sorting:\n")
        print(csvdata)
        

       
    # Select only the first three records
    def do_select_top_three(self,line):

        logging.basicConfig(filename="error.log", level=logging.ERROR)
        try:
            # Read first three rows of the records.csv file using read_csv() nrows parameter
            csvdata = pd.read_csv("records.csv", nrows=3)
            print("\n top 3 records:\n")
            print(csvdata)

        except Exception as e:
            print("Error",e)
            print("Something went wrong")
            logging.error("Exception occured:%s",str(e),exc_info=True)

        

    # Displays the csv file
    def do_get_records(self, line):
        logging.basicConfig(filename="error.log", level=logging.ERROR)
        try:
            csvdata = pd.read_csv("records.csv")
            print(csvdata)
            
        except Exception as e:
            print("Error",e)
            print("Something went wrong")
            logging.error("Exception occured:%s",str(e),exc_info=True)
  

    # Exit CLI tool to stdout
    def do_quit_or_stdout(self, line):
        return True      
 


    # Documentation for the commands. Example: type 'help printfile' as command to view documentation for printfile command.
    def help_get_records(self):
        print("Print record.csv file")

    def help_sort_records(self):
        print("Sorts the records by division and points")

    def help_select_top_three(self):
        print("Selects the top three records")

    def help_quit_or_stdout(self):
        print("exit the CLI tool / to view stdout data")
        


    # Add an empty line after each command to improve readability in the CLI output
    def postcmd(self, stop,line):
        print()
        return stop



# Create an instance of RecordManagerCLI() class
cli = RecordManagerCLI()
# Call the mainloop method to start the CLI
cli.cmdloop()   



def readcsv():
    df = pd.read_csv('recordst.csv')
    data = df.to_dict(orient='records')
    for row in data:
        yield row


def csv_to_yaml():
    print("records:")   
    for idx, row in enumerate(readcsv()):
        if idx > 10: 
            return   
        sys.stdout.write(" \nname:%(Firstname)s %(Lastname)s\n details: In division %(Division)s from %(Date)s performing %(Summary)s\n" % row)
        
csv_to_yaml()
            


"""def csv_to_yaml():
    df = pd.read_csv('records.csv')
    with open('recordst.yaml','w') as yamlfile:
        yaml.dump(df.to_dict(orient='records'),yamlfile,sort_keys=False)

    yamfileout = open('records.yaml').read()
    return yamfileout
    
output=csv_to_yaml()
print(output)"""




