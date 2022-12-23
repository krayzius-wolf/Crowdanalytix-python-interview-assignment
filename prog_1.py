import argparse


# Custom error created. Error statement generated when raised.

class DuplicateFoundError(Exception):

    def __init__(self, i):
        self.i = i

    def __str__(self):
        return 'Duplicate found at index ' + str(self.i)


# Class initialized with the array. Operations are performed to obtain required output.

class ops:

    '''
    Throws an exception when first occurence of duplicate is encountered. Acoording to the ques. all duplicate values
    had to be removed and reversed list has to be returned. However according to the sub ques. only error had to be
    returned with no further output rquired. Program written as per sub ques.
    '''

    def __init__(self, arr):
        self.arr = arr

    def operations(self):
        output = []
        for i in enumerate(self.arr):
            if i[1] not in output:
                output.append(i[1])
            else:
                raise DuplicateFoundError(i[0])
        output.reverse()
        return output


def main():
    '''
    Validates input with N. Creates object and performs operation. Raises appropriate error if reqd.
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('N', type=int)
    parser.add_argument('input_array', type=int, nargs='+')
    args = parser.parse_args()
    if args.N != len(args.input_array):
        print ('The no .of elements to be enterred as part of array should match first arguement(N)')
        exit()
    c = ops(args.input_array)
    try:
        print (c.operations())
    except DuplicateFoundError as error:
        print (error.__str__())


main()
