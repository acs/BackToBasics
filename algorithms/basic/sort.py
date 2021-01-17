#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from random import randint


GROUP_SIZE = 10000
MAX_NUMBER = 10000


def generate_random(size):
    group = []

    for i in range(0, size):
        group.append(randint(0, MAX_NUMBER))

    return group


def selection_sort(group):
    sorted_group = []
    group_copy = group.copy()

    while group_copy:
        min_item = group_copy[0]
        for item in group_copy:
            min_item = item if item < min_item else min_item
        sorted_group.append(min_item)
        group_copy.remove(min_item)

    return sorted_group


def compute_sort(sort_func, sort_group):
    start_time_compute = time.time()
    sorted_group = sort_func(sort_group)
    end_time_compute_ms = (time.time() - start_time_compute) * 1000
    print("%s Sort group with %i items in %4.2f miliseconds"
          % (sort_func, len(sorted_group), end_time_compute_ms))

    return sorted_group


if __name__ == '__main__':
    print("Basic searching algorithms")
    random_group = generate_random(GROUP_SIZE)
    sorted_selection_group = compute_sort(selection_sort, random_group)
    assert(len(random_group) == len(sorted_selection_group))
    print(sorted_selection_group)


