import pandas as pd
import numpy as np

# Michelle L. Gill, 2016-12-17

# This function uses pandas to infer types for and print
# a SQL schema for a csv file. The function reads the 
# first 1 million rows of the csv file and converts
# the pandas-inferred types to SQL types. Note that
# datetimes are usually read by pandas as an object
# so those types may need to be manually adjusted

# Inputs are the relative path to the csv file
# and a name for the table in SQL. 

# Relative path is preferred since the script
# adds a Linux home (/home/ubuntu) to the path.

def sql_schema(path, table_name):
    tbl = pd.read_csv(path, nrows=1000000)

    type_dict = {'object'  : 'varchar',
                 'float64' : 'numeric',
                 'int64'   : 'integer',
                 np.dtype('O')      : 'varchar',
                 np.dtype('float64'): 'numeric',
                 np.dtype('int64')  : 'numeric'}

    max_str = max([len(x) for x in tbl.columns])
    col_wid = max_str + 3
    col_str = '    {0: <' + str(col_wid) + '} {1}{2}'

    print("CREATE TABLE {} (".format(table_name))

    columns = tbl.columns
    for col in columns:
        if col == columns[-1]:
            punct = ');'
        else:
            punct = ','

        print(col_str.format(col, type_dict[tbl[col].dtype], punct))

    print('')
    print('COPY {}'.format(table_name))
    print('FROM \'/home/ubuntu/'+ path + '\'')
    print('DELIMITER \',\'')
    print('CSV HEADER;')

    return

# prints all scheme for a list of csv files and corresponding names
# do not include directories in list, use base_path

def print_all_schema(table_paths, table_names, base_path):

    for pth, nam in zip(table_paths, table_names):
        print('## {}'.format(nam))
        print('')

        try:
            print('```sql')
            sql_schema(base_path+pth, nam)
            print('```')
        except:
            print('ERROR')

        print('')

    return
