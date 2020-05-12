import pandas as pd
from prettytable import PrettyTable

year = input("input year >>")
semester = input("input semester >> ")
# to read csv file named "samplee"

# open csv file
a = open("./major/ict_"+str(year)+"_"+str(semester)+".csv","r",encoding='UTF-8')
# read the csv file
a = a.readlines()

# Seperating the Headers
l1 = a[0]
l1 = l1.split(',')

# headers for table
t = PrettyTable([l1[0],l1[1]])

# Adding the data
for i in range(1,len(a)):
    t.add_row(a[i].split(','))

code = t.get_html_string()
html_file = open("Table.htm","w")
html_file = html_file.wirte(code)
