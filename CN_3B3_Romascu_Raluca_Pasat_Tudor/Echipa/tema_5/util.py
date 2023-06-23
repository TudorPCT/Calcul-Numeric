import re


def load_rare_matrix(a_path, epsilon):
    with open(a_path, 'r') as f:
        size = int(f.readline())
        a = [[] for _ in range(size)]
        for line in f.readlines():

            line_split = line[:-1] if line[-1] == '\n' else line
            line_split = re.split(r'\s*,\s', line_split.strip())
            line_split[0] = float(line_split[0])
            line_split[1] = int(line_split[1])
            line_split[2] = int(line_split[2])

            if line_split[1] == line_split[2] and abs(line_split[0]) < epsilon:
                raise Exception("Diagonal element is null")

            if (line_split[0], line_split[2]) not in a[line_split[1]]:
                a[line_split[1]].append((line_split[0], line_split[2]))
            else:
                a[line_split[1]][0] += line_split[0]

    return a, size


def load_vector(b_path):
    b = []
    with open(b_path, 'r') as f:
        size = int(f.readline())

        for line in f.readlines():
            _line = line[:-1] if line[-1] == '\n' else line
            _line = float(_line.strip())
            b.append([_line])

    return b, size
