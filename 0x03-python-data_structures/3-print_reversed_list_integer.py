#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):

    for i in range(len(my_list)):
        print('\n'.join(['{:d}'.format(n) for n in my_list[::-1]]))
