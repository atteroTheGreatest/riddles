"""Implement an algorithm to determine if a string has all
unique characters. What if you can not use additional data
structures?
"""
import itertools


def has_all_unique_characters(text):
    found_letters = set()
    for letter in text:
        if letter not in found_letters:
            found_letters.add(letter)
        else:
            return False
    else:
        return True


def has_all_unique_characters_without_ds(text):
    for key, group in itertools.groupby(sorted(text)):
        if len(list(group)) > 1:
            return False
    else:
        return True

