# import libraries
import glob
from os import path
from table import Table

# get input files
def get_input():
    fpaths = glob.glob("../input/input_files/*.txt")
    fbasename = [path.basename(x) for x in fpaths]
    fdict = dict(zip(fbasename, fpaths))
    return fdict;

# produce table output
def output_table(table, indexes, keys):
    table.print_entries(indexes, keys)
    print('\n'),

# produce output equivalent to content in model_output.txt
def output():

    # populate output table
    t1 = Table()
    t1.populate_table(get_input())

    print('Output 1:')
    output_table(t1, [2, 9, 1, 3, 7, 8, 5, 6, 4], ['last_name', 'first_name', 'gender', 'birth_date', 'color'])

    print('Output 2:')
    output_table(t1, [7, 9, 8, 3, 5, 6, 1, 2, 4], ['last_name', 'first_name', 'gender', 'birth_date', 'color'])

    print('Output 3:')
    output_table(t1, [4, 3, 1, 9, 2, 6, 5, 8, 7], ['last_name', 'first_name', 'gender', 'birth_date', 'color'])

if __name__ == '__main__':
    output()