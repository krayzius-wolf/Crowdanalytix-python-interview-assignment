import argparse


def strops(s):
    '''
    Performs reqd. string operations. A string given in input file is seperated at hyphen and stored as a list
    of words. Order is reversed and the words are joind into requd strings.
    '''

    l = []
    [l.append(i.split('-')) for i in s]
    [i.reverse() for i in l]
    for i in enumerate(l):
        l[i[0]] = '-'.join(i[1])
    return l


def main():
    '''
    Input is provided as a txt file thats converted to list of test cases.
    Each of this test cases are processed and printed.
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str,
                        help='Enter the absolute path of the input text file containing the text cases'
                        )
    args = parser.parse_args()
    lines = []
    with open(args.path) as f:
        lines = f.readlines()
    lines = lines[1:]
    for i in enumerate(lines):
        lines[i[0]] = i[1].strip('\n')
    p = strops(lines)
    for i in p:
        print(i)


main()
