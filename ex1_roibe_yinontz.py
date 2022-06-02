"""
    names: Roi Ben Ezra, id:206123994 & Yinon Tzumi, id:208489369
    user nemes: roibe, yinontz

    This program manage sections 1-4 of the home exercise.
"""

###########################################
def how_many_times():
    """
    Reads two numbers and counts
    :return: how many times
             the digits from the first number
             exists in the second
    """
    num1 = read_num_and_convert_to_list()
    num2 = read_num_and_convert_to_dic()

    counter = 0
    for num in num1:
        if num2.keys().__contains__(num):
            counter += 1

    return counter
##############################################


def stack():
    """
    input: i-input to stack
           e-extract from stack last input
           p-print the stack
    :return: None
    """
    lst = []
    while True:
        inp = input("please enter char of action: ")
        match inp:
            case 'i':
                print("please enter a string to push into stack: ")
                lst.append(input()[1:])
            case 'e':
                if not lst:
                    break
                else:
                    lst.pop()
                    print("one item extracted from stack: ")
            case 'p':
                index = 1
                for i in lst:
                    print(index, " ", i)
                    index += 1
            case _:
                break
##############################################


def genes():
    # find the best genes in genes list
    genes_lst = [['B2B', 'HLA_A', 'AMHR2', 590, 0.12],           ['B2B', 'HLA_A', 'AMH', 591, 0.12],
                 ['B2B', 'HLA_A', 'AMICA1', 592, 0.12],          ['B2B', 'HLA_A', 'AMIGO1', 593, 0.12],
                 ['B2B', 'HLA_A', 'AMIGO2', 594, 0.12],          ['B2B', 'HLA_A', 'AMIGO3', 595, 0.12],
                 ['B2B', 'HLA_A', 'AMMECR1L', 596, 0.12],        ['B2B', 'HLA_A', 'AMMECR1', 597, 0.12],
                 ['B2B', 'HLA_A', 'AMN1', 598, 0.12],            ['B2B', 'HLA_A', 'AMN', 599, 0.12],
                 ['B2B', 'HLA_A', 'AMOTL1', 600, 0.12],          ['B2B', 'HLA_A', 'AMOTL2', 601, 0.12],
                 ['B2B', 'HLA_A', 'AMOT', 602, 0.12],            ['B2B', 'HLA_A', 'AMPD1', 603, 0.12],
                 ['B2B', 'HLA_A', 'AMPD2', 604, 0.12],           ['B2B', 'HLA_A', 'AMPD3', 605, 0.12],
                 ['B2B', 'HLA_A', 'AMPH', 606, 0.0019],          ['B2B', 'HLA_A', 'AMTN', 607, 0.12],
                 ['B2B', 'HLA_A', 'AMT', 608, 0.12],             ['B2B', 'HLA_A', 'AMY1A', 609, 0.12],
                 ['B2B', 'HLA_A', 'AMY2A', 610, 0.0019],         ['B2B', 'HLA_A', 'AMY2B', 611, 0.12],
                 ['B2B', 'HLA_A', 'AMZ1', 612, 0.12],            ['B2B', 'HLA_A', 'AMZ2P1', 613, 0.12],
                 ['B2B', 'HLA_A', 'AMZ2', 614, 0.12],            ['B2B', 'HLA_A', 'ANAPC10', 615, 0.12],
                 ['B2B', 'HLA_A', 'ANAPC11', 616, 0.12],         ['B2B', 'HLA_A', 'ANAPC13', 617, 0.12],
                 ['B2B', 'HLA_A', 'ANAPC16', 618, 0.12],         ['B2B', 'HLA_A', 'ANAPC1', 619, 0.12],
                 ['B2B', 'HLA_A', 'ANAPC2', 620, 0.0019],        ['B2B', 'HLA_A', 'ANAPC4', 621, 0.0019],
                 ['B2B', 'HLA_A', 'ANAPC5', 622, 0.12],          ['B2B', 'HLA_A', 'ANAPC7', 623, 0.12],
                 ['B2B', 'HLA_A', 'ANGEL1', 624, 0.12],          ['B2B', 'HLA_A', 'ANGEL2', 625, 0.12],
                 ['B2B', 'HLA_A', 'ANGPT1', 626, 0.12],          ['B2B', 'HLA_A', 'ANGPT2', 627, 0.12],
                 ['B2B', 'HLA_A', 'ANGPT4', 628, 0.12],          ['B2B', 'HLA_A', 'ANGPTL1', 629, 0.12],
                 ['B2B', 'HLA_A', 'ANGPTL2', 630, 0.12],         ['B2B', 'HLA_A', 'ANGPTL3', 631, 0.12],
                 ['B2B', 'HLA_A', 'ANGPTL4', 632, 0.12],         ['B2B', 'HLA_A', 'ANGPTL5', 633, 0.12],
                 ['B2B', 'HLA_A', 'ANGPTL6', 634, 0.12],         ['B2B', 'HLA_A', 'ANGPTL7', 635, 0.12],
                 ['B2B', 'HLA_A', 'ANG', 636, 0.12],             ['B2B', 'HLA_A', 'ANK1', 637, 0.0019],
                 ['B2B', 'HLA_A', 'ANK2', 638, 0.0019],          ['B2B', 'HLA_A', 'ANK3', 639, 0.12],
                 ['B2B', 'HLA_A', 'ANKAR', 640, 0.12],           ['B2B', 'HLA_A', 'ANKDD1A', 641, 0.12],
                 ['B2B', 'HLA_A', 'ANKFN1', 642, 0.0019],        ['B2B', 'HLA_A', 'ANKFY1', 643, 0.12],
                 ['B2B', 'HLA_A', 'ANKHD1_EIF4EBP3', 644, 0.12], ['B2B', 'HLA_A', 'ANKHD1', 645, 0.12]]

    best_gens = []
    for sub_list in genes_lst:
        if sub_list[4] < 0.1:
            for gen in range(len(sub_list)-2):
                best_gens.append(sub_list[gen])

    best_list = list(dict.fromkeys(best_gens))      # sort & delete duplicates
    print(best_list)

##############################################


def read_num_and_convert_to_list():
    """
             reads number
    :return: list of the nuber
    """
    num = input("Enter a number\n")
    return [int(x) for x in num]
##############################################


def read_num_and_convert_to_dic():
    """
    reads number
    :return: dictionary of the number
    """
    num = input("Enter a number\n")
    return {int(x): 0 for x in num}
##############################################


def caesar_cipher():
    """
    reads code and performs
    decode to 13 char back
    without symbols
    """
    code = input("Enter a code\n")

    code = map(sub13, code)

    for i in code:
        print(i)
##############################################


def sub13(char):
    """

    :param char: char to take 13 places back
    :return:
    """
    if char.isalpha():
        if char.isupper():
            ret = chr((((ord(char) - ord('A')) - 13) % 26) + ord('A'))
            return ret
        else:
            ret = chr((((ord(char) - ord('a')) - 13) % 26) + ord('a'))
            return ret
    else:
        return char
###################################################


if __name__ == '__main__':
    while True:
        section = input("please choose section between 1-4: ")
        match section:
            case '1':
                print(how_many_times())     # find num of digits of two numbers : question 1
            case '2':
                stack()                    # make a stack of strings  : question 2
            case '3':
                genes()                    # find the best genes      : question 3
            case '4':
                caesar_cipher()           # create caesar code from a string : question 4
