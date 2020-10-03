#! /usr/bin/python3
""" Opens and processes lake level report from hobolink website defined
    input_path variable.
    
    User must retrieve data file, rename and place in right folder or
    optionally change the 'input_path' variable below to match path to
    report file. The report file must be a csv file with data in the
    following format: ['mm/dd/yy hh:mm:ss', '-##.##']
    
    The 'date time' data is seperated into separate fields and then filtered
    based on time = 'time_filter' variable. The resulting data is written
    to the file defined in the variable 'out_path'."""
    

import csv
import sys

input_path = 'C:\\Users\\Don\\Desktop\\LL_Data.csv'
output_path = 'C:\\Users\\Don\\Desktop\\filtered_ll_data.csv'
time_filter = '08:00:00'
output_header = ['Date', 'Time','LL(inches)'] #header for output file

# open files and set up reader and writer
try:
    ip_file = open(input_path,'r')
except Exception as e:
    print(f'Error opening ll data: {e}')
    sys.exit()
    
try:
    op_file = open(output_path, 'w', newline = '')
except Exception as e:
    print(f'Error opening filtered output file: {e}')
    ip_file.close() #assumes input file was successfully opened
    sys.exit()

csv_reader = csv.reader(ip_file)
next(csv_reader) # first line is the header. don't need. It's a throwaway

csv_writer = csv.writer(op_file)  
csv_writer.writerow(output_header) #new header needed for out_file

def date_time_split(csv_reader):
    """ generater that yields a new row whose time matches the time_filter
        variable.
        input from the csv_reader
            input row[0] contains the date and time string 'mm/dd/yy hh:mm:ss'
            input row[1] contains the level string '##.##'"""

    for row in csv_reader:
        # this next line splits 'date time' into ['mm/dd/yy', 'hh:mm:ss]       
        date_time = row[0].split(sep = ' ')

        if date_time[1] == time_filter:
            yield [date_time[0], date_time[1], row[1]]
        


output_gen=(row for row in date_time_split(csv_reader)) # generator not a list

csv_writer.writerows(output_gen)


##cleanup
ip_file.close()
op_file.close()
