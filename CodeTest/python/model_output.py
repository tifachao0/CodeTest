# import libraries
import glob
from os import path
from table import Table

# produce model output
def output(table, indexes, keys):
    table.print_entries(indexes, keys)
    print('\n')

if __name__ == '__main__':

    # get input files
    fpaths = glob.glob("../input/input_files/*.txt")
    fbasename = [path.basename(x) for x in fpaths]
    fdict = dict(zip(fbasename, [open(x) for x in fpaths]))

    # populate output table
    t1 = Table()
    t1.populate_table(fdict)

    print('Output 1:')
    output(t1, [2, 9, 1, 3, 7, 8, 5, 6, 4], ['last_name', 'first_name', 'gender', 'birth_date', 'color'])
    print('Output 2:')
    output(t1, [7, 9, 8, 3, 5, 6, 1, 2, 4], ['last_name', 'first_name', 'gender', 'birth_date', 'color'])
    print('Output 3:')
    output(t1, [4, 3, 1, 9, 2, 6, 5, 8, 7], ['last_name', 'first_name', 'gender', 'birth_date', 'color'])