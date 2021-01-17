#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from random import randint


def simple_search(search_number, search_group):
    print("Simple Search")

    position = None

    for i in range(0, len(search_group)):
        if search_number == search_group[i]:
            position = i
            break

    return position


def binary_search_recursive(search_number, search_group):
    # Sorted group of elements
    # log2(n) steps needed in worst case

    def search(offset, number, group):
        mid_position = round(len(group) / 2)

        # print(offset, mid_position, group)

        if len(group) == 1:
            return None

        if search_number > group[mid_position]:
            offset += mid_position
            return search(offset, number, group[mid_position:])
        elif search_number < group[mid_position]:
            return search(offset, number, group[:mid_position])
        elif search_number == group[mid_position]:
            return offset + mid_position
        else:
            # This case must not happen
            return None

    position = search(0, search_number, search_group)

    return position


def binary_search(search_number, search_group):
    # Sorted group of elements
    # log2(n) steps needed in worst case

    position = None
    start = 0
    end = len(search_group)
    mid = round((start + end) / 2)

    while start <= end:
        # print(start, end, mid)
        guess = search_group[mid]
        if search_number > guess:
            start = mid
            mid = round((mid + end) / 2)
        elif search_number < guess:
            end = mid
            mid = round((start + mid) / 2)
        elif search_number == guess:
            position = mid
            break
        else:
            # This case must not happen
            position = None
            break

    return position


def compute_search(search_func, search_number, search_group):
    start_time_compute = time.time()
    position = search_func(search_number, search_group)
    end_time_compute_ms = (time.time() - start_time_compute) * 1000
    if position:
        print("%s Found %i in position %i in %4.2f miliseconds"
              % (search_func, search_number, position, end_time_compute_ms))
    else:
        print("%s does not found %i in %4.2f miliseconds"
              % (search_func, search_number, end_time_compute_ms))

    return position


MAX_NUMBER = 1000 * 1000
SEARCH_GROUP = range(1, MAX_NUMBER)

if __name__ == '__main__':
    print("Basic searching algorithms")
    random_number = randint(0, MAX_NUMBER)
    pos_simple = compute_search(simple_search, random_number, SEARCH_GROUP)
    pos_binary = compute_search(binary_search, random_number, SEARCH_GROUP)
    pos_binary_rec = compute_search(binary_search_recursive, random_number, SEARCH_GROUP)
    assert(pos_simple == pos_binary_rec)
    assert(pos_simple == pos_binary)

