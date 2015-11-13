import glob
import model_output
from os import path
import sys
from cStringIO import StringIO
from table import Table
import unittest

class TestTableMethods(unittest.TestCase):

    def setUp(self):
        self.fpaths = glob.glob("../input/input_files/*.txt")
        self.fbasename = [path.basename(x) for x in self.fpaths]
        self.fdict = dict(zip(self.fbasename, self.fpaths))
        self.t1 = Table()

    def test_validateSetUp(self):
        self.assertEqual(self.fdict.keys().sort(), ['comma.text', 'pipe.txt', 'space.txt'].sort())

    def test_loadEntries(self):

        entries_comma = self.t1.load_entries(self.fdict['comma.txt'], ',')
        entries_pipe = self.t1.load_entries(self.fdict['pipe.txt'], '|')
        entries_space = self.t1.load_entries(self.fdict['space.txt'], ' ')

        self.assertEqual(entries_comma[0], ['Abercrombie', 'Neil', 'Male', 'Tan', '2/13/1943'])
        self.assertEqual(entries_pipe[1], ['Bonk', 'Radek', 'S', 'M', 'Green', '6-3-1975'])
        self.assertEqual(entries_space[2], ['Seles', 'Monica', 'H', 'F', '12-2-1973', 'Black'])

    def test_populateTable(self):

        dict_comma = {"comma.txt": self.fdict["comma.txt"]}
        self.t1.populate_table(dict_comma)

        self.assertEqual(self.t1.data['last_name'], ['Abercrombie', 'Bishop', 'Kelly'])
        self.assertEqual(self.t1.data['first_name'], ['Neil', 'Timothy', 'Sue'])
        self.assertEqual(self.t1.data['gender'], ['Male', 'Male', 'Female'])
        self.assertEqual(self.t1.data['color'], ['Tan', 'Yellow', 'Pink'])
        self.assertEqual(self.t1.data['birth_date'], ['2/13/1943', '4/23/1967', '7/12/1959'])
        self.assertEqual(self.t1.data['other'], ['', '', ''])

    def test_getEntry(self):

        dict_comma = {"comma.txt": self.fdict["comma.txt"]}
        self.t1.populate_table(dict_comma)

        self.assertEqual(self.t1.get_entry(1, ['last_name']), ['Abercrombie'])
        self.assertEqual(self.t1.get_entry(1, ['last_name', 'first_name']), ['Abercrombie', 'Neil'])
        self.assertEqual(self.t1.get_entry(1, ['color', 'first_name']), ['Tan', 'Neil'])

    def test_getEntries(self):

        dict_comma = {"comma.txt": self.fdict["comma.txt"]}
        self.t1.populate_table(dict_comma)

        self.assertEqual(self.t1.get_entries([1, 3], ['last_name']), [['Abercrombie'], ['Kelly']])
        self.assertEqual(self.t1.get_entries([3, 1], ['last_name', 'first_name']), [['Kelly', 'Sue'], ['Abercrombie', 'Neil']])

    def test_printEntries(self):

        dict_pipe = {"pipe.txt": self.fdict["pipe.txt"]}
        self.t1.populate_table(dict_pipe)

        # get print output
        defaultStdout = sys.stdout # save stdout to value
        printOutput = StringIO()
        sys.stdout = printOutput
        self.t1.print_entries([1], ['last_name', 'first_name'])
        sys.stdout = defaultStdout

        self.assertEqual(printOutput.getvalue(), 'Smith Steve\n')

    def test_modelOutput(self):

        # get print output from table
        defaultStdout = sys.stdout # save stdout to value
        printOutput = StringIO()
        sys.stdout = printOutput
        model_output.output()
        sys.stdout = defaultStdout

        # get content of model_output.txt
        f = open("../input/model_output.txt")
        txt = f.read()
        f.close()

        self.assertEqual(printOutput.getvalue(), txt)

suite = unittest.TestLoader().loadTestsFromTestCase(TestTableMethods)
unittest.TextTestRunner(verbosity=2).run(suite)

