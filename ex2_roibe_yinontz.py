# ex2 -  Roee BenEzra 206123994
#        Yinon Tzomi  208489369
#
# create csv files - python


# return list of columns names
def name_of_columns(file):
    column_name = []
    line = file.readline()
    while line:
        start = line.lstrip()   # remove wide space from began of line
        if start.startswith('`'):
            column_name.append(start.split()[0].strip('`'))
        else:
            return column_name
        line = file.readline()


# insert data to csc file
def data_insert(src_file, des_file):
    line = src_file.readline()
    while line:
        start = line.lstrip()
        if start.startswith('INSERT INTO'):
            line_list = extract_data(start)
            write_to_file(line_list, des_file)
        elif start.startswith('UNLOCK TABLE'):
            return
        line = src_file.readline()


# extract data  of head-line
def extract_data(head_line):
    head_line = head_line[head_line.find('('):-2]
    head_line = head_line.lstrip('(').rstrip(')')
    head_line = head_line.replace("'", '"')
    return head_line.split('),(')


# write to csv file
def write_to_file(line, des_file):
    des_file.writelines(map(lambda s: s + '\n', line))


# create csc file
def create_csv(file, index, table_name):
    file_name = table_name + '.csv'
    file.seek(index)
    columns = name_of_columns(file)
    with open(file_name, 'w+') as csv:
        columns = ','.join(columns) + '\n'
        csv.write(columns)
        data_insert(file, csv)


def check_if_insert(file, key, end):
    line = file.readline()
    while line:
        start = line.lstrip()
        if start.startswith(key):
            return True
        elif start.startswith(end):
            return False
        line = file.readline()


def convert_sql_to_csv(file_name):
    with open(file_name, 'r') as file:
        line = file.readline()
        while line:
            if line.startswith('CREATE TABLE'):
                index = file.tell()
                table_name = line.split()[2]
                if check_if_insert(file, 'INSERT INTO', 'UNLOCK TABLE'):
                    create_csv(file, index, table_name)
            line = file.readline()


if __name__ == "__main__":
    # open sql file
    convert_sql_to_csv('demo.sql')
