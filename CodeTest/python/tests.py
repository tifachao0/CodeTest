import glob
from os import path
from table import Table
import unittest

class TestTableMethods(unittest.TestCase):

    def setUp(self):
        self.fpaths = glob.glob("../input/input_files/*.txt")
        self.fbasename = [path.basename(x) for x in self.fpaths]
        self.fdict = dict(zip(self.fbasename, [open(x) for x in self.fpaths]))
        self.t1 = Table()

    def test_validateSetUp(self):
        self.assertEqual(self.fdict.keys().sort(), ['comma.text', 'pipe.txt', 'space.txt'].sort())

    def test_loadInputStrings(self):

        loaded_comma = self.t1.load_entries(self.fdict['comma.txt'], ',')
        loaded_pipe = self.t1.load_entries(self.fdict['pipe.txt'], '|')
        loaded_space = self.t1.load_entries(self.fdict['space.txt'], ' ')

        self.assertEqual(loaded_comma[0], ['Abercrombie', 'Neil', 'Male', 'Tan', '2/13/1943'])
        self.assertEqual(loaded_pipe[1], ['Bonk', 'Radek', 'S', 'M', 'Green', '6-3-1975'])
        self.assertEqual(loaded_space[2], ['Seles', 'Monica', 'H', 'F', '12-2-1973', 'Black'])

    def test_modelOutput(self):
        self.t1.populate_table(self.fdict)
        self.t1.print_entries([1, 2, 3, 4, 5, 6, 7, 8, 9], ['last_name', 'first_name', 'gender', 'birth_date', 'color'])

suite = unittest.TestLoader().loadTestsFromTestCase(TestTableMethods)
unittest.TextTestRunner(verbosity=2).run(suite)

