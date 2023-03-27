import re


class RareMatrix:
    def __init__(self, file_path):
        self.path = file_path
        self.data = {}
        self.load_data()
        self.size = 0

    def load_data(self):
        with open(self.path, 'r') as f:
            self.size = int(f.readline())
            lines = f.readlines()
            for line in lines:

                line_split = line[:-1] if line[-1] == '\n' else line
                line_split = re.split(r'\s*,\s', line_split.strip())
                line_split[0] = float(line_split[0])
                line_split[1] = int(line_split[1])
                line_split[2] = int(line_split[2])

                if self.data.get(line_split[1]) is None:
                    self.data[line_split[1]] = {}
                self.data[line_split[1]][line_split[2]] = self.data[line_split[1]].get(line_split[2], 0) + line_split[0]
        return self.data
