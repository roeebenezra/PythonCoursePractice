# ex3 -  Roee Ben Ezra (roibe) 206123994
#        Yinon Tzomi (yinontz) 208489369
#
#  Ex4 - Regex on files

import re


# Q1
def create_list_of_biggest_cities(largest_cities):
    return{(re.search(r'[a-zA-Z]+[\s]?[a-zA-Z]*[A-Z]', city).group()[0:-1])
           for city in largest_cities}


def create_dict_of_postal_codes_cities(postal_codes):
    cities_postal_codes_dict = dict()
    for city in postal_codes:
        city_postal_code = re.search(r'([0-9]*),([a-zA-Z]+)', city)
        if city_postal_code:
            cities_postal_codes_dict[city_postal_code.group(2)] = city_postal_code.group(1)
    return cities_postal_codes_dict


def find_intersection(largest_cities_list, postal_code_list):
    return [(city, postal_code_list[city]) for city in largest_cities_list if city in postal_code_list.keys()]


def ex1():
    largest_cities = open("2019_largest_cities.txt")
    postal_codes = open("us_postal_codes.csv")

    largest_cities_list = create_list_of_biggest_cities(largest_cities)
    postal_code_list = create_dict_of_postal_codes_cities(postal_codes)
    intersection = find_intersection(largest_cities_list, postal_code_list)

    for city, postal_code in intersection:
        print(city, postal_code)

    largest_cities.close()
    postal_codes.close()


# Q2
def ex2():
    file = open("atoms2.log", 'r')
    file_out = open("output.log", 'w')
    content = file.readlines()
    for line in content:
        if re.search(r'\BFLOW', line) or re.search(r'\bALGORITHM', line):
            pass
        else:
            line_lst = line.split()
            file_out.write('file number: ' + line_lst[1] + ', file name: ' + line_lst[6] + '\n')

    file.close()
    file_out.close()


# main
if __name__ == '__main__':
    ex1()
    ex2()
