import time

class Table:

    # create empty table
    def __init__(self):
        self.numItems = 0
        self.data = {
            'id': [],
            'last_name': [],
            'first_name': [],
            'gender': [],
            'birth_date': [],
            'color': [],
            'other': []
        }

    # populate table with values from input files
    def populate_table(self, fdict):
        for key, value in fdict.iteritems():
            if key == 'comma.txt':
                loaded = self.load_entries(value, ',')
                for entry in loaded:
                    self.data['last_name'].append(entry[0])
                    self.data['first_name'].append(entry[1])
                    self.data['gender'].append(entry[2])
                    self.data['color'].append(entry[3])
                    self.data['birth_date'].append(entry[4])
                    self.data['other'].append("") # nothing here
                    self.increment_id()
            elif key == 'pipe.txt':
                loaded = self.load_entries(value, '|')
                for entry in loaded:
                    self.data['last_name'].append(entry[0])
                    self.data['first_name'].append(entry[1])
                    self.data['gender'].append(self.convert_gender(entry[3]))
                    self.data['color'].append(entry[4])
                    self.data['birth_date'].append(self.convert_datetime(entry[5]))
                    self.data['other'].append(entry[2])
                    self.increment_id()
            elif key == 'space.txt':
                loaded = self.load_entries(value, ' ')
                for entry in loaded:
                    self.data['last_name'].append(entry[0])
                    self.data['first_name'].append(entry[1])
                    self.data['gender'].append(self.convert_gender(entry[3]))
                    self.data['birth_date'].append(self.convert_datetime(entry[4]))
                    self.data['color'].append(entry[5])
                    self.data['other'].append(entry[2])
                    self.increment_id()
            else:
                print("unknown filename")

    # print entries
    def print_entries(self, ids, keys):
        entries = self.get_entries(ids, keys)
        for e in entries:
            print(' '.join(e))

    # get multiple entries
    def get_entries(self, ids, keys):
        entries = []
        for i in ids:
            entries.append(self.get_entry(i, keys))
        return entries

    # get one entry, can get subset of keys in table
    def get_entry(self, id, keys):
        entry = []
        for k in keys:
            if self.data.has_key(k):
                value = self.data[k]
                if id > 0 and id <= len(value):
                    entry.append(value[id - 1]) # get value index
                else:
                    print("index out of bounds")
            else:
                print(k + " does not exist")
        return entry

    # load each line from file as list of strings
    def load_entries(self, file, delimiter):
        loaded = []
        f = open(file)
        for line in f:
            input_strings = line.split(delimiter) # split line into separate strings
            input_strings = [i.strip() for i in input_strings] # remove beginning/trailing spaces and newlines
            loaded.append(input_strings)
        f.close()
        return loaded

    # increment id as entries are added to table. count starts from 1
    def increment_id(self):
        self.numItems += 1
        self.data['id'].append(self.numItems)

    # convert abbreviation to full name
    def convert_gender(self, gender):
        if (gender == 'M'):
            return 'Male'
        elif (gender == 'F'):
            return 'Female'
        else:
            print ("Invalid input")

    # convert date format
    def convert_datetime(self, datetime):
        t = time.strptime(datetime, "%m-%d-%Y")
        s = time.strftime("%-m/%-d/%Y", t)
        return s







