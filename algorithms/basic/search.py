#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from random import randint


def simple_search(search_number, search_group):
    # With simple search the worst case is visiting all the elements in the search group
    print("Simple Search")

    position = None

    for i in range(0, len(search_group)):
        if search_number == search_group[i]:
            position = i
            break

    return position


def binary_search_recursive(search_number, search_group):
    print("Binary Search")
    # Sorted group of elements
    # log2(n) steps needed in worst case

    mid_position = round(len(search_group)/2)
    if search_number > search_group[mid_position]:
        return binary_search_recursive(search_number, search_group[mid_position:])
    elif search_number < search_group[mid_position]:
        return binary_search_recursive(search_number, search_group[:mid_position])
    else:
        return mid_position


MAX_NUMBER = 1000 * 1000
SEARCH_GROUP = range(1, MAX_NUMBER)

if __name__ == '__main__':
    print("Basic searching algorithms")
    start_time = time.time()
    random_number = randint(0, MAX_NUMBER)
    simple_pos = simple_search(random_number, SEARCH_GROUP)
    end_time_ms = (time.time() - start_time) * 1000
    if simple_pos:
        print("Found %i in position %i in %4.2f miliseconds" % (random_number, simple_pos, end_time_ms))
    else:
        print("Not Found %i after a search of %4.2f miliseconds" % (random_number, end_time_ms))
    start_time = time.time()
    binary_search_recursive(random_number, SEARCH_GROUP)
    end_time_ms = (time.time() - start_time) * 1000
    print("Found %i in position %i in %4.2f miliseconds" % (random_number, simple_pos, end_time_ms))
