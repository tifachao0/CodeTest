import time

class Table:

    def __init__(self):
        self.numItems = 0
        self.t = {
            'id': [],
            'last_name': [],
            'first_name': [],
            'gender': [],
            'birth_date': [],
            'color': [],
            'other': []
        }

    def populate_table(self, fdict):
        for key, value in fdict.iteritems():
            if key == 'comma.txt':
                loaded = self.load_entries(value, ',')
                for entry in loaded:
                    self.t['last_name'].append(entry[0])
                    self.t['first_name'].append(entry[1])
                    self.t['gender'].append(entry[2])
                    self.t['color'].append(entry[3])
                    self.t['birth_date'].append(entry[4])
                    self.t['other'].append(None)
                    self.increment_id()
            elif key == 'pipe.txt':
                loaded = self.load_entries(value, '|')
                for entry in loaded:
                    self.t['last_name'].append(entry[0])
                    self.t['first_name'].append(entry[1])
                    self.t['gender'].append(self.convert_gender(entry[3]))
                    self.t['color'].append(entry[4])
                    self.t['birth_date'].append(self.convert_datetime(entry[5]))
                    self.t['other'].append(None)
                    self.increment_id()
            elif key == 'space.txt':
                loaded = self.load_entries(value, ' ')
                for entry in loaded:
                    self.t['last_name'].append(entry[0])
                    self.t['first_name'].append(entry[1])
                    self.t['gender'].append(self.convert_gender(entry[3]))
                    self.t['birth_date'].append(self.convert_datetime(entry[4]))
                    self.t['color'].append(entry[5])
                    self.t['other'].append(None)
                    self.increment_id()
            else:
                print("unknown filename")

    # print entries
    def print_entries(self, indexes, keys):
        entries = self.get_entries(indexes, keys)
        for e in entries:
            print(' '.join(e))

    # multiple entries
    def get_entries(self, indexes, keys):
        entries = []
        for i in indexes:
            entries.append(self.get_entry(i, keys))
        return entries

    # one entry, can get subset of columns in table
    def get_entry(self, index, keys):
        entry = []
        for k in keys:
            if self.t.has_key(k):
                value = self.t[k]
                if index > 0 and index <= len(value):
                    entry.append(value[index - 1])
                else:
                    print("index out of bounds")
            else:
                print(k + " does not exist")
        return entry

    def load_entries(self, file, delimiter):
        loaded = []
        for line in file:
            input_strings = line.split(delimiter) # split line into separate strings
            input_strings = [i.strip() for i in input_strings] # remove beginning/trailing spaces and newlines
            loaded.append(input_strings)
        return loaded

    def increment_id(self):
        self.numItems += 1
        self.t['id'].append(self.numItems)

    def convert_gender(self, gender):
        if (gender == 'M'):
            return 'Male'
        elif (gender == 'F'):
            return 'Female'
        else:
            print ("Invalid input")

    def convert_datetime(self, datetime):
        t = time.strptime(datetime, "%m-%d-%Y")
        s = time.strftime("%-m/%-d/%Y", t)
        return s







