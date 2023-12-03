#!/usr/bin/python3
"""Defines a peak-finding algorithm."""

def find_peak(list_of_integers):
    """Finds a peak in a list of integers."""
    length = len(list_of_integers)

    if length == 0:
        return None

    mid = length // 2
    current = list_of_integers[mid]

    if (mid == 0 or current >= list_of_integers[mid - 1]) and (mid == length - 1 or current >= list_of_integers[mid + 1]):
        return current

    if mid > 0 and list_of_integers[mid - 1] > current:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
